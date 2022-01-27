from functools import reduce
from typing import Callable, Iterable, TypeVar

TIterMethodChain = TypeVar("TIterMethodChain", bound="IterMethodChain")

class IterMethodChain:
    def __init__(self, iterable: Iterable):
        self._iter = iterable

    def map(self, func: Callable) -> TIterMethodChain:
        return IterMethodChain(map(func, self._iter))

    def filter(self, func: Callable) -> TIterMethodChain:
        return IterMethodChain(filter(func, self._iter))

    def list(self) -> Iterable:
        return list(self._iter)

    def reduce(self, func: Callable, initializer=None):
        if initializer:
            return reduce(func, self._iter, initializer)
        else:
            return reduce(func, self._iter)