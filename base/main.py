def sum_numbers(a, b):
    return a + b


def mult_numbers(a, b):
    return a * b


def list_numbers(qty):
    numbers = []
    for number in range(qty):
        numbers.append(number)
    return numbers


if __name__ == '__main__':
    print(sum_numbers(5, 7))
    print(mult_numbers(3, 9))
    print(list_numbers(8))
