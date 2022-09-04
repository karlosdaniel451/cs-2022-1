import time

import iterative_quicksort
import recursive_quicksort


def make_benchmark(lists_of_numbers: list[list[int]]) -> list:
    benchmark_results = []

    for numbers in lists_of_numbers:
        numbers_copy = numbers

        start_iterative_quicksort = time.perf_counter()
        iterative_quicksort.quicksort(numbers)
        end_iterative_quicksort = time.perf_counter()

        start_recursive_quicksort = time.perf_counter()
        recursive_quicksort.quicksort(numbers_copy)
        end_recursive_quicksort = time.perf_counter()

        diff_iterative_quicksort = end_iterative_quicksort - start_iterative_quicksort
        diff_recursive_quicksort = end_recursive_quicksort - start_recursive_quicksort

        benchmark_results.append(
            [len(numbers), round(diff_iterative_quicksort * 1000, 3), round(diff_recursive_quicksort * 1000, 3)]
        )

    return benchmark_results

# benchmarking_data.append([100, end_1_iterative-start_1_iterative, end_1_recursive-start_1_recursive])
