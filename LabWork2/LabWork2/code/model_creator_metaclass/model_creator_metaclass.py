__author__ = 'AlexF'

from .field import Field


class ModelCreatorMeta(type):
    def __new__(mcs, name, parents, dct):
        def init(self, *args, **kwargs):
            fields_to_create = self.fields_to_create

            for f_name, f_obj in fields_to_create.items():
                f_value = kwargs.get(f_name, None)
                self.__dict__[f_name] = f_obj.proceed_value(f_value)

        field_prots = ModelCreatorMeta._extract_field_prototypes(dct)
        mcs._delete_field_prots(dct, field_prots)
        parents_field_prots = mcs._extract_parents_field_prototypes(parents)
        dct['fields_to_create'] = mcs._merge_field_prots_lists(parents_field_prots, field_prots)
        dct['__init__'] = init
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


if __name__ == '__main__':
    from LabWork2.code.model_creator_metaclass.field import StringField, IntField


    class Foo(metaclass=ModelCreatorMeta):
        name = StringField('petia')


    class Bar(Foo):
        age = IntField()
        name = StringField('sasha')


    print(Bar().__dict__)
