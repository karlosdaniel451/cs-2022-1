from stack import Stack


def main():
    stack = Stack[int]()

    for i in range(0, 10):
        stack.push(i)

    while not stack.is_empty():
        print(stack.pop())


if __name__ == '__main__':
    main()
