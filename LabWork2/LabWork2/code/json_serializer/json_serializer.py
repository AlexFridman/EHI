__author__ = 'AlexF'

from functools import singledispatch

NoneType = type(None)


class JsonSerializer:
    @classmethod
    def dumps(cls, arg):
        return to_json(arg)

    @classmethod
    def loads(cls, arg):
        return from_json(arg)


@singledispatch
def to_json(arg):
    return arg


@to_json.register(tuple)
@to_json.register(list)
def _(arg):
    return '[' + ', '.join(_serialize_children(arg)) + ']'


@to_json.register(dict)
def _(arg):
    return '{' + ', '.join(['{}: {}'.format(to_json(k), to_json(v))
                            for k, v in sorted(arg.items(), key=lambda x: str(x[0]))]) + '}'


def _serialize_children(children: list):
    return [to_json(c_i) for c_i in children]


@to_json.register(int)
@to_json.register(float)
def _(arg):
    return str(arg)


@to_json.register(str)
def _(arg):
    # zaikranirovatb
    return '\"' + arg + '\"'


@to_json.register(NoneType)
def _(arg):
    return 'null'


@singledispatch
def from_json(arg):
    return arg


if __name__ == '__main__':
    pass
