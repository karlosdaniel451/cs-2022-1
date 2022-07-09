# from collections import deque

# def _partition(numbers: list[int], start, end):
 
#     # Escolha o elemento mais à direita como pivô da lista
#     pivot = numbers[end]
 
#     # Elementos # menores que o pivô irão para a esquerda de `pIndex`
#     # Elementos # mais do que o pivô irão para a direita de `pIndex`
#     # Elementos iguais # podem ir de qualquer maneira
#     pivot_position = start
 
#     # cada vez que encontramos um elemento menor ou igual ao pivô,
#     # `pIndex` é incrementado, e esse elemento seria colocado
#     # antes do pivô.
#     for i in range(start, end):
#         if numbers[i] <= pivot:
#             # swap(a, i, pIndex)
#             (i, pivot_position) = (pivot_position, i)
#             pivot_position += 1
 
#     # swap(a, pIndex, end)
#     (pivot_position, end) = (end, pivot_position)
 
#     # retorna `pIndex` (índice do elemento pivô)
#     return pivot_position
 
 
# def _iterative_quicksort(numbers: list[int]):
 
#     # cria uma Stack para armazenar o índice inicial e final da sublista
#     stack: deque[tuple[int, int]] = deque()
 
#     # obtém o índice inicial e final de uma determinada lista
#     start = 0
#     end = len(numbers) - 1
 
#     # empurra o índice inicial e final do array para a Stack
#     stack.append((start, end))
 
#     # loop até que a Stack esteja vazia
#     while stack:
 
#         # remove o par superior da lista e inicia a sublista
#         # e índices finais
#         start, end = stack.pop()
 
#         # reorganiza os elementos no pivô
#         pivot = _partition(numbers, start, end)
 
#         # Índices de sublista push # contendo elementos que são
#         # menor que o pivô atual para stack
#         if pivot - 1 > start:
#             stack.append((start, pivot - 1))
 
#         # Índices de sublista push # contendo elementos que são
#         # mais do que o pivô atual para stack
#         if pivot + 1 < end:
#             stack.append((pivot + 1, end))


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
