"""Old way of doing a factorial"""


def get_factorial(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
    return factorial


print(get_factorial(10))
