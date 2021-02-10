'''
nums = [23, 29, 1, 11, 89, 56, 4]
[23, 29, 1]             [11, 89, 56, 4]
[23]  [29, 1]           [11, 89]    [56, 4]
[23] [29] [1]           [11] [89]   [56] [4] 
[23] [1, 29]            [11, 89]    [4, 56]
[1, 23, 29]             [4, 11, 56, 89]
[1, 4, 11, 23, 29, 56, 89]
'''
from random import randint
from timing import run_sorting_algorithm

ARRAY_LENGTH = 1000


def merge(left, right):
    result = []
    l = r = 0

    while len(result) < len(left) + len(right):
        if l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        elif l >= len(left):
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1

    return result


def merge_sort(arr):

    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    return merge(left=merge_sort(arr[:mid]),
                 right=merge_sort(arr[mid:]))


if __name__ == '__main__':
    # Generate Array of random integers
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="merge_sort", array=array)
