from typing import Iterable


def _merge(arr_1: Iterable, arr_2: Iterable) -> Iterable:
    """Returns a sequence was merged from given ones
    :param arr_1: first sequence
    :type arr_1: Iterable
    :param arr_2: second sequence
    :type arr_2: Iterable
    :return: merged sequence
    :rtype: Iterable
    """
    p_1 = p_2 = 0
    result = []
    while p_1 < len(arr_1) and p_2 < len(arr_2):
        if arr_1[p_1] < arr_2[p_2]:
            result.append(arr_1[p_1])
            p_1 += 1
        else:
            result.append(arr_2[p_2])
            p_2 += 1

    result.extend(arr_1[p_1:])
    result.extend(arr_2[p_2:])
    return result


def merge_sort(array: Iterable) -> Iterable:
    """Sorts given sequence in-place
    :param array: sequence of comparable
    :type array: Iterable
    :return: sorted sequence
    :rtype: Iterable
    """
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return _merge(left, right)
