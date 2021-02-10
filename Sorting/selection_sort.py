from random import randint
from timing import run_sorting_algorithm

ARRAY_LENGTH = 1000


def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[min], arr[i] = arr[i], arr[min]

    return arr


if __name__ == '__main__':
    # Generate Array of random integers
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="selection_sort", array=array)
