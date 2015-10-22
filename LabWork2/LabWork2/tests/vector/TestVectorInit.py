__author__ = 'AlexF'

import unittest
from LabWork2.code.vector.vector import Vector


class TestVectorInit(unittest.TestCase):
    def test_init_when_int_passed(self):
        vector = Vector(0, float)

        self.assertEqual(0, vector.size)
        self.assertEqual(float, vector.dtype)

    def test_init_when_neg_int_passed(self):
        inst = lambda: Vector(-1)

        self.assertRaises(ValueError, inst)

    def test_inst_when_iterable_passed(self):
        arg = [1, 2, 3, 4, 5]
        vector = Vector(arg)

        self.assertSequenceEqual(arg, vector)
        self.assertEqual(len(arg), vector.size)
        self.assertEqual(int, vector.dtype)

    def test_inst_when_iterable_and_dtype_passed(self):
        arg = [1, 2, 3, 4, 5]
        dtype = float
        vector = Vector(arg, dtype)

        self.assertSequenceEqual([float(a_i) for a_i in arg], vector)
        self.assertEqual(len(arg), vector.size)
        self.assertEqual(float, vector.dtype)

    def test_inst_when_iterable_of_diff_types_objects_passed(self):
        arg = [1, 2, 3, 4, 5]
        inst = lambda: Vector(arg)

        self.assertRaises(TypeError, inst)


if __name__ == '__main__':
    unittest.main()
