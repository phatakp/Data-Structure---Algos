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


def merge(left, right):
    global compares, swaps
    result = []
    l_id = r_id = 0
    while len(result) < len(left) + len(right):
        if l_id < len(left) and r_id < len(right):
            if compare(left[l_id], right[r_id]):
                result.append(right[r_id])
                r_id += 1
            else:
                result.append(left[l_id])
                l_id += 1
        elif l_id < len(left):
            result.append(left[l_id])
            l_id += 1
        elif r_id < len(right):
            result.append(right[r_id])
            r_id += 1
    return result


def split_array(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    return merge(left=split_array(arr[:mid]),
                 right=split_array(arr[mid:]))


def merge_sort(arr):
    """
    Recursively split arrays until no further possible.
    Merge splits in sorted order until all merged
    """
    global compares, swaps
    arr = split_array(arr)
    print(f"{compares=}")
    print(f"{swaps=}")
    return arr
