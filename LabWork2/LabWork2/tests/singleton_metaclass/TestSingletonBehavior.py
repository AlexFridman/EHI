__author__ = 'AlexF'

import unittest
from LabWork2.code.singleton_metaclass.singleton import Singleton


class TestSingletonBehavior(unittest.TestCase):
    def test_reference_equality_with_nonparametric_ctor(self):
        class SimpleSingleton(metaclass=Singleton):
            pass

        ref_1 = SimpleSingleton()
        ref_2 = SimpleSingleton()

        self.assertIs(ref_1, ref_2)

    def test_reference_equality_with_parametric_ctor(self):
        class SimpleSingleton(metaclass=Singleton):
            def __init__(self, attr):
                self._attr = attr

            @property
            def attr(self):
                return self._attr

        ref_1 = SimpleSingleton('test_1')
        ref_2 = SimpleSingleton('test_2')

        self.assertIs(ref_1, ref_2)
        self.assertEquals(ref_1.attr, 'test_1')

    def test_reference_equality_with_inheritance(self):
        class BaseSingleton(metaclass=Singleton):
            pass

        class DerivedSingleton(BaseSingleton):
            pass

        ref_1 = DerivedSingleton()
        ref_2 = DerivedSingleton()

        self.assertIs(ref_1, ref_2)


if __name__ == '__main__':
    unittest.main()
