def factorial(n):
    if n < 0:
        raise NameError('Invalid argument')
    factorial_v = n
    for i in range(n - 1, 1, - 1):
        factorial_v *= i
    return factorial_v


def fibonacci(n):
    if n < 0:
        raise NameError('Invalid argument')
    if n == 0:
        return 0
    first = 0
    second = 1
    next_n = 1

    for i in range(2, n):
        first = second
        second = next_n
        next_n = first + second
    return next_n
