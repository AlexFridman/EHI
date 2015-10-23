__author__ = 'AlexF'

from functools import singledispatch


class JsonSerializer:
    @classmethod
    def dumps(cls, arg):
        return to_json(arg)


@singledispatch
def to_json(arg):
    return arg


@to_json.register(tuple)
@to_json.register(list)
def _(arg):
    return '[' + ', '.join(_serialize_children(arg)) + ']'


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


@to_json.register(dict)
def _(arg):
    return '{' + ', '.join(['{}: {}'.format(to_json(k), to_json(v))
                            for k, v in sorted(arg.items(), key=lambda x: x[0])]) + '}'


if __name__ == '__main__':
    data = (1, 2)
    t = to_json(data)
    print(JsonSerializer.dumps(data))
