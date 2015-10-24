__author__ = 'AlexF'
import json
from LabWork2.code.attr_loader_meta.attrs_loading_error import AttrsLoadingError


class AttrLoaderMeta(type):
    def __new__(mcs, name, parents, dct):
        try:
            with open(mcs._attrs_path, 'r') as fp:
                attrs = json.load(fp)
                dct = mcs._merge_attrs(attrs, dct)
        except Exception:
            raise AttrsLoadingError()

        return super(AttrLoaderMeta, mcs).__new__(mcs, name, parents, dct)

    def _merge_attrs(attrs_1: dict, attrs_2: dict):
        result = attrs_1.copy()
        for name, value in attrs_2.items():
            if name not in result:
                result[name] = value
        return result

    @classmethod
    def create(mcs, attrs_path):
        AttrLoaderMeta._attrs_path = attrs_path
        return AttrLoaderMeta
