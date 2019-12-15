import matplotlib.pyplot as plt


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0 and c == 0:
        return "Rozwiazaniem jest zbior liczb rzeczywistych"
    elif a == 0 and b == 0 and c != 0:
        return "Brak rozwiazan"
    elif a == 0 and b != 0 and c == 0:
        return "Rozwiazaniem jest prosta y = 0"
    elif a == 0 and b != 0 and c != 0:
        return "Rozwiazaniem jest prosta y = " + str((-c) / b)
    elif a != 0 and b == 0 and c == 0:
        return "Rozwiazaniem jest prosta x = 0"
    elif a != 0 and b == 0 and c != 0:
        return "Rozwiazaniem jest prosta x = " + str((-c) / a)
    elif a != 0 and b != 0 and c == 0:
        return "Rozwiazaniem jest prosta y = " + str(-a)+"x /"+str(b)

    return "Rozwiazaniem jest prosta spelniajaca rownanie: y = (" + str(-a) + "x" + str(-c) + ") / " + str(b)


def main():
    print(solve1(2, 0, 4))


if __name__ == '__main__':
    main()  # uruchamia wszystkie testy
