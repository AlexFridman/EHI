__author__ = 'AlexF'
import json

from .attrs_loading_error import AttrsLoadingError


class JsonAttrLoaderMeta(type):
    def __new__(mcs, name, parents, dct):
        try:
            with open(mcs._attrs_path, 'r') as fp:
                attrs = json.load(fp)
                dct = mcs._merge_attrs(attrs, dct)
        except Exception:
            raise AttrsLoadingError()

        return super(JsonAttrLoaderMeta, mcs).__new__(mcs, name, parents, dct)

    def _merge_attrs(attrs_1: dict, attrs_2: dict):
        result = attrs_1.copy()
        result.update(attrs_2)
        return result

    @classmethod
    def create(mcs, attrs_path):
        JsonAttrLoaderMeta._attrs_path = attrs_path
        return JsonAttrLoaderMeta
