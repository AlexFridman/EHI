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
        root = LinearFunction(lambda x: x ** (1 / 2), [], 'sqrt({})')
        root_1 = root(mul_1)

        self.assertEqual(5, root_1(25))


if __name__ == '__main__':
    unittest.main()
