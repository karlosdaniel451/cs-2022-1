import random
import time
import csv

import recursive_quicksort
import iterative_quicksort

benchmarking_header = [
    'length',
    ' ms to sort with iterative_quicksort',
    ' ms to sort with iterative_quicksort']

benchmarking_data = []

def main():
    numbers_1 = [random.randint(0, 100_000) for _ in range(100)]
    numbers_2 = [random.randint(0, 100_000) for _ in range(1_000)]
    numbers_3 = [random.randint(0, 100_000) for _ in range(10_000)]

    numbers_1_copy = numbers_1[:]
    numbers_2_copy = numbers_2[:]
    numbers_3_copy = numbers_3[:]

    start_1_recursive = time.perf_counter()
    recursive_quicksort.quicksort(numbers_1)
    end_1_recursive = time.perf_counter()

    start_2_recursive = time.perf_counter()
    recursive_quicksort.quicksort(numbers_2)
    end_2_recursive = time.perf_counter()

    start_3_recursive = time.perf_counter()
    recursive_quicksort.quicksort(numbers_3)
    end_3_recursive = time.perf_counter()

    start_1_iterative = time.perf_counter()
    iterative_quicksort.quicksort(numbers_1_copy)
    end_1_iterative = time.perf_counter()

    start_2_iterative = time.perf_counter()
    iterative_quicksort.quicksort(numbers_2_copy)
    end_2_iterative = time.perf_counter()

    start_3_iterative = time.perf_counter()
    iterative_quicksort.quicksort(numbers_3_copy)
    end_3_iterative = time.perf_counter()

    # Append benchnmarking data of iterative quicksort.
    benchmarking_data.append((100, 'iterative quicksort', round(end_1_iterative-start_1_iterative, 6)))
    benchmarking_data.append((1_000, 'iterative quicksort', round(end_2_iterative-start_2_iterative, 6)))
    benchmarking_data.append((10_000, 'iterative quicksort', round(end_3_iterative-start_3_iterative, 6)))

    # Append benchnmarking data of recursive quicksort.
    benchmarking_data.append((100, 'recursive quicksort', round(end_1_recursive-start_1_recursive, 6)))
    benchmarking_data.append((1_000, 'recursive quicksort', round(end_2_recursive-start_2_recursive, 6)))
    benchmarking_data.append((10_000, 'recursive quicksort', round(end_3_recursive-start_3_recursive, 6)))

    with open('./benchmarks.csv', 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(benchmarking_header)

        writer.writerows(benchmarking_data)


if __name__ == '__main__':
    main()
