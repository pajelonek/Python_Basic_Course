import matplotlib.pyplot as plt


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b != 0:
        y = (-c) / b
        return "Rozwiazaniem jest liczba " + str(y)
    if b == 0:
        y = (-c) / a
        return "Rozwiazaniem jest liczba " + str(y)
    return "Rozwiazaniem jest prosta spelniajaca rownanie: y = (" + str(-a) + "x" + str(-c) + ") / " + str(b)


def main():
    print("Wynik dla 10:" + str(solve1(2, 3, 4)))


if __name__ == '__main__':
    main()  # uruchamia wszystkie testy
