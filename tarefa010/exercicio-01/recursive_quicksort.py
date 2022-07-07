from typing import List, Union

def _partition(numbers: List[Union[int, float]], left: int, right: int) -> int:
    pivot = numbers[right]

    i = left - 1

    for j in range(left, right):
        if numbers[j] <= pivot:
            i += 1
            # Swap numbers at i and numbers at j.
            (numbers[i], numbers[j]) = (numbers[j], numbers[i])


    (numbers[i + 1], numbers[right]) = (numbers[right], numbers[i + 1])

    return i + 1


def _recursive_quicksort(numbers: List[Union[int, float]], left: int, right: int):
    if left >= right:
        return
    
    pivot_position = _partition(numbers, left, right)

    # Recursive quicksort call on the left of pivot.
    _recursive_quicksort(numbers, left, pivot_position - 1)

    # Recursive quicksort call on the right of pivot.
    _recursive_quicksort(numbers, pivot_position + 1, right)


def quicksort(numbers: List[Union[int, float]]):
    _recursive_quicksort(numbers, 0, len(numbers) - 1)
