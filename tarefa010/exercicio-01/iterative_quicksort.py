def _partition(arr, l, h):
    i = ( l - 1 )
    x = arr[h]
  
    for j in range(l, h):
        if   arr[j] <= x:
  
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)
  
# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def _iterative_quicksort(numbers: list[int], left, right):
    # Create an auxiliary stack
    size = right - left + 1
    stack = [0] * (size)
  
    # initialize top of stack
    top = -1
  
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = left
    top = top + 1
    stack[top] = right
  
    # Keep popping from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        right = stack[top]
        top = top - 1
        left = stack[top]
        top = top - 1
  
        # Set pivot element at its correct position in
        # sorted array
        p = _partition( numbers, left, right )
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > left:
            top = top + 1
            stack[top] = left
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < right:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = right
  

def quicksort(numbers: list[int]):
    _iterative_quicksort(numbers, 0, len(numbers) - 1)

