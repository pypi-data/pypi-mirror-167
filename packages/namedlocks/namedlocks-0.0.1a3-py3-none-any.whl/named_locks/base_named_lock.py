from asyncio import Lock as AsyncLock
from collections import defaultdict
from multiprocessing import Lock as ProcessLock
from threading import Lock as ThreadLock
from typing import Hashable, Union

BaseLocks = Union[AsyncLock, ThreadLock, ProcessLock]


class BaseNamedLock:
    __slots__ = ("_locks",)

    def __init__(self):
        self._locks: defaultdict[Hashable, BaseLocks]

    def _cleanup(self, name: Hashable):
        raise NotImplementedError

    def lock(self, name: Hashable):
        raise NotImplementedError

    def __repr__(self):
        return "<%s _locks_size(%s)>" % (self.__class__.__name__, len(self._locks))
