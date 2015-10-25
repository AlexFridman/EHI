__author__ = 'AlexF'

from LabWork2.code.model_creator_metaclass.field import Field


class ModelCreatorMeta(type):
    def __new__(mcs, name, parents, dct):
        field_prots = ModelCreatorMeta._extract_field_prototypes(dct)
        mcs._delete_field_prots(dct, field_prots)
        parents_field_prots = mcs._extract_parents_field_prototypes(parents)
        dct['fields_to_create'] = mcs._merge_field_prots_lists(parents_field_prots, field_prots)
        mcs._add_pre_init_logic(dct)
        return super(ModelCreatorMeta, mcs).__new__(mcs, name, parents, dct)

    def _extract_field_prototypes(classdict):
        return dict([(f_name, f_value)
                     for f_name, f_value in classdict.items()
                     if isinstance(f_value, Field)])

    def _extract_parents_field_prototypes(parents):
        parents_field_prots = {}
        for parent in reversed(parents):
            if 'fields_to_create' in parent.__dict__:
                parents_field_prots.update(parent.__dict__['fields_to_create'])
        return parents_field_prots

    def _delete_field_prots(dct, field_prots):
        [dct.pop(field_name) for field_name in field_prots.keys()]

    def _merge_field_prots_lists(fpl_1, fpl_2):
        for k, v in fpl_2.items():
            fpl_1[k] = v

        return fpl_1

    @classmethod
    def _add_pre_init_logic(mcs, dct: dict):
        if '__init__' in dct and callable(dct['__init__']):
            dct['__init__'] = mcs._pre_init_decorator(dct['__init__'], mcs._pre_init_logic)
        else:
            dct['__init__'] = mcs._pre_init_logic

    def _pre_init_decorator(func, pre_init_logic):
        def inner(self, *args, **kwargs):
            pre_init_logic(self, *args, **kwargs)
            init_arg_names = set(func.__code__.co_varnames)
            init_kwargs = dict([(name, value) for name, value in kwargs.items() if name in init_arg_names])
            func(self, *args, **init_kwargs)

        return inner

    def _pre_init_logic(self, *args, **kwargs):
        fields_to_create = self.fields_to_create

        for f_name, f_obj in fields_to_create.items():
            if f_name not in self.__dict__:
                f_value = kwargs.get(f_name, None)
                self.__dict__[f_name] = f_obj.proceed_value(f_value)


if __name__ == '__main__':
    from LabWork2.code.model_creator_metaclass.field import StringField, IntField


    class Foo(metaclass=ModelCreatorMeta):
        def __init__(self, name):
            self.name = name

        name = StringField('petia')


    class Bar(Foo):
        age = IntField()
        name = StringField('sasha')


    foo = Foo(name='hello')
    print(foo.__dict__)
