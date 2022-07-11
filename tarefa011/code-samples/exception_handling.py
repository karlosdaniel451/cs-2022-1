dividend: int
divider : int
quotient: float


while True:
    try:
        dividend = int(input('Enter the dividend: '))
    except ValueError:
        print('Error: dividend must be an integer number. Please try it again.')
    else:
        break

while True:
    try:
        divider = int(input('Enter the divisor: '))
        quotient = dividend / divider
    except ValueError:
        print('Error: divider must be an integer number. Please try it again.')
    except ZeroDivisionError:
        print('Error: divider must be an integer number different than 0. Please try it again.')
    else:
        break

print(quotient)

