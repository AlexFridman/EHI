__author__ = 'AlexF'

import unittest
from LabWork2.code.vector.vector import Vector
from LabWork2.code.vector.dimension_mismatch import DimensionMismatch


class TestVectorMathMethods(unittest.TestCase):
    def test_addition(self):
        vect_1 = Vector([1] * 5)
        vect_2 = Vector([1] * 5)

        self.assertSequenceEqual([2] * 5, vect_1 + vect_2)

    def test_addition_of_not_same_length_vectors_raises_exception(self):
        vect_1 = Vector([1] * 5)
        vect_2 = Vector([1] * 1)

        self.assertRaises(DimensionMismatch, lambda: vect_1 + vect_2)

    def test_subtraction(self):
        vect_1 = Vector([1] * 5)
        vect_2 = Vector([1] * 5)

        self.assertSequenceEqual([0] * 5, vect_1 - vect_2)

    def test_subtraction_of_not_same_length_vectors_raises_exception(self):
        vect_1 = Vector([1] * 5)
        vect_2 = Vector([1] * 1)

        self.assertRaises(DimensionMismatch, lambda: vect_1 - vect_2)

    def test_dot_product(self):
        vect_1 = Vector([2] * 5)
        vect_2 = Vector([1] * 5)

        self.assertEqual(10, vect_1.dot(vect_2))

    def test_dot_product_of_not_same_length_vectors_raises_exception(self):
        vect_1 = Vector([1] * 5)
        vect_2 = Vector([1] * 1)

        self.assertRaises(DimensionMismatch, lambda: vect_1.dot(vect_2))

    def test_equality(self):
        vect_1 = Vector([1] * 5)
        vect_2 = Vector([1] * 5)
        vect_3 = Vector([1] * 1)
        vect_4 = Vector([1] * 5, float)

        self.assertEqual(True, vect_1 == vect_2)
        self.assertEqual(False, vect_1 == vect_3)
        self.assertEqual(True, vect_1 == vect_4)

    def test_scalar_multiplication(self):
        vect_1 = Vector([1] * 5)

        self.assertSequenceEqual([2] * 5, vect_1 * 2)


if __name__ == '__main__':
    unittest.main()
