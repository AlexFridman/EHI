__author__ = 'AlexF'

import os
import tempfile

import numpy as np


class ExternalMemoryMergeSort:
    def sort(self, path, result_path, verbose=False):
        if not self._is_file_exists(path):
            raise FileNotFoundError('file {} not exists'.format(path))
        self._input_path = path
        self._data_size = self._define_data_size(path)
        self._max_chunk_size = self._define_max_chunk_size()
        self._verbose = verbose
        temp_res = self._sort_data(0, self._data_size)
        self._copy_from_temp(temp_res, result_path)

    def _is_file_exists(self, path):
        return os.path.exists(path)

    def _define_data_size(self, path):
        with open(path, 'r') as fp:
            return sum(1 for line in fp)

    def _define_max_chunk_size(self):
        return 10 ** 5

    def _sort_data(self, l_bound, r_bound, indent=1):
        if r_bound - l_bound <= self._max_chunk_size:
            sorted_data = self._sort_in_memory(l_bound, r_bound)
            return self._save_to_temp_file(sorted_data)
        else:
            mid = l_bound + (r_bound - l_bound) // 2
            if self._verbose:
                print('{}[{}, {}]'.format('-' * indent, l_bound, mid))
                print('{}[{}, {}]'.format('-' * indent, mid, r_bound))
            temp_file_l = self._sort_data(l_bound, mid, indent + 1)
            temp_file_r = self._sort_data(mid + 1, r_bound, indent + 1)
            if self._verbose:
                print('{} [{}, {}]'.format('+' * indent, l_bound, r_bound))
            return self._merge(temp_file_l, temp_file_r)

    def _sort_in_memory(self, l_bound, r_bound):
        data = self._read_chunk_from_init_file(l_bound, r_bound)
        nd_array = np.array(data)
        nd_array.sort()
        return nd_array.astype(int)

    def _read_chunk_from_init_file(self, chunk_start, chunk_end):
        chunk = []
        if chunk_end >= self._data_size:
            chunk_end = self._data_size - 1
        with open(self._input_path, 'r') as fp:
            for l_number in range(chunk_start):
                next(fp)

            for l_number in range(chunk_end - chunk_start + 1):
                line = fp.readline()
                number = int(line)
                chunk.append(number)

            return chunk

    def _save_to_temp_file(self, data):
        temp_file = tempfile.TemporaryFile()
        for item in data:
            temp_file.write(bytes(str(item) + '\n', 'utf-8'))
        temp_file.seek(0)
        return temp_file

    def _merge(self, temp_file_1, temp_file_2):
        temp_file = tempfile.TemporaryFile()

        success_1, num_1 = self._try_read_next_item_from_temp_file(temp_file_1)
        success_2, num_2 = self._try_read_next_item_from_temp_file(temp_file_2)

        alive_markers = [success_1, success_2]
        while all(alive_markers):
            if num_1 <= num_2:
                temp_file.write(bytes(str(num_1) + '\n', 'utf-8'))
                alive_markers[0], num_1 = self._try_read_next_item_from_temp_file(temp_file_1)
            else:
                temp_file.write(bytes(str(num_2) + '\n', 'utf-8'))
                alive_markers[1], num_2 = self._try_read_next_item_from_temp_file(temp_file_2)

        if not any(alive_markers):
            temp_file.seek(0)
            return temp_file

        if alive_markers[0]:
            alived = temp_file_1
            temp_file.write(bytes(str(num_1) + '\n', 'utf-8'))
        else:
            alived = temp_file_2
            temp_file.write(bytes(str(num_2) + '\n', 'utf-8'))

        still_alive = True

        while still_alive:
            still_alive, num = self._try_read_next_item_from_temp_file(alived)
            if still_alive:
                temp_file.write(bytes(str(num) + '\n', 'utf-8'))

        temp_file.seek(0)
        return temp_file

    def _try_read_next_item_from_temp_file(self, temp_file):
        number = None
        try:
            line_of_bytes = temp_file.readline()
            int_str = line_of_bytes.decode('utf-8')
            number = int(int_str)
        except:
            return False, 0

        return True, number

    def _copy_from_temp(self, temp_file, output_path):
        with open(output_path, 'w+') as fp:
            for line in temp_file:
                int_str = line.decode('utf-8')
                if int_str == '':
                    break
                number = int(int_str)
                fp.write(str(number) + '\n')


if __name__ == '__main__':
    ExternalMemoryMergeSort().sort('D:/sort/input.txt', 'D:/sort/output.txt', verbose=True)
