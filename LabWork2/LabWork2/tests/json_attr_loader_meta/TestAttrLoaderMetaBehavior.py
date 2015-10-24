__author__ = 'AlexF'

import unittest
import json
import os

from LabWork2.code.attr_loader_meta.json_attr_loading_meta import AttrLoaderMeta
from LabWork2.code.attr_loader_meta.attrs_loading_error import AttrsLoadingError


class TestAttrLoaderMetaBehavior(unittest.TestCase):
    def test_attrs_loading(self):
        attrs_file_path = 'attrs.json'
        attrs = {'a': 1, 'b': [1, 2, 3], 'c': [1, 2, 3]}
        with open(attrs_file_path, 'w+') as fp:
            json.dump(attrs, fp)

        class Foo(metaclass=AttrLoaderMeta.create(attrs_file_path)):
            attrs_path = attrs_file_path

        os.remove(attrs_file_path)
        for attr_name, value in attrs.items():
            self.assertTrue(hasattr(Foo, attr_name))
            self.assertEqual(value, getattr(Foo, attr_name))

    def test_attrs_load_from_not_existing_file(self):
        attrs_file_path = 'foobar'

        def define_class():
            class Foo(metaclass=AttrLoaderMeta.create(attrs_file_path)):
                attrs_path = attrs_file_path

        self.assertRaises(AttrsLoadingError, lambda: define_class())


if __name__ == '__main__':
    unittest.main()
