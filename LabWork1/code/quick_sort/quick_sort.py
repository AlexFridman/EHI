from typing import Sequence


def quick_sort(array: Sequence) -> Sequence:
    """Sorts given sequence in-place
    :param array: sequence of comparable
    :type array: Sequence
    :return: sorted sequence
    :rtype: Sequence
    """
    if len(array) <= 1:
        return array
    pivot = array[0]
    return quick_sort([x for x in array if x < pivot]) + \
        [x for x in array if x == pivot] + \
        quick_sort([x for x in array if x > pivot])
