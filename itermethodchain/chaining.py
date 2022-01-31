from functools import reduce
from typing import Callable, Generic, Iterable, TypeVar, Union

T = TypeVar("T")
U = TypeVar("U")
TIterMethodChain = TypeVar("TIterMethodChain", bound="IterMethodChain")

class IterMethodChain(Generic[T]):
    def __init__(self, iterable: Iterable[T]):
        self._iter = iterable

    def map(self, func: Callable[[T], U]) -> TIterMethodChain:
        return IterMethodChain(map(func, self._iter))

    def filter(self, func: Callable[[T], bool]) -> TIterMethodChain:
        return IterMethodChain(filter(func, self._iter))

    def list(self) -> Iterable[T]:
        return list(self._iter)

    def reduce(self, func: Callable[[T, U], T], initializer: Union[T, None]=None) -> T:
        if initializer:
            return reduce(func, self._iter, initializer)
        else:
            return reduce(func, self._iter)