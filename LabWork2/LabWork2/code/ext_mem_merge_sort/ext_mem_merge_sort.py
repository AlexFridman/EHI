__author__ = 'AlexF'

import os
import math
import tempfile
from heapq import heappush, heappop, heapify
from LabWork2.code.ext_mem_merge_sort.invalid_chunk_borders_error import InvalidChunkBordersError
from LabWork2.code.ext_mem_merge_sort.invalid_data_error import InvalidDataError
from LabWork2.code.ext_mem_merge_sort.cannot_create_temp_file_error import CannotCreateTempFileError


class ExternalMemoryMergeSort:
    def sort(self, path, result_path):
        if not self._is_file_exists(path):
            raise FileNotFoundError('file {} not exists'.format(path))
        self._data_size = self._define_data_size(path)
        self._chunk_count, self._chunk_shifts = self._define_chunk_count_and_shifts(self._data_size)
        self._temp_files = {}
        for chunk_i in range(self._chunk_count):
            print('#{}'.format(chunk_i))
            self._sort_chunk(path, chunk_i)

        self.merge(result_path)

    def _is_file_exists(self, path):
        return os.path.exists(path)

    def _define_data_size(self, path):
        with open(path, 'r') as fp:
            return sum(1 for line in fp)

    def _define_chunk_count_and_shifts(self, data_size):
        chunk_size = self._define_max_chunk_size()
        chunk_count = math.ceil(data_size / chunk_size)
        chunk_shifts = dict([(chunk_n, chunk_n * chunk_size)
                             for chunk_n in range(chunk_count)])
        return chunk_count, chunk_shifts

    def _define_max_chunk_size(self):
        return 10000

    def _sort_chunk(self, path, chunk_n):
        data = self._read_chunk_from_init_file(path, chunk_n)
        sorted_data = self._merge_sort(data)
        temp_file = self._create_temp_file()
        if not temp_file:
            raise CannotCreateTempFile()
        self._temp_files[chunk_n] = temp_file
        self._write_chunk_to_temp_file(self._temp_files[chunk_n], sorted_data)

    def _read_chunk_from_init_file(self, path, chunk_n):
        chunk_start, chunk_end = self._define_chunk_borders(chunk_n)
        chunk = []
        with open(path, 'r') as fp:
            try:
                for l_number in range(chunk_start):
                    next(fp)
            except StopIteration:
                raise InvalidChunkBorders()

            for l_number in range(chunk_end - chunk_start):
                try:
                    line = fp.readline()
                    number = int(line)
                    chunk.append(number)
                except ValueError:
                    raise InvalidData()

            return chunk

    def _define_chunk_borders(self, chunk_n):
        lower_bound = self._chunk_shifts[chunk_n]
        upper_bound = self._chunk_shifts.get(chunk_n + 1, self._data_size)
        return lower_bound, upper_bound

    def _merge_sort(self, xs):
        unit = 1
        while unit <= len(xs):
            h = 0
            for h in range(0, len(xs), unit * 2):
                l, r = h, min(len(xs), h + 2 * unit)
                mid = h + unit
                # merge xs[h:h + 2 * unit]
                p, q = l, mid
                while p < mid and q < r:
                    if xs[p] < xs[q]:
                        p += 1
                    else:
                        tmp = xs[q]
                        xs[p + 1: q + 1] = xs[p:q]
                        xs[p] = tmp
                        p, mid, q = p + 1, mid + 1, q + 1

            unit *= 2

        return xs

    def _create_temp_file(self):
        return tempfile.TemporaryFile()

    def _write_chunk_to_temp_file(self, temp_file, data):
        for item in data:
            temp_file.write(bytes(str(item) + '\n', 'utf-8'))
        temp_file.seek(0)

    def merge(self, result_path):
        heap = [(self._try_read_next_item_from_temp_file(chunk_n)[1], chunk_n)
                for chunk_n in range(self._chunk_count)]

        heapify(heap)
        i = 0
        with open(result_path, 'w+') as fp:
            while any(self._temp_files.values()):
                min_item, chunk_n = heappop(heap)
                fp.write(str(min_item) + '\n')
                success, next_item = self._try_read_next_item_from_temp_file(chunk_n)
                if not success:
                    self._temp_files[chunk_n].close()
                    del self._temp_files[chunk_n]
                    self._chunk_count -= 1
                else:
                    heappush(heap, (next_item, chunk_n))

    def _try_read_next_item_from_temp_file(self, chunk_n):
        file = self._temp_files[chunk_n]
        number = None
        try:
            line_of_bytes = file.readline()
            int_str = line_of_bytes.decode('utf-8')
            number = int(int_str)
        except:
            return False, 0

        return True, number


if __name__ == '__main__':
    ExternalMemoryMergeSort().sort('D:/sort/input.txt', 'D:/sort/output.txt')
