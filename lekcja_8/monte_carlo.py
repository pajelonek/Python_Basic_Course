import random
import math


def w_kole(x, y):
    r_p = math.sqrt(x * x + y * y)
    if r_p < 1.0:
        return True
    return False


def calc_pi(n=10000):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    liczba_w_srodku = 0
    for i in range(0, n):
        x = random.random()
        y = random.random()
        if w_kole(x, y):
            liczba_w_srodku = liczba_w_srodku + 1

    return  (float(liczba_w_srodku) / n) * 4


def main():
    print("Wynik dla 10:"+str(calc_pi(10)))
    print("Wynik dla 100:" + str(calc_pi(100)))
    print("Wynik dla 1000:" + str(calc_pi(1000)))
    print("Wynik dla 10000:" + str(calc_pi(10000)))
    print("Wynik dla 100000:" + str(calc_pi(100000)))
    print("Wynik dla 1000000:" + str(calc_pi(1000000)))


if __name__ == '__main__':
    main()  # uruchamia wszystkie testy
