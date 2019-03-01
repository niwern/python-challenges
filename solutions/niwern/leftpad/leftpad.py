import math


def leftpad(value, length):
    value_length = int(math.floor(math.log(value, 10)) + 1)
    result = ''

    for i in range(length):
        if value_length > i:
            digit = int((value/math.pow(10, i)) % 10)
            result = str(digit) + result

        else:
            result = '0' + result

    return result
