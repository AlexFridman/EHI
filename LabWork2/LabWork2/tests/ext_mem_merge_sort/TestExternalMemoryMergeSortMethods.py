__author__ = 'AlexF'

import unittest
import random

from LabWork2.code.ext_mem_merge_sort.ext_mem_merge_sort import ExternalMemoryMergeSort
from LabWork2.code.ext_mem_merge_sort.invalid_data_error import InvalidDataError


class TestExternalMemoryMergeSortMethods(unittest.TestCase):
    def test_sorting(self):
        input_file = 'input.txt'
        output_file = 'output.txt'
        TOTAL_COUNT = 100000

        with open(input_file, 'w') as fp:
            fp.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(TOTAL_COUNT))

        ExternalMemoryMergeSort().sort(input_file, output_file)
        count = 0
        num = 0
        with open(output_file) as fp:
            for line in fp:
                next_num = int(line)
                if count > 0:
                    self.assertTrue(next_num >= num)
                count += 1
                num = next_num
        self.assertEquals(count, TOTAL_COUNT)

    def test_no_input_file(self):
        input_file = 'Q:\\no_such_file.txt'
        output_file = 'output.txt'

        invoke = lambda: ExternalMemoryMergeSort().sort(input_file, output_file)
        self.assertRaises(FileNotFoundError, invoke)


def test_invalid_data(self):
    input_file = 'input.txt'
    output_file = 'output.txt'

    with open(input_file, 'w') as fp:
        fp.writeline('some invalid data')

    self.assertRaises(InvalidDataError, lambda: ExternalMemoryMergeSort().sort(input_file, output_file))


if __name__ == '__main__':
    unittest.main()
