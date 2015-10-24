__author__ = 'AlexF'

import unittest

from LabWork2.code.cached_decorator.cached import cached


class TestCachedBehavior(unittest.TestCase):
    def test_caching_with_class_instance(self):
        class IntWrapper:
            def __init__(self, value):
                self.value = value

        @cached
        def simple_function(x: IntWrapper):
            return x.value + 1

        arg = IntWrapper(5)
        result_1 = simple_function(arg)
        arg.value += 1
        result_2 = simple_function(arg)

        self.assertIs(6, result_1)
        self.assertIs(6, result_2)


if __name__ == '__main__':
    unittest.main()
