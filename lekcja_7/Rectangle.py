from Point import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if x1 < x2 and y1 < y2:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
        else:
            raise ValueError("Incorrect values ")

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(
            self.pt2.y) + ")]"

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(
            self.pt2.y) + ")"

    def __eq__(self, other):  # obsługa rect1 == rect2
        if other.pt1 == self.pt1 and other.pt2 == self.pt2:
            return True
        return False

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2.0, (self.pt1.y + self.pt2.y) / 2.0)

    def area(self):  # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):  # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other):  # część wspólna prostokątów
        return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x),
                         min(self.pt2.y, other.pt2.y))

    def cover(self, other):  # prostąkąt nakrywający oba
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x),
                         max(self.pt2.y, other.pt2.y))

    def make4(self):  # zwraca listę czterech mniejszych
        x_half = (self.pt2.x + self.pt1.x) / 2.0
        y_half = (self.pt2.y + self.pt1.y) / 2.0
        return [Rectangle(self.pt1.x, self.pt1.y, x_half, y_half),
                Rectangle(x_half, self.pt1.y, self.pt2.x, y_half),
                Rectangle(self.pt1.x, y_half, x_half, self.pt2.y),
                Rectangle(x_half, y_half, self.pt2.x, self.pt2.y)]
