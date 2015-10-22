__author__ = 'AlexF'

import unittest
from LabWork2.code.xrange.xrange import Xrange


class TestXrangeMethods(unittest.TestCase):
    def test_xrange_iterator(self):
        iter_1 = Xrange(10)
        iter_2 = Xrange(1, 10)
        iter_3 = Xrange(0, 10, 2)

        self.assertSequenceEqual(range(10), iter_1)
        self.assertSequenceEqual(range(1, 10), iter_2)
        self.assertSequenceEqual(range(0, 10, 2), iter_3)

    def test_indexing(self):
        iter = Xrange(10)

        self.assertIn(0, iter)
        self.assertNotIn(10, iter)

    def test_index(self):
        iter = Xrange(10)

        self.assertEqual(0, iter.index(0))
        self.assertEqual(10, iter.index(9))

    def test_count(self):
        iter = Xrange(10)

        self.assertEqual(0, iter.count(0))
        self.assertEqual(1, iter.count(1))

    def test_reversed(self):
        iter_1 = reversed(Xrange(10))
        iter_2 = reversed(Xrange(0, -10, -2))

        self.assertSequenceEqual(reversed(range(10)), iter_1)
        self.assertSequenceEqual(reversed(range(0, -10, -2)), iter_2)


if __name__ == '__main__':
    unittest.main()
