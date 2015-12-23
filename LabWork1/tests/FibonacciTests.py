import math
from unittest import TestCase
from LabWork1.code.fibonacci import fibonacci


class FibonacciTests(TestCase):
    def test_base_case(self):
        def direct_fibonacci(n):
            return int(((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (2 ** n * math.sqrt(5)))

        fib_gen = fibonacci()
        self.assertSequenceEqual([direct_fibonacci(i) for i in range(10)],
                                 [next(fib_gen) for __ in range(10)])
