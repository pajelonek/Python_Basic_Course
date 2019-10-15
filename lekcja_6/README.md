# Algorytmy i struktury danych w języku python 

Zestaw 6.

## Jak uruchomić

Wystarczy pobrać pliki pythonowe i uruchomić w dowolnym środowisku.
## Treści zadań


##### ZADANIE 6.2 (KLASA POINT)
W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami. Punkty są traktowane jak wektory zaczepione w początku układu współrzędnych, o końcu w położeniu (x, y). Napisać kod testujący moduł points.
```
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self): pass         # zwraca string "(x, y)"

    def __repr__(self): pass        # zwraca string "Point(x, y)"

    def __eq__(self, other): pass   # obsługa point1 == point2

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other): pass  # v1 + v2

    def __sub__(self, other): pass  # v1 - v2

    def __mul__(self, other): pass  # v1 * v2, iloczyn skalarny

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self): pass          # długość wektora

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): pass
```
##### ZADANIE 6.5 (KLASA FRAC)
W pliku fracs.py zdefiniować klasę Frac wraz z potrzebnymi metodami. Ułamek jest reprezentowany przez parę liczb całkowitych. Napisać kod testujący moduł fracs.
```
class Frac:
    """Klasa reprezentująca ułamek."""

    class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self): pass         # zwraca "x/y" lub "x" dla y=1

    def __repr__(self): pass        # zwraca "Frac(x, y)"

    def __add__(self, other): pass  # frac1 + frac2

    def __sub__(self, other): pass  # frac1 - frac2

    def __mul__(self, other): pass  # frac1 * frac2

    def __div__(self, other): pass  # frac1 / frac2

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __cmp__(self, other): pass  # cmp(frac1, frac2)

    def __float__(self): pass       # float(frac)

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase): pass

```
## Użyto

* [anaconda2019](https://www.anaconda.com/distribution/) - środowisko pythona
* [pycharm](https://www.jetbrains.com/pycharm/download/) - dependency management

## Autor

* **Paweł Jelonek** 