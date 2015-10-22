__author__ = 'AlexF'


class MergeSort(object):
    @staticmethod
    def sort(items: list):
        result = MergeSort.merge_sort(items)
        return result

    @staticmethod
    def merge_sort(m):
        if len(m) <= 1:
            return m

        middle = len(m) // 2
        left = m[:middle]
        right = m[middle:]

        left = MergeSort.merge_sort(left)
        right = MergeSort.merge_sort(right)
        return list(MergeSort.merge(left, right))

    @staticmethod
    def merge(left, right):
        result = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            # change the direction of this comparison to change the direction of the sort
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1

        if left:
            result.extend(left[left_idx:])
        if right:
            result.extend(right[right_idx:])
        return result
