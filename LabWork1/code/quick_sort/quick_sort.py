from typing import Iterable


def quick_sort(array: Iterable) -> Iterable:
    """Sorts given sequence in-place
    :param array: sequence of comparable
    :type array: Iterable
    :return: sorted sequence
    :rtype: Iterable
    """
    if len(array) <= 1:
        return array
    pivot = array[0]
    return quick_sort([x for x in array if x < pivot]) + \
        [x for x in array if x == pivot] + \
        quick_sort([x for x in array if x > pivot])
