from random import randint
from timing import run_sorting_algorithm

ARRAY_LENGTH = 1000


def insertion_sort(arr):

    end = len(arr)

    for i in range(1, end):
        j = i-1
        curr_num = arr[i]
        while j >= 0 and arr[j] > curr_num:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr_num

    return arr


if __name__ == '__main__':
    # Generate Array of random integers
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="insertion_sort", array=array)
