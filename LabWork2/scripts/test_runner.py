__author__ = 'AlexF'

import unittest
import sys
from time import sleep

from LabWork2.tests import *

tests_dict = {
    '1': (TestExternalMemoryMergeSortMethods,),
    '2': (TestJsonSerializerDumpsMethod, TestJsonSerializerLoadsMethod),
    '3': (TestVectorInit, TestVectorMathMethods),
    '4': (TestLinearFunctionMethods,),
    '5': (TestLoggerMethods,),
    '6': (TestRecursiveDefaultdictMethods,),
    '7': (TestAttrLoaderMetaBehavior,),
    '8': (TestCachedBehavior,),
    '9': (TestXrangeMethods,),
    '10': (TestFilterableListMethods,),
    '11': (TestSingletonBehavior,),
    '12': (TestModelCreatorMetaMethods,),
}

lines = []
for i, tests in sorted(tests_dict.items(), key=lambda kvp: int(kvp[0])):
    test_names = [test.__name__ for test in tests]
    line_i = '{}. {}'.format(i, ', '.join(test_names))
    lines.append(line_i)

greeting = '\n'.join(lines)

if __name__ == '__main__':
    while True:
        sleep(.01)
        print(greeting)
        user_input = input('Test suite: ')
        if user_input == 'exit':
            sys.exit(0)

        if user_input in tests_dict:
            tests = tests_dict[user_input]
            for test in tests:
                suite = unittest.defaultTestLoader.loadTestsFromTestCase(test)
                unittest.TextTestRunner().run(suite)
        else:
            print('You should write a number of a task!')
