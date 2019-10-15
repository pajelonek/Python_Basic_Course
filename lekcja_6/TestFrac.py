import unittest
from Frac import Frac


class TestFrac(unittest.TestCase):

    def test_add_frac(self):
        self.assertEqual(Frac(1, 3) + Frac(1, 2), Frac(5, 6))
        self.assertEqual(Frac(1, 3) + Frac(0, 6), Frac(1, 3))
        self.assertEqual(Frac(49, 100) + Frac(51, 100), Frac(1, 1))
        self.assertEqual(Frac(1, 3) + Frac(1, 3), Frac(2, 3))
        self.assertEqual(Frac(0, 3) + Frac(0, 2), Frac(0, 6))

    def test_sub_frac(self):
        self.assertEqual(Frac(5, 7) - Frac(3, 7), Frac(2, 7))
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(0, 2) - Frac(3, 7), Frac(-3, 7))
        self.assertEqual(Frac(5, 6) - Frac(3, 12), Frac(7, 12))
        self.assertEqual(Frac(5, 7) - Frac(0, 7), Frac(5, 7))

    def test_mul_frac(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(0, 2) * Frac(1, 3), Frac(0, 6))
        self.assertEqual(Frac(18, 2) * Frac(1, 3), Frac(3, 1))
        self.assertEqual(Frac(1, 2) * Frac(0, 3), Frac(0, 6))
        self.assertEqual(Frac(-1, 2) * Frac(-1, 3), Frac(1, 6))
        self.assertEqual(Frac(-1, 2) * Frac(1, 3), Frac(-1, 6))

    def test_div_frac(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 3), Frac(3, 2))
        self.assertEqual(Frac(0, 2) / Frac(1, 3), Frac(0, 2))
        self.assertEqual(Frac(1, 3) / Frac(1, 6), Frac(2, 1))
        self.assertEqual(Frac(-1, 2) / Frac(1, 3), Frac(-3, 2))

    def test_str_frac(self):
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertEqual(str(Frac(0, 2)), "0/2")
        self.assertEqual(str(Frac(-1, 2)), "-1/2")
        self.assertEqual(str(Frac(2, 2)), "1.0")

    def test_repr_frac(self):
        self.assertEqual(repr(Frac(1, 2)), "Frac(1, 2)")
        self.assertEqual(repr(Frac(0, 2)), "Frac(0, 2)")
        self.assertEqual(repr(Frac(-1, 2)), "Frac(-1, 2)")
        self.assertEqual(repr(Frac(2, 2)), "Frac(1.0, 1.0)")

    def test_neg_frac(self):
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))
        self.assertEqual(-Frac(2, 1), Frac(-2, 1))

    def test_revert_frac(self):
        self.assertEqual(~Frac(1, 2), Frac(2, 1))
        self.assertEqual(~Frac(-2, 1), Frac(-1, 2))


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
