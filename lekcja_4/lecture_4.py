def task_3_5(length):
    measure = "|"
    for i in range(1, length + 1):
        measure += "....|"

    measure += "\r\n0"

    for i in range(1, length + 1):
        digits = len(str(i))
        measure += ((5 - digits) * ".")
        measure += str(i)

    return measure


def task_3_6(x, y):
    template = "+"
    for i in range(0, x):
        template += "---+"

    template += "\r\n|"
    for i in range(0, x):
        template += "   |"
    draw = ""
    for i in range(0, y):
        draw += template + "\r\n"
    draw += "+"
    for i in range(0, x):
        draw += "---+"

    return draw


def task_4_2(length, x, y):
    print("4.2:")
    print(task_3_5(length))
    print(task_3_6(x, y))


def factorial(n):
    if n < 0:
        raise NameError('Invalid argument')
    factorial = n
    for i in range(n - 1, 1, - 1):
        factorial *= i
    return factorial


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


def odwracanie(L, l, r):
    if l < 0 or r > len(L):
        raise NameError('Invalid argument')
    for i in range(l, int((l + r) / 2)):
        L[i], L[len(L) - i] = L[len(L) - i], L[i]
    print(str(L))


def sum_seq(seq):
    suma = 0
    if isinstance(seq, (list, tuple)):
        for i in seq:
            suma += sum_seq(i)
    else:
        suma += seq
    return suma


def flatten(sequence):
    L = []
    if isinstance(sequence, (list, tuple)):
        for i in sequence:
            for el in flatten(i):
                L.append(el)
    else:
        L.append(sequence)
    return L


def main():
    task_4_2(12, 4, 2)
    print("4.3: " + str(factorial(5)))
    print("4.4: " + str(fibonacci(6)))
    odwracanie([1, 2, 3, 4, 5], 1, 5)
    print(sum_seq([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]))
    print(flatten([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]))


if __name__ == "__main__":
    main()
