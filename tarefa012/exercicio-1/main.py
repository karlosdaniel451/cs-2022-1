def main():
    dividend: float
    divider: float
    quotient: float

    while True:
        try:
            dividend = float(input('Dividend: '))
            divider = float(input('Divider: '))
            quotient = dividend / divider
        except ValueError:
            print('Error: input should be numeric. Please try it again.\n')
        except ZeroDivisionError:
            print('Error: divider should be non-null. Please try it again.\n')
        else:
            print(quotient)
            break


if __name__ == '__main__':
    main()
