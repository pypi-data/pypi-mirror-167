from typing import Any, Optional
import asyncio
import time
import copy

class CacheValue():
    """
    Maplecache cache value
    
    This is internal and should never be used
    """
    def __init__(self, parent: "Cache", key: str, value: Any, *, expiry: int | float):
        self._val = value
        self.parent = parent
        self.key = key
        self.expiry = expiry

        # Start task to clear from cache when expired
        if expiry:
            self.cleanup = asyncio.create_task(self._clear_cache())

    async def _clear_cache(self):
        """Clears the cache"""
        expiry = self.expiry - time.time()
        await asyncio.sleep(expiry)
        self.parent.remove(self.key)
        self._val = None # Clear value
        return
            
    def expired(self):
        if not self.expiry:
            return False
        return self.expiry < time.time()
    
    def borrow(self) -> "BorrowedCacheValue":
        return BorrowedCacheValue(
            self.key,
            self._val,
            expiry=self.expiry,
        )
    
    def remove(self):
        """Removes this cache"""
        self._val = None
        self.cleanup.cancel()
        self.expiry = 0
    
    def edit(self, value: Any, *, expiry: Optional[int | float] = None):
        """Edit the value and expiry"""
        self._val = value
        if expiry:
            self.expiry = expiry
            self.cleanup.cancel()
        self.cleanup = asyncio.create_task(self._clear_cache())

class BorrowedCacheValue():
    """
    Maplecache borrowed cache value (borrowed from cache)
    
    The system of borrowing is used to avoid ratelimits and help in memory management
    """
    __slots__ = ("_init", "_val", "key", "expiry", "empty")
    def __init__(self, key: str, value: Any, *, expiry: int | float):
        self._init = True
        self._val = value
        self.key = key
        self.expiry = expiry
        self.empty = self._val is None

        self._init = False

    def __repr__(self):
        return f"<CacheValue value={self._val} expiry={self.expiry} empty={self.empty}>"

    def __str__(self):
        return self.__repr__()
    
    def value(self):
        return self._val
    
    def expired(self):
        if not self.expiry:
            return False
        return self.expiry < time.time()
    
    def __delattr__(self, __name: str) -> None:
        raise AttributeError("Cannot delete attributes on borrowed cache value")

    def __setattr__(self, name: str, value: Any):
        if getattr(self, "_init", True):
            return super().__setattr__(name, value)
        raise AttributeError("Cannot set attributes on borrowed cache value")

class Cache():
    """
    Cache for Maplecache with expiry
    

    **This is the class you likely want to see in this library**
    """

    __slots__ = ["_cache"]

    def __init__(self):
        self._cache: dict[str, CacheValue] = {}

        # Start task to clear cache
        asyncio.create_task(self._clear_cache())
    
    def remove(self, key: str) -> bool:
        """Deletes a value from the cache"""
        try:
            del self._cache[key]
            return True
        except:
            return False
    
    async def _clear_cache(self):
        """Clears the cache"""
        while True:
            to_remove = []
            for key in self._cache:
                if self._cache[key].expired():
                    to_remove.append(key)
            
            for key in to_remove:
                self._cache[key].remove()
                self.remove(key)
            await asyncio.sleep(360)
    
    def get(self, key: str) -> Optional[BorrowedCacheValue]:
        """Gets a snippet from the cache"""
        if key in self._cache:
            cached_data = self._cache[key]
            if cached_data.expired():
                self.remove(key)
                return None
            return cached_data.borrow()
        return None
    
    def set(self, key: str, value: Any, *, expiry: Optional[int | float] = None, deepcopy: bool = True) -> Any:
        """Sets a value in the cache"""
        if isinstance(value, CacheValue):
            raise TypeError("Value must not be of type CacheValue")

        value = copy.deepcopy(value) if deepcopy else value

        if key in self._cache:
            self._cache[key].edit(value, expiry=expiry)

        self._cache[key] = CacheValue(
            self,
            key,
            value,
            expiry=(time.time() + expiry) if expiry else None,
        )    

    def entries(self):
        """Returns all entries in the cache"""
        return self._cache.items()