__author__ = 'AlexF'

import functools


class Logger:
    def __init__(self, verbose=False, format_str='{0}({1}) = {2}'):
        self._logs = []
        self._verbose = verbose
        self._format_str = format_str

    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if name not in ['_log', '__str__'] and hasattr(attr, '__call__'):

            @functools.wraps(attr)
            def wrapper(*args, **kwargs):
                result = attr(*args, **kwargs)
                self._log(name, list(args) + [kwargs], result)
                return result

            return wrapper
        else:
            return attr

    def _log(self, attr_name, args, result):
        log_message = self._format_str.format(attr_name, args, result)
        self._logs.append(log_message)
        if self._verbose:
            print(log_message)

    def __str__(self):
        pass
        return ' '.join(self._logs)
