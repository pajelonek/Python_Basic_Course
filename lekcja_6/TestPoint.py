import unittest
from Point import Point


class TestPoint(unittest.TestCase):

    def test_add_point(self):
        self.assertEqual(Point(1, 3) + Point(1, 2), Point(2, 5))
        self.assertEqual(Point(1, 3) + Point(-1, -3), Point(0, 0))
        self.assertEqual(Point(-1, 3) + Point(1, 2), Point(0, 5))
        self.assertEqual(Point(0, 0) + Point(1, 1), Point(1, 1))

    def test_sub_point(self):
        self.assertEqual(Point(1, 3) - Point(1, 2), Point(0, 1))
        self.assertEqual(Point(1, 3) - Point(1, 3), Point(0, 0))
        self.assertEqual(Point(-1, 3) - Point(1, 2), Point(-2, 1))
        self.assertEqual(Point(0, 0) - Point(1, 1), Point(-1, -1))

    def test_mul_point(self):
        self.assertEqual(Point(1, 3) * Point(1, 2), Point(1, 6))
        self.assertEqual(Point(1, 3) * Point(1, 3), Point(1, 9))
        self.assertEqual(Point(-1, 3) * Point(1, 2), Point(-1, 6))
        self.assertEqual(Point(0, 0) * Point(1, 1), Point(0, 0))

    def test_cross_point(self):
        self.assertEqual(Point(1, 3).cross(Point(1, 2)), -1)
        self.assertEqual(Point(1, 3).cross(Point(1, 3)), 0)
        self.assertEqual(Point(-1, 3).cross(Point(1, 2)), -5)
        self.assertEqual(Point(0, 0).cross(Point(1, 1)), 0)


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
