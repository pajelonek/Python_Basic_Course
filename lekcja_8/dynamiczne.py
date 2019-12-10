
values = {(0, 0): 0.5, (0, 1): 1.0, (1, 0): 0.0}


def P_rek(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif i == 0 and j > 0:
        return 1.0
    elif i > 0 and j == 0:
        return 0.0
    elif j > 0 and i > 0:
        return 0.5 * (P_rek(i - 1, j) + P_rek(i, j - 1))


def P_dyn(i, j):
    if (i, j) in values:
        return values[i, j]
    if i == 0 and j > 0:
        values[(i, j)] = 1.0
        return values.get((i, j))
    elif i > 0 and j == 0:
        values[(i, j)] = 0.0
        return values.get((i, j))
    else:
        values[(i, j)] = 0.5 * (P_dyn(i - 1, j) + P_dyn(i, j - 1))
        return values.get((i, j))


def main():
    print(P_rek(9, 5))
    print(P_dyn(9, 5))


if __name__ == '__main__':
    main()  # uruchamia wszystkie testy
