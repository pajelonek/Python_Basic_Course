import unittest
from Rectangle import Rectangle
from Point import Point

class TestFrac(unittest.TestCase):

    def test_center_rectangle(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).center(), Point(1, 1))
        self.assertEqual(Rectangle(0, 0, 3, 3).center(), Point(1.5, 1.5))
        self.assertEqual(Rectangle(1, 1, 3, 3).center(), Point(2, 2))

    def test_area_rectangle(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).area(), 4)
        self.assertEqual(Rectangle(0, 0, 5, 5).area(), 25)
        self.assertEqual(Rectangle(1, 1, 3, 3).area(), 4)

    def test_move_rectangle(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).move(1, 1), Rectangle(1, 1, 3, 3))
        self.assertEqual(Rectangle(0, 0, 2, 2).move(2, 2), Rectangle(2, 2, 4, 4))
        self.assertEqual(Rectangle(0, 0, 2, 2).move(-2, -2), Rectangle(-2, -2, 0, 0))

    def test_intersection_rectangle(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).intersection(Rectangle(1, 1, 2, 2)), Rectangle(1, 1, 2, 2))
        self.assertEqual(Rectangle(0, 0, 4, 4).intersection(Rectangle(-1, -1, 2, 2)), Rectangle(0, 0, 2, 2))

    def test_cover_rectangle(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).cover(Rectangle(1, 1, 3, 3)), Rectangle(0, 0, 3, 3))
        self.assertEqual(Rectangle(0, 0, 4, 4).cover(Rectangle(-1, -1, 2, 2)), Rectangle(-1, -1, 4, 4))

    def test_make4_rectangle(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).make4(),  [Rectangle(0, 0, 2.0, 2.0), Rectangle(2.0, 0, 4, 2.0), Rectangle(0, 2.0, 2.0, 4), Rectangle(2.0, 2.0, 4, 4)])

if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
