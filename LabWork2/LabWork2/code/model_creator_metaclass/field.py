__author__ = 'AlexF'


class Field:
    def __init__(self, dtype, default_value, perform_type_check=False, perform_type_cast=False):
        self._dtype = dtype
        self._default_value = default_value
        self._perform_type_check = perform_type_check
        self._perform_type_cast = perform_type_cast

    def check_type(self, value):
        return isinstance(value, self._dtype)

    def cast(self, value):
        return self._dtype(value)

    def proceed_value(self, value):
        if self._perform_type_check and not self.check_type(value):
            raise TypeError('type mismatch')
        if self._perform_type_cast and not isinstance(value, self._dtype):
            try:
                value = self.cast(value)
            except TypeError:
                raise TypeError('unsuccessful type cast')
        if value is None:
            value = self._default_value

        return value


class StringField(Field):
    def __init__(self, def_val='', perform_type_check=False, perform_type_cast=False):
        super(StringField, self).__init__(str, def_val, perform_type_check, perform_type_cast)


class IntField(Field):
    def __init__(self, def_val=0, perform_type_check=False, perform_type_cast=False):
        super(StringField, self).__init__(int, def_val, perform_type_check, perform_type_cast)
