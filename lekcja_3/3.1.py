def main():
    # Case a):
    x = 2;
    y = 3;
    if (x > y):
        result = x;
    else:
        result = y;
    print(result)

    # poprawna wersja wg mnie

    x = 2
    y = 3
    if x > y:
        result = x
    else:
        result = y
    print(result)

    # Tak, sredniki sa warningami, mozna je stosowac, chociaz raczej nie powinno

    # Case b)
    #   for i in "qwerty": if ord(i) < 100: print i

    # Nie, for + instrukcje warunkowe musza znajdowac sie w innych rzedach po 4 spacjach/tabulatorach - nie mozna tego pisac w 1 linijce
    # poprawna wersja:
    for i in "qwerty":
        if ord(i) > 100:
            print(i)

    # Case c)
    for i in "axby": print(ord(i)) if ord(i) < 100 else i

    # Mimo ze produkuje warning powyzszna konstrukcja jest poprawna, przez to ze najpierw wystepuje print mozemy umiescic instrukcje i jej warunek w tym samym rzedzie


if __name__ == "__main__":
    main()
