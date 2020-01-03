def sort(tab):
    for i in range(len(tab)):
        j = len(tab) - 1
    while j > i:
        if tab[j] < tab[j - 1]:
            tmp = tab[j]
            tab[j] = tab[j - 1]
            tab[j - 1] = tmp
        j -= 1
    return tab


def mediana_sort(L, left, right):
    if left >= right:
        raise ValueError("Pass correct range")
    L = L[left:right+1]
    L = sort(L)
    if len(L) % 2 == 0:
        return (L[int((len(L) / 2) - 1)] + L[int((len(L) / 2))]) / 2
    return L[int(len(L) / 2)]


def main():
    print(mediana_sort([1, 2, 3, 4], 0, 3))
    print(mediana_sort([1, 2, 3], 0, 2))
    print(mediana_sort([1, 2, 3, 4, 5], 0, 4))

    print(mediana_sort([1, 2, 3, 4], 0, 1))
    print(mediana_sort([1, 2, 3], 0, 1))
    print(mediana_sort([1, 2, 3, 4, 5], 0, 2))


if __name__ == '__main__':
    main()  # uruchamia wszystkie testy
