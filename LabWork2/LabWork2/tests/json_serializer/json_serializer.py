__author__ = 'AlexF'

import unittest
from LabWork2.code.json_serializer.json_serializer import JsonSerializer


class TestJsonSerializerMethods(unittest.TestCase):
    def test_int_serialization(self):
        data = 1

        self.assertEqual('1', JsonSerializer.dumps(data))

    def test_float_serialization(self):
        data = 1.1111

        self.assertEqual('1.1111', JsonSerializer.dumps(data))

    def test_simple_str_serialization(self):
        data = 'test_str'

        self.assertEqual('\"test_str\"', JsonSerializer.dumps(data))

    def test_tuple_of_ints_serialization(self):
        data = (1, 2)

        self.assertEqual('[1, 2]', JsonSerializer.dumps(data))

    def test_tuple_of_strs_serialization(self):
        data = ('1', '2')

        self.assertEqual('[\"1\", \"2\"]', JsonSerializer.dumps(data))

    def test_tuple_of_diff_type_args_serialization(self):
        data = ('1', 2, 3.3, (4,))

        self.assertEqual('[\"1\", 2, 3.3, [4]]', JsonSerializer.dumps(data))

    def test_list_of_ints_serialization(self):
        data = [1, 2]

        self.assertEqual('[1, 2]', JsonSerializer.dumps(data))

    def test_list_of_strs_serialization(self):
        data = ['1', '2']

        self.assertEqual('[\"1\", \"2\"]', JsonSerializer.dumps(data))

    def test_list_of_diff_type_args_serialization(self):
        data = ['1', 2, 3.3, (4,)]

        self.assertEqual('[\"1\", 2, 3.3, [4]]', JsonSerializer.dumps(data))

    def test_dict_of_int_keys_serialization(self):
        data = {1: 1, 2: 2}

        self.assertEqual('{1: 1, 2: 2}', JsonSerializer.dumps(data))

    def test_dict_with_str_keys_serialization(self):
        data = {'1': 1, '2': 2}

        self.assertEqual('{\"1\": 1, \"2\": 2}', JsonSerializer.dumps(data))

    def test_dict_with_str_keys_and_values_serialization(self):
        data = {'1': '1', '2': '2'}

        self.assertEqual('{\"1\": \"1\", \"2\": \"2\"}', JsonSerializer.dumps(data))


if __name__ == '__main__':
    unittest.main()
