# Algorytmy i struktury danych w języku python 

Zestaw 7.

## Jak uruchomić

Wystarczy pobrać pliki pythonowe i uruchomić w dowolnym środowisku.
## Treści zadań


##### ZADANIE 7.1 (KLASA FRAC)
W pliku fracs.py zdefiniować klasę Frac wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do obsługi błędów w ułamkach. Dodać możliwości dodawania liczb (int, long) do ułamków (działania lewostronne i prawostronne). Rozważyć możliwość włączenia liczb float do działań na ułamkach [Wskazówka: metoda float.as_integer_ratio()]. Napisać kod testujący moduł fracs.

```
class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        self.x = x
        self.y = y

    def __str__(self): pass         # zwraca "x/y" lub "x" dla y=1

    def __repr__(self): pass        # zwraca "Frac(x, y)"

    def __cmp__(self, other): pass  # porównywanie

    def __add__(self, other): pass  # frac1+frac2, frac+int

    __radd__ = __add__              # int+frac

    def __sub__(self, other): pass  # frac1-frac2, frac-int

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other): pass  # frac1*frac2, frac*int

    __rmul__ = __mul__              # int*frac

    def __div__(self, other): pass  # frac1/frac2, frac/int

    def __rdiv__(self, other): pass # int/frac

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self): pass         # -frac = (-1)*frac

    def __invert__(self): pass      # odwrotnosc: ~frac

    def __float__(self): pass       # float(frac)

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase): pass
```
##### ZADANIE 7.3 (KLASA RECTANGLE)
W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do obsługi błędów. Napisać kod testujący moduł rectangles.
```
from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self): pass         # "[(x1, y1), (x2, y2)]"

    def __repr__(self): pass        # "Rectangle(x1, y1, x2, y2)"

    def __eq__(self, other): pass   # obsługa rect1 == rect2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self): pass          # zwraca środek prostokąta

    def area(self): pass            # pole powierzchni

    def move(self, x, y): pass      # przesunięcie o (x, y)

    def intersection(self, other): pass # część wspólna prostokątów

    def cover(self, other): pass    # prostąkąt nakrywający oba

    def make4(self): pass           # zwraca listę czterech mniejszych

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase): pass
```
## Użyto

* [anaconda2019](https://www.anaconda.com/distribution/) - środowisko pythona
* [pycharm](https://www.jetbrains.com/pycharm/download/) - dependency management

## Autor

* **Paweł Jelonek** 