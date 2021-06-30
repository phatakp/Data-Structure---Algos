from random import randrange
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


def pivot_and_repeat(arr):
    if len(arr) < 2:
        return arr

    left, mid, right = [], [], []
    pivot = arr[randrange(len(arr))]

    for num in arr:
        if compare(pivot, num):
            left.append(num)
        elif num == pivot:
            mid.append(num)
        else:
            right.append(num)

    return pivot_and_repeat(left) + mid + pivot_and_repeat(right)


def quick_sort(arr):
    """ 
    Select a random number from array as pivot.
    Move all numbers smaller to pivot on the left side and larger than pivot on right side.
    Repeat the process by then recursively selecting pivot from left and right sides.
    """
    global comp, swaps

    arr = pivot_and_repeat(arr)
    print(f"{compares=}")
    print(f"{swaps=}")
    return arr
