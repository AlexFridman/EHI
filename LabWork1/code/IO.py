from collections import Counter
import sys

__author__ = 'AlexF'


def open_as_list_of_ints(path: str):
    try:
        with open(path, "r+") as f:
            str_input = f.readline()
        ints = [int(item) for item in str_input.split(' ')]
    except:
        raise IOError

    return ints


def open_as_text(path: str):
    try:
        with open(path, "r+",encoding='utf8') as f:
            return f.read()
    except:
        raise IOError


def print_list_of_ints(items: list):
    output = str.join(' ', [str(i) for i in items])
    print(output)


def print_word_count_result(counts: Counter):
    print("stat:")
    for w, c in counts.items():
        print("{0}\t{1}".format(w, c))
