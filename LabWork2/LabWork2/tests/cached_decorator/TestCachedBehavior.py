__author__ = 'AlexF'

import unittest
from LabWork2.code.cached_decorator.cached import cached


class TestCachedBehavior(unittest.TestCase):
    def test_caching(self):
        @cached
        def simple_function(x: tuple):
            return x

        arg = ('test',)
        result_1 = simple_function(arg)
        result_2 = simple_function(arg)

        self.assertIs(arg, result_1)
        self.assertIs(arg, result_2)

if __name__ == '__main__':
    unittest.main()
