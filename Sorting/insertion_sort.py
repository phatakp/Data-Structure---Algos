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


def insertion_sort(arr):
    """
    shift the number to as left as you can such that 
    it will be larger or equal to all numbers in its left.
    Requires only one pass for sorting 
    """
    global compares, swaps
    end = len(arr)

    for i in range(1, end):
        j = i-1
        while j >= 0 and compare(arr[j], arr[i]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = arr[i]
        swaps += 1

    print(f"{compares=}")
    print(f"{swaps=}")
    return arr
