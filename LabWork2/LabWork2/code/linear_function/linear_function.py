__author__ = 'AlexF'


class LinearFunction:
    def __init__(self, expression, children, format_str):
        self._expression = expression
        self._children = children
        self._format_str = format_str

    def __str__(self):
        return self._format_str.format(*self._children)

    def __call__(self, x):
        return self._expression(x)

    def __add__(self, other):
        return LinearFunction(lambda x: self(x) + other(x), [self, other], '{} + {}')

    def __mul__(self, other):
        return LinearFunction(lambda x: self(x) * other(x), [self, other], '({}) * ({})')

    def composition(self, other):
        return LinearFunction(lambda x: other(self(x)), [other, self], '{}({})')


class Parameter(LinearFunction):
    def __init__(self, param_name):
        super(Parameter, self).__init__(lambda x: x, [param_name], '{}')


class Constant(LinearFunction):
    def __init__(self, value):
        super(Constant, self).__init__(lambda x: value, [value], '{}')


if __name__ == '__main__':
    param_1 = Parameter('x')
    const_1 = Constant(5)
    add_1 = const_1 + param_1
    print(add_1)
    print(add_1(5))
