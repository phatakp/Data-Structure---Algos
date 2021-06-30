# from ..run_parallel_algos import swap, compare

compares = swaps = 0


def compare(i, j):
    global compares
    compares += 1
    return i > j


def swap(arr, i, j):
    global swaps
    arr[i], arr[j] = arr[j], arr[i]
    swaps += 1
    return arr


def bubble_sort(arr):
    """
    Swap two adjacent numbers if left > right.
    Each pass will result in largest number in the end.
    Repeat until no swaps are required
    """
    global compares, swaps
    end = len(arr)
    swapped = True
    while swapped:
        swapped = False
        end -= 1
        for i in range(end):
            j = i + 1
            if compare(arr[i], arr[j]):
                arr = swap(arr, i, j)
                swapped = True

    print(f"{compares=}")
    print(f"{swaps=}")
    return arr
