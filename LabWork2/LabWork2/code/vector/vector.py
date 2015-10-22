__author__ = 'AlexF'

from collections import Iterable
from .dimension_mismatch import DimensionMismatch


class Vector:
    def __init__(self, arg, dtype=None):
        if isinstance(arg, int):
            if arg < 0:
                raise ValueError('size must be greather or equal than 0')
            self._values = []
            self._size = arg
            self._dtype = dtype or int
        elif isinstance(arg, Iterable):
            if dtype is None:
                dtype = arg[0]
                if not all([type(v_i) for v_i in arg]):
                    raise TypeError('all item in Iterable must be the same type')
                self._values = list(arg)
            else:
                self._values = [dtype(v_i) for v_i in arg]
            self._size = len(self._values)
            self._dtype = dtype
        else:
            raise TypeError('Vector() requires int or Iterable')

    def __len__(self):
        return self._size

    def __getitem__(self, key):
        return self._values[key]

    def __setitem__(self, key, value):
        if isinstance(value, self._dtype):
            self._values[key] = value
        else:
            raise TypeError('value is not instance of %s' % self._dtype)

    def _check_type(self, other):
        if not isinstance(other, Vector):
            raise TypeError('other must be the instance of Vector')

    def _check_dimension_match(self, other):
        if self.size != other.size:
            raise DimensionMismatch()

    def __add__(self, other):
        self._check_type(other)
        self._check_dimension_match(other)
        return Vector([self_i + other_i for self_i, other_i in zip(self, other)])

    def __sub__(self, other):
        self._check_type(other)
        self._check_dimension_match(other)
        return Vector([self_i - other_i for self_i, other_i in zip(self, other)])

    def dot(self, other):
        self._check_type(other)
        self._check_dimension_match(other)
        return sum([self_i * other_i for self_i, other_i in zip(self, other)])

    @property
    def size(self):
        return self._size

    @property
    def dtype(self):
        return self._dtype

    def __iter__(self):
        return self._values.__iter__()

    def __str__(self):
        return str(self._values)

    def __repr__(self):
        return 'Vector(%s)' % str(self)

    def __eq__(self, other):
        return len(self) == len(other) and \
               all([self_i == other_i for self_i, other_i in zip(self, other)])
