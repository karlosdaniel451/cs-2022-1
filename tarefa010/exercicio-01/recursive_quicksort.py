def partition(numbers: list[int], left: int, right: int) -> int:
    pivot = numbers[left]
    low = left + 1
    high = right

    while True:
        while low <= high and numbers[high] >= pivot:
            high -= 1

        while low <= high and numbers[low] <= pivot:
            low += 1

        if low <= high:
            (numbers[low], numbers[high]) = (numbers[high], numbers[low])
        else:
            break

    numbers[left], numbers[high] = numbers[high], numbers[left]

    return high


def _recursive_quicksort(numbers: list[int], left: int, right: int):
    if left >= right:
        return

    pivot_position = partition(numbers, left, right)

    _recursive_quicksort(numbers, left, pivot_position-1)

    _recursive_quicksort(numbers, pivot_position+1, right)


def quicksort(numbers: list[int]):
    _recursive_quicksort(numbers, 0, len(numbers) - 1)

