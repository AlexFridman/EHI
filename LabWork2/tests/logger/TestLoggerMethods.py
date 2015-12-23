__author__ = 'AlexF'

import unittest
from LabWork2.code.logger.logger import Logger


class TestLoggerMethods(unittest.TestCase):
    def test_logging(self):
        class SimpleClass(Logger):
            def test(self, x, y=5):
                return x + y

        obj = SimpleClass()
        obj.test(5)

        log = str(obj)
        self.assertEqual('test([5, {}]) = 10', log)

    def test_custom_logging_format(self):
        class SimpleClass(Logger):
            def __init__(self):
                super(SimpleClass, self).__init__(format_str=']{0}[ ]{1}[ = {2}')

            def test(self, x, y=5):
                return x + y

        obj = SimpleClass()
        obj.test(5)

        log = str(obj)
        self.assertEqual(']test[ ][5, {}][ = 10', log)


if __name__ == '__main__':
    unittest.main()
