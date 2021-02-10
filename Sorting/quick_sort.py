'''
nums = [23, 29, 1, 11, 89, 56, 4]
       [1, 4] [11] [23, 29, 89, 56]
       [1] [4] [11] [23, 29, 56] [89]
       [1] [4] [11] [23] [29] [56] [89]
       [1,4] [11] [23,29,56] [89]
       [1,4,11] [23,29,56,89]
       [1,4,11,23,29,56,89]
'''
from random import randint
from timing import run_sorting_algorithm

ARRAY_LENGTH = 1000


def quick_sort(arr):

    if len(arr) < 2:
        return arr

    left, mid, right = [], [], []
    pivot = arr[len(arr) // 2]

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            mid.append(num)
        else:
            right.append(num)

    return quick_sort(left) + mid + quick_sort(right)


if __name__ == '__main__':
    # Generate Array of random integers
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="quick_sort", array=array)
