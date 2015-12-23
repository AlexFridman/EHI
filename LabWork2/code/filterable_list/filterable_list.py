__author__ = 'AlexF'

from collections import Iterator


class FilterableList(list):
    class _UnexhaustableIterator(Iterator):
        def __init__(self, iterable_obj):
            self._iterable = iterable_obj
            self._current = -1

        def __iter__(self):
            return self

        def __next__(self):
            self._current += 1
            return self._iterable[self._current % len(self._iterable)]

    def filter(self, predicate):
        return FilterableList([i for i in self if predicate(i)])

    def __getitem__(self, key):
        return super(FilterableList, self).__getitem__(key % len(self))
