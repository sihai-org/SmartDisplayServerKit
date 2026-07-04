import asyncio
from abc import ABC, abstractmethod
from typing import Any, ClassVar, Self


class SingletonAsync(ABC):
    _instance: ClassVar[Self | None] = None
    _lock: ClassVar[asyncio.Lock] = asyncio.Lock()

    @classmethod
    @abstractmethod
    async def init(cls, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError

    @classmethod
    async def _set_instance(cls, new_instance: Self) -> None:
        async with cls._lock:
            if cls._instance is None:
                cls._instance = new_instance

    @classmethod
    def instance(cls) -> Self:
        instance = cls._instance
        if instance is None:
            raise RuntimeError(f"{cls.__name__} has not been initialized")
        return instance
