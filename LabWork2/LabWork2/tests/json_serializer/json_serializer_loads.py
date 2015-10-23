__author__ = 'AlexF'

import unittest
from LabWork2.code.json_serializer.json_serializer import JsonSerializer
import json

class TestJsonSerializerLoadsMethod(unittest.TestCase):
    def test_none_deserialization(self):
        data = None

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_int_serialization(self):
        data = 1

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_float_serialization(self):
        data = 1.1111

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_simple_str_serialization(self):
        data = 'test_str'

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_tuple_of_ints_serialization(self):
        data = (1, 2)

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_tuple_of_strs_serialization(self):
        data = ('1', '2')

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_tuple_of_diff_type_args_serialization(self):
        data = ('1', 2, 3.3, (4,), None, 56)

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_list_of_ints_serialization(self):
        data = [1, 2]

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_list_of_strs_serialization(self):
        data = ['1', '2']

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_list_of_diff_type_args_serialization(self):
        data = ['1', 2, 3.3, (4,)]

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_dict_of_int_keys_serialization(self):
        data = {1: 1, 2: 2}

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_dict_with_str_keys_serialization(self):
        data = {'1': 1, '2': 2}

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_dict_with_str_keys_and_values_serialization(self):
        data = {'1': '1', '2': '2'}

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))

    def test_dict_with_diff_type_keys_and_values_serialization(self):
        data = {'1': '1', 2: '2', 3: None}

        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonSerializer.loads(json_data))


if __name__ == '__main__':
    unittest.main()
