__author__ = 'AlexF'

import unittest
from LabWork2.code.filterable_list.filterable_list import FilterableList


class TestFilterableListMethods(unittest.TestCase):
    def test_filtering(self):
        f_collection = FilterableList(range(10 + 1))
        filtering_result = f_collection.filter(lambda x: x % 2 == 0)

        self.assertSequenceEqual(range(0, 10 + 1, 2), filtering_result)


if __name__ == '__main__':
    unittest.main()
