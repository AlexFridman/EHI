__author__ = 'AlexF'


class _defaultdict(dict):
    def __init__(self, default_factory=None, *a, **kw):
        dict.__init__(self, *a, **kw)
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory()
        return value

    def __repr__(self):
        return dict.__repr__(self)


RecursiveDefaultdict = lambda: _defaultdict(RecursiveDefaultdict)

if __name__ == '__main__':
    rdd = RecursiveDefaultdict()
    rdd['a']['b']['c'] = 2
    print(rdd)
