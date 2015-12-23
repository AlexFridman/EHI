__author__ = 'AlexF'

import argparse
from project.WordCount import WordCount
from project.SentenceMaker import SentenceMaker
from project.QuickSort import QuickSort
from project.MergeSort import MergeSort
from project.Fibonacci import fib_gen
from project.IO import *

parser = argparse.ArgumentParser(add_help=True, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("task", type=int, help="number of task", choices=range(1, 6))
parser.add_argument("--path", type=str, help="path to input file")
parser.add_argument("--data", type=str, help="data")
parser.add_argument("--fib_count", type=int, help="count of fib nums", default=5)
parser.description = 'tasks:\n\r 1) wordcount \n\r' \
                     ' 2) sentence maker \n\r' \
                     ' 3) quicksort \n\r' \
                     ' 4) mergesort \n\r' \
                     ' 5) fibonacci'

task_num = None
fib_count = None
path = None
data = None

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
        word_counts = WordCount.proceed_text(text)
        print_word_count_result(word_counts)
    elif task_num == 2:
        if path:
            text = open_as_text(path)
        else:
            text = data
        sentence = SentenceMaker.make_sentence(text)
        print(sentence)
    elif task_num == 3:
        if path:
            nums = open_as_list_of_ints(path)
        else:
            nums = [int(s_i) for s_i in data.split(' ')]
        sorted_nums = QuickSort.sort(nums)
        print_list_of_ints(sorted_nums)
    elif task_num == 4:
        if path:
            nums = open_as_list_of_ints(path)
        else:
            nums = [int(s_i) for s_i in data.split(' ')]
        sorted_nums = MergeSort.sort(nums)
        print_list_of_ints(sorted_nums)
    elif task_num == 5:
        gen = fib_gen()
        fib_nums = [next(gen) for _ in range(fib_count)]
        print_list_of_ints(fib_nums)
    else:
        print("Incorrect task number")
except IOError:
    print("IO error")
except:
    print(sys.exc_info())
