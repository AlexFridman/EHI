__author__ = 'AlexF'

import unittest

from LabWork2.code.model_creator_metaclass.field import IntField, StringField
from LabWork2.code.model_creator_metaclass import ModelCreatorMeta


class TestModelCreatorMetaMethods(unittest.TestCase):
    def test_object_fields_initialization(self):
        class Foo(metaclass=ModelCreatorMeta):
            name = StringField()
            age = IntField()

        foo = Foo(name='sasha', age=18)

        self.assertTrue(hasattr(foo, 'name'))
        self.assertTrue(hasattr(foo, 'age'))
        self.assertEqual('sasha', foo.name)
        self.assertEqual(18, foo.age)

    def test_object_fields_initialization_with_default_values(self):
        class Foo(metaclass=ModelCreatorMeta):
            name = StringField()
            age = IntField()

        foo = Foo()

        self.assertTrue(hasattr(foo, 'name'))
        self.assertTrue(hasattr(foo, 'age'))
        self.assertEqual('', foo.name)
        self.assertEqual(0, foo.age)

    def test_object_with_type_checked_fields(self):
        class Foo(metaclass=ModelCreatorMeta):
            name = StringField(perform_type_check=True)
            age = IntField(perform_type_check=True)

        self.assertRaises(TypeError, lambda: Foo(name=18))
        self.assertRaises(TypeError, lambda: Foo(age='sasha'))

    def test_object_with_type_casted_fields(self):
        class Foo(metaclass=ModelCreatorMeta):
            name = StringField(perform_type_cast=True)
            age = IntField(perform_type_cast=True)

        foo = Foo(name=18, age='18')

        self.assertTrue(hasattr(foo, 'name'))
        self.assertTrue(hasattr(foo, 'age'))
        self.assertEqual('18', foo.name)
        self.assertEqual(18, foo.age)

        self.assertRaises(ValueError, lambda: Foo(age='sasha'))

        class A:
            def __str__(self):
                return None

        self.assertRaises(ValueError, lambda: Foo(name=A()))

    def test_object_hierarchy_field_initialization(self):
        class Foo(metaclass=ModelCreatorMeta):
            name = StringField('petia')
            age = IntField(17)

        class Bar(Foo):
            name = StringField('sasha')

        bar = Bar()

        self.assertTrue(hasattr(bar, 'name'))
        self.assertTrue(hasattr(bar, 'age'))
        self.assertEqual('sasha', bar.name)
        self.assertEqual(17, bar.age)
