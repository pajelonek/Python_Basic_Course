data = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 14, 15]


def binarne_rek(l, p, target):
    if l > p:
        return -1
    sr = int((l + p) / 2)
    if target == data[sr]:
        return sr
    if target < data[sr]:
        return binarne_rek(l, sr - 1, target)
    return binarne_rek(sr + 1, p, target)


def main():
    assert binarne_rek(0, len(data) - 1, 9) == 10


if __name__ == '__main__':
    main()  # uruchamia wszystkie testy
