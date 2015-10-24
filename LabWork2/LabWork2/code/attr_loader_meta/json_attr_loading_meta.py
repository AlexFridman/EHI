__author__ = 'AlexF'
import json
from .attrs_loading_error import AttrsLoadingError


class AttrLoaderMeta(type):
    def __new__(cls, name, parents, dct):
        if 'attrs_path' in dct:
            try:
                with open(dct['attrs_path'], 'r') as fp:
                    attrs = json.load(fp)
            except (FileNotFoundError, FileExistsError, ValueError):
                raise AttrsLoadingError()

        del dct['attrs_path']
        dct.update(attrs)

        return super(AttrLoaderMeta, cls).__new__(cls, name, parents, dct)


if __name__ == '__main__':
    attrs_path = 'D:/attrs/attrs.json'
    obj = AttrLoaderMeta('Foo', (), {'attrs_path': attrs_path})
    print(obj.__dict__)
