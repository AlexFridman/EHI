__author__ = 'AlexF'

import sys
import argparse
from project.WordCount import WordCount
from project.SentenceMaker import SentenceMaker
from project.QuickSort import QuickSort
from project.MergeSort import MergeSort
from project.IO import open_as_list_of_ints, open_as_text, print_list_of_ints

parser = argparse.ArgumentParser()
parser.add_argument("--task", help="number or task (1-4)", type=int)
parser.add_argument("--path", help="path to input file", type=str)

args = None

taskNum = None
path = None

try:
    args = parser.parse_args()
    taskNum = args.task
    path = args.path
except:
    print("Incorrect args")
    sys.exit()

try:
    if taskNum == 1:
        input = open_as_text(path)
        WordCount.calculate(input)
    elif taskNum == 2:
        input = open_as_text(path)
        SentenceMaker.make_sentence(input)
    elif taskNum == 3:
        input = open_as_list_of_ints(path)
        sorted = QuickSort.sort(input)
        print_list_of_ints(sorted)
    elif taskNum == 4:
        input = open_as_list_of_ints(path)
        sorted = MergeSort.sort(input)
        print_list_of_ints(sorted)
    else:
        print("Incorrect task number")
except IOError:
    print("IO error")
except:
    print(sys.exc_info()[0])
