from random import randint
from .timing import run_sorting_algorithm

ARRAY_LENGTH = 1000


def bubble_sort(arr):

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    end = len(arr)
    swapped = True
    while swapped:
        swapped = False
        end -= 1
        for i in range(end):
            if arr[i] > arr[i+1]:
                swap(i, i+1)
                swapped = True

    return arr


if __name__ == '__main__':
    # Generate Array of random integers
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="bubble_sort", array=array)
