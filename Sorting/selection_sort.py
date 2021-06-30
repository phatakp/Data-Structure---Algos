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


def selection_sort(arr):
    """
    Select minimum from the list and place to leftmost.
    Repeat the process for remaining sub list
    """
    global compares, swaps
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if compare(arr[min], arr[j]):
                min = j

        arr = swap(arr, i, min)

    print(f"{compares=}")
    print(f"{swaps=}")
    return arr
