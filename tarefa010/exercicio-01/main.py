import sys
import random
import csv

from benchmark import make_benchmark


benchmarking_header = [
    'length',
    'ms to sort with iterative quicksort',
    'ms to sort with recursive quicksort']

benchmarking_data = []

def main():
    sys.setrecursionlimit(1_000_000)
    lists_of_numbers: list[list[int]] = []

    lists_of_numbers.append([random.randint(0, 2**32) for _ in range(100)])
    lists_of_numbers.append([random.randint(0, 2**32) for _ in range(1_000)])
    lists_of_numbers.append([random.randint(0, 2**32) for _ in range(10_000)])

    # benchmarking_data.append([100, end_1_iterative-start_1_iterative, end_1_recursive-start_1_recursive])
    benchmarking_data = make_benchmark(lists_of_numbers)

    with open('./benchmark_results.csv', 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(benchmarking_header)

        writer.writerows(benchmarking_data)


if __name__ == '__main__':
    main()
