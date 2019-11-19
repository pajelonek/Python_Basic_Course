import math


class Frac:

    def __init__(self, x=0, y=1):

        if y == 0:
            raise ValueError("Y cannot be 0")

        n = math.gcd(int(x), int(y))
        if n != 1 and x != 0:
            self.x = x / n
            self.y = y / n
        else:
            self.x = x
            self.y = y
        self.normalize()

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.y)
        return str(self.x) + "/" + str(self.y)

    def __repr__(self):  # zwraca "Frac(x, y)"
        return "Frac(" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, other):  # frac1 + frac2
        if self.y != other.y:
            return Frac(self.x * other.y + other.x * self.y, self.y * other.y)
        return Frac(self.x + other.x, self.y)

    def __radd__(self, value):
        if isinstance(value, float):
            return self + Frac(float.as_integer_ratio(value)[0], float.as_integer_ratio(value)[1])
        if self.x == 0:
            return Frac(value * self.y, self.y)
        return Frac(self.x + (value * self.y), self.y)

    def __sub__(self, other):  # frac1 - frac2
        if self.y != other.y:
            return Frac(self.x * other.y - other.x * self.y, self.y * other.y)
        return Frac(self.x - other.x, self.y)

    def __rsub__(self, other):  # int-frac
        if isinstance(other, float):
            return Frac(float.as_integer_ratio(other)[0], float.as_integer_ratio(other)[1]) - self
        return Frac((self.y * other) - self.x, self.y)

    def __mul__(self, other):
        return Frac(self.x * other.x, self.y * other.y)

    def __rmul__(self, other):  # int*frac
        if isinstance(other, float):
            return self * Frac(float.as_integer_ratio(other)[0], float.as_integer_ratio(other)[1])
        return Frac(self.x * other, self.y)

    def __truediv__(self, other):
        return Frac(self.x * other.y, self.y * other.x) # frac1 / frac2

    def __rtruediv__(self, other):  # int/frac
        if self.x == 0:
            raise ValueError("Denominator cannot be 0")
        if isinstance(other, float):
            return Frac(float.as_integer_ratio(other)[0], float.as_integer_ratio(other)[1]) / self
        return Frac(other * self.y, self.x)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        self.x *= 1
        return Frac(self.x * 1, self.y)

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        if self.x > 0:
            return Frac(self.y, self.x)
        return Frac(-self.y, -self.x)

    def __cmp__(self, other):  # cmp(frac1, frac2)
        return self.x == other.x and self.y == other.y

    def __eq__(self, other):  # cmp(frac1, frac2)
        return self.x == other.x and self.y == other.y

    def __float__(self):
        if self.y == 0:
            raise NameError("Y cannot be 0")
        return float(self.x / self.y)  # float(frac)

    def normalize(self):
        if self.x != 0:
            n = math.gcd(int(self.x), int(self.y))
            if n != 1:
                self.x = self.x / int(n)
                self.y = self.y / int(n)
        return self
