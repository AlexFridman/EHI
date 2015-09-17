__author__ = 'AlexF'


class QuickSort(object):
    @staticmethod
    def sort(items: list):
        result = QuickSort.qsort(items)
        return result

    @staticmethod
    def qsort(items: list):
        if len(items) <= 1: return items
        return QuickSort.qsort([lt for lt in items[1:] if lt < items[0]]) + items[0:1] + \
                QuickSort.qsort([ge for ge in items[1:] if ge >= items[0]])

if __name__ == "__main__":
    input = [2,1,55,1,2,666,3,1]
    sorted = QuickSort.sort(input)