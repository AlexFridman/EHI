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
    dict_keys = arg.keys()
    if not _check_dict_keys(dict_keys):
        raise TypeError("keys must be a string or a number")

    keys = _normalize_dict_keys_when_serializing(list(dict_keys))
    values = arg.values()

    return '{' + ', '.join(['{}: {}'.format(to_json(k), to_json(v))
                            for k, v in sorted(zip(keys, values), key=lambda x: str(x[0]))]) + '}'


def _check_dict_keys(dict_keys):
    return all([isinstance(k, (str, float, int)) for k in dict_keys])


def _normalize_dict_keys_when_serializing(keys: list):
    norm_keys = []
    for key in keys:
        if isinstance(key, (int, float)):
            norm_keys.append(str(key))
        else:
            norm_keys.append(key)

    return norm_keys


def _serialize_children(children: list):
    return [to_json(c_i) for c_i in children]


@to_json.register(int)
@to_json.register(float)
def _(arg):
    return str(arg)


@to_json.register(str)
def _(arg):
    return '\"' + arg.replace('\'', '\"') + '\"'


@to_json.register(NoneType)
def _(arg):
    return 'null'


TOKEN_NONE = 'TOKEN_NONE';
TOKEN_CURLY_OPEN = 'TOKEN_CURLY_OPEN';
TOKEN_CURLY_CLOSE = 'TOKEN_CURLY_CLOSE';
TOKEN_SQUARED_OPEN = 'TOKEN_SQUARED_OPEN';
TOKEN_SQUARED_CLOSE = 'TOKEN_SQUARED_CLOSE';
TOKEN_COLON = 'TOKEN_COLON';
TOKEN_COMMA = 'TOKEN_COMMA';
TOKEN_STRING = 'TOKEN_STRING';
TOKEN_NUMBER = 'TOKEN_NUMBER';
TOKEN_TRUE = 'TOKEN_TRUE';
TOKEN_FALSE = 'TOKEN_FALSE';
TOKEN_NULL = 'TOKEN_NULL';


def from_json(data: str):
    def _parse_object(index: int, success: bool) -> (int, bool, object):
        obj = {}
        index, token = _next_token(index)

        done = False
        while not done:
            token = _look_ahead(index)
            if token == TOKEN_NONE:
                success = False
                return index, success, None
            elif token == TOKEN_COMMA:
                index, token = _next_token(index)
            elif token == TOKEN_CURLY_CLOSE:
                index, token = _next_token(index)
                return index, success, obj
            else:
                # name
                index, success, name = _parse_string(index, success)
                if not success:
                    return index, success, None

                # :
                index, token = _next_token(index)
                if token != TOKEN_COLON:
                    success = False
                    return index, success, None

                # value
                index, success, value = _parse_value(index, success)
                if not success:
                    return index, success, None

                obj[name] = value

        return obj, index, success

    def _eat_whitespace(index: int) -> int:
        for i in range(index, len(data)):
            if data[i] not in " \t\n\r":
                return i

    def _parse_value(index: int, success: bool) -> (int, bool, object):
        token = _look_ahead(index)
        if token == TOKEN_STRING:
            return _parse_string(index, success)
        elif token == TOKEN_NUMBER:
            return _parse_number(index, success)
        elif token == TOKEN_CURLY_OPEN:
            return _parse_object(index, success)
        elif token == TOKEN_SQUARED_OPEN:
            return _parse_array(index, success)
        elif token == TOKEN_TRUE:
            index, token = _next_token(index)
            return index, success, True
        elif token == TOKEN_FALSE:
            index, token = _next_token(index)
            return index, success, False
        elif token == TOKEN_NULL:
            index, token = _next_token(index)
            return index, success, None
        else:
            raise ValueError('No JSONObject can be decoded')

    def _parse_string(index: int, success: bool) -> (int, bool, str):
        s = ''
        index = _eat_whitespace(index)

        # "
        c = data[index]
        index += 1

        complete = False
        while not complete:
            if index == len(data):
                break

            c = data[index]
            index += 1
            if c == '"':
                complete = True
                break
            elif c == '\\':
                if index == len(data):
                    break
                if c == '"':
                    s += '"'
                elif c == '\\':
                    s += '\\'
                elif c == '/':
                    s += '/'
                elif c == 'b':
                    s += '\b'
                elif c == 'f':
                    s += '\f'
                elif c == 'n':
                    s += '\n'
                elif c == 'r':
                    s += '\r'
                elif c == 't':
                    s += '\t'
            else:
                s += c

        if not complete:
            success = False
            return index, success, None

        return index, success, s

    def _parse_array(index: int, success: bool) -> (int, bool, object):
        array = []
        index, token = _next_token(index)

        done = False
        while not done:
            token = _look_ahead(index)
            if token == TOKEN_NONE:
                success = False
                return index, success, None
            elif token == TOKEN_COMMA:
                index, token = _next_token(index)
            elif token == TOKEN_SQUARED_CLOSE:
                index, token = _next_token(index)
                break
            else:
                index, success, value = _parse_value(index, success)
                if not success:
                    return index, success, None

                array.append(value)

        return index, success, array

    def _look_ahead(index: int) -> int:
        next_index, token = _next_token(index)
        return token

    def _next_token(index: int) -> (int, int):
        index = _eat_whitespace(index)

        if index == len(data):
            return index, TOKEN_NONE

        c = data[index]

        index += 1
        if c == '{':
            return index, TOKEN_CURLY_OPEN
        elif c == '}':
            return index, TOKEN_CURLY_CLOSE
        elif c == '[':
            return index, TOKEN_SQUARED_OPEN
        elif c == ']':
            return index, TOKEN_SQUARED_CLOSE
        elif c == ',':
            return index, TOKEN_COMMA
        elif c == '"':
            return index, TOKEN_STRING
        elif c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or \
                        c == '5' or c == '6' or c == '7' or c == '8' or c == '9' or \
                        c == '-' or c == '.':
            return index, TOKEN_NUMBER
        elif c == ':':
            return index, TOKEN_COLON

        index -= 1

        remaining_length = len(data) - index

        # false
        if remaining_length >= 5 and data[index:index + 5] == 'false':
            return index + 5, TOKEN_FALSE

        # true
        if remaining_length >= 4 and data[index:index + 4] == 'true':
            return index + 4, TOKEN_TRUE

        # null
        if remaining_length >= 4 and data[index:index + 4] == 'null':
            return index + 4, TOKEN_NULL

        return index, TOKEN_NONE

    def _parse_number(index: int, success: bool) -> (int, bool, int):
        index = _eat_whitespace(index)

        last_index = _get_last_index_of_number(index)

        success, number = _num_try_parse(data[index:last_index + 1])
        return last_index + 1, success, number

    def _get_last_index_of_number(index: int) -> int:
        cur_index = index
        while cur_index < len(data):
            if data[cur_index] not in "0123456789+-.eE":
                return cur_index - 1
            cur_index += 1
        return cur_index - 1

    def _num_try_parse(value: str) -> (bool, int):
        number = None
        try:
            number = int(value)
        except ValueError:
            pass
        if number is not None:
            return True, number
        try:
            return True, float(value)
        except ValueError:
            return False, value

    return _parse_value(0, True)[2]


if __name__ == '__main__':
    test = '[1]'
    JsonSerializer.loads(test)
