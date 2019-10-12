def main():
    L = [3, 5, 4]; L = L.sort()  # <---  L = none bo L.sort() nic nie zwraca!!
    # x, y = 1, 2, 3 # <--- liczba inicjacji nie jest rowna liczbie deklaracji
    X = 1, 2, 3;  # X[1] = 4 # <---- to krotka, nie mozna jej zmieniac
    X = [1, 2, 3];  # X[3] = 4  # <--- index jest out of range
    X = "abc";  # X.append("d") #<--- str nie ma metody append
    map(pow, range(8))  # nie przypisuje nigdzie wartosci mapowania


if __name__ == "__main__":
    main()
