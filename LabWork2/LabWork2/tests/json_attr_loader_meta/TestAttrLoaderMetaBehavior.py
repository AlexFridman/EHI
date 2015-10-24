__author__ = 'AlexF'

import unittest
import json
from LabWork2.code.attr_loader_meta.json_attr_loading_meta import AttrLoaderMeta
import os


class TestAttrLoaderMetaBehavior(unittest.TestCase):
    def test_attrs_loading(self):
        attrs_file_path = 'attrs.json'
        attrs = {'a': 1, 'b': [1, 2, 3], 'c': [1, 2, 3]}
        with open(attrs_file_path, 'w+') as fp:
            json.dump(attrs, fp)

        class Foo(metaclass=AttrLoaderMeta):
            attrs_path = attrs_file_path

        instance = Foo()

        os.remove(attrs_file_path)
        for attr_name, value in attrs.items():
            self.assertTrue(hasattr(instance, attr_name))
            self.assertEqual(value, getattr(instance, attr_name))

            # def test_attrs_load_from_not_existing(self):
            #     attrs_file_path = 'foobar'
            #
            #     class Foo(metaclass=AttrLoaderMeta):
            #         attrs_path = attrs_file_path
            #
            #     self.assertRaises(AttrsLoadingError, lambda: Foo())


if __name__ == '__main__':
    unittest.main()
