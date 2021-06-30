from random import randint
from time import perf_counter
import sys
import os
sys.path.insert(0, os.getcwd())
ARRAY_LENGTH = 1000


if __name__ == '__main__':
    # from PS_Algos2.sorting import bubble_sort, merge_sort, selection_sort, quick_sort, insertion_sort
    from PS_Algos2.timing import run_sorting_algorithm
    array = {randint(1, ARRAY_LENGTH*10) for _ in range(ARRAY_LENGTH)}

    # algos = {'bubble_sort': bubble_sort, 'merge_sort': merge_sort,
    #          'selection_sort': selection_sort, 'insertion_sort': insertion_sort, 'quick_sort': quick_sort}

    algos = ('bubble_sort', 'merge_sort', 'selection_sort',
             'insertion_sort', 'quick_sort')

    print(f'\n Testing {ARRAY_LENGTH} records')
    # for algo_name, algo in algos.items():
    #     print(f'\n**************{algo_name.upper()}*********************')
    #     st = perf_counter()
    #     func = getattr(algo, algo_name)
    #     arr, compares, swaps = func(list(array))
    #     ed = perf_counter()
    #     print(f'Execution time={(ed-st):3f} seconds')
    #     print(f'{compares=}')
    #     print(f'{swaps=}')
    #     print()
    for algo_name in algos:
        print(f'\n**************{algo_name.upper()}*********************')
        run_sorting_algorithm(algo_name, list(array))
        print()
