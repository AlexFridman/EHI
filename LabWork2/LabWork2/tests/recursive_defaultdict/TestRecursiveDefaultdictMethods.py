__author__ = 'AlexF'

import unittest
from LabWork2.code.recursive_defaultdict.recursive_defaultdict import RecursiveDefaultdict


class TestRecursiveDefaultdictMethods(unittest.TestCase):
    def test_recursion(self):
        rdd = RecursiveDefaultdict()

        rdd['a']['b']['c'] = 1
        rdd['b']['c']['d'] = 2

        self.assertEqual(1, rdd['a']['b']['c'])
        self.assertEqual(2, rdd['b']['c']['d'])

    def test_str_repr(self):
        rdd = RecursiveDefaultdict()

        rdd['a']['b']['c'] = 1
        self.assertEqual({'a': {'b': {'c': 1}}}, rdd)

        rdd['b']['c']['d'] = 2
        self.assertEqual({'b': {'c': {'d': 2}}, 'a': {'b': {'c': 1}}}, rdd)
