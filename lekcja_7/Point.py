import math


class Point:

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return "(" + self.x + ", " + self.y + ")"

    def __repr__(self):  # zwraca string "Point(x, y)"
        return "Point(" + self.x + ", " + self.y + ")"

    def __eq__(self, other):  # obsluga point1 == point2
        return self.x == other.x and self.y == other.y

    def __cmp__(self, other):  # obsluga point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return Point(self.x * other.x, self.y * other.y)

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))
