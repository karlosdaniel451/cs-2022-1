def main():
    integers: list[int] = [None] * 10
    counter = 0

    while True:
            try:
                new_integer = int(input(f'New value for index {counter}: '))
                if new_integer == 0:
                    break 
                integers[counter] = new_integer
                counter += 1
            except ValueError:
                print('Error: input should be an integer value.\n')
            except IndexError:
                print('Error: you should enter only 10 integers.\n')
                break

    print(integers)


if __name__ == '__main__':
    main()
