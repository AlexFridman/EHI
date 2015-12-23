import argparse
import sys

from LabWork1.code.fibonacci import fibonacci
from LabWork1.code.io import (print_word_count_result,
                              print_list_of_ints,
                              open_as_text,
                              open_as_list_of_ints)
from LabWork1.code.merge_sort import merge_sort
from LabWork1.code.quick_sort import quick_sort
from LabWork1.code.text_summarizer import summarize_text
from LabWork1.code.word_count import word_count

parser = argparse.ArgumentParser(add_help=True, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("task", type=int, help="number of task", choices=range(1, 6))
parser.add_argument("--path", type=str, help="path to input file")
parser.add_argument("--data", type=str, help="data")
parser.add_argument("--fib_count", type=int, help="count of fib nums", default=5)
parser.description = 'tasks:\n\r 1) wordcount \n\r' \
                     ' 2) sentence maker \n\r' \
                     ' 3) quick_sort \n\r' \
                     ' 4) merge_sort \n\r' \
                     ' 5) fibonacci'

try:
    args = parser.parse_args()
    task_num = args.task
    fib_count = args.fib_count
    path = args.path
    data = args.data
except Exception:
    print("Incorrect args")
    sys.exit()

try:
    if task_num == 1:
        if path:
            text = open_as_text(path)
        else:
            text = data
        word_counts = word_count(text)
        print_word_count_result(word_counts)
    elif task_num == 2:
        if path:
            text = open_as_text(path)
        else:
            text = data
        sentence = summarize_text(text)
        print(sentence)
    elif task_num == 3:
        if path:
            nums = open_as_list_of_ints(path)
        else:
            nums = [int(s_i) for s_i in data.split(' ')]
        sorted_nums = quick_sort(nums)
        print_list_of_ints(sorted_nums)
    elif task_num == 4:
        if path:
            nums = open_as_list_of_ints(path)
        else:
            nums = [int(s_i) for s_i in data.split(' ')]
        sorted_nums = merge_sort(nums)
        print_list_of_ints(sorted_nums)
    elif task_num == 5:
        gen = fibonacci()
        fib_nums = [next(gen) for _ in range(fib_count)]
        print_list_of_ints(fib_nums)
    else:
        print("Incorrect task number")
except IOError:
    print("IO error")
except Exception:
    print(sys.exc_info())
