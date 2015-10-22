__author__ = 'AlexF'


class DimensionMismatch(Exception):
    def __init__(self):
        super(Exception, self).__init__('dimension mismatch')
