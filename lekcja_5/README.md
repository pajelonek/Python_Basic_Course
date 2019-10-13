# Algorytmy i struktury danych w języku python 

Zestaw 5.

## Jak uruchomić

Wystarczy pobrać pliki pythonowe i uruchomić w dowolnym środowisku.
lecture_3.py zawiera wszystkie zadania oprócz : 3.1, 3.2 i 3.4.
## Treści zadań
##### ZADANIE 5.1
Stworzyć plik rekurencja.py i zapisać w nim funkcje z zadań 4.3 (factorial), 4.4 (fibonacci). Sprawdzić operacje importu i przeładowania modułu.

```
import rekurencja
# import rekurencja as rek
# from rekurencja import *
# from rekurencja import factorial
# from rekurencja import fibonacci as fib

print rekurencja.factorial(6)
print rekurencja.fibonacci(5)
```
##### ZADANIE 5.2
Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik]. Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions. Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.
Python wersja 2(użyty interpreter = 2.7.15)
```
def add_frac(frac1, frac2): pass        # frac1 + frac2

def sub_frac(frac1, frac2): pass        # frac1 - frac2

def mul_frac(frac1, frac2): pass        # frac1 * frac2

def div_frac(frac1, frac2): pass        # frac1 / frac2

def is_positive(frac): pass             # bool, czy dodatni

def is_zero(frac): pass                 # bool, typu [0, x]

def cmp_frac(frac1, frac2): pass        # -1 | 0 | +1

def frac2float(frac): pass              # konwersja do float

f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznaczność)
f5 = [0, 2]                   # zero (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): pass

    def test_mul_frac(self): pass

    def test_div_frac(self): pass

    def test_is_positive(self): pass

    def test_is_zero(self): pass

    def test_cmp_frac(self): pass

    def test_frac2float(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
```

## Użyto

* [anaconda2019](https://www.anaconda.com/distribution/) - środowisko pythona
* [pycharm](https://www.jetbrains.com/pycharm/download/) - dependency management

## Autor

* **Paweł Jelonek** 