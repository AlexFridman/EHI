__author__ = 'AlexF'

import unittest
from LabWork2.code.linear_function.linear_function import LinearFunction, Parameter, Constant


class TestLinearFunctionMethods(unittest.TestCase):
    def test_addition(self):
        param_1 = Parameter('x')
        const_1 = Constant(5)
        add_1 = const_1 + param_1

        self.assertEqual(10, add_1(5))

    def test_multiplication(self):
        param_1 = Parameter('x')
        const_1 = Constant(5)
        mul_1 = const_1 * param_1

        self.assertEqual(25, mul_1(5))

    def test_composition(self):
        param_1 = Parameter('x')
        const_1 = Constant(5)
        mul_1 = const_1 * param_1
        doubler = LinearFunction(lambda x: x * 2, [], 'sqrt({})')
        doubler_1 = doubler(mul_1)

        self.assertEqual(50, doubler(25))


if __name__ == '__main__':
    unittest.main()
