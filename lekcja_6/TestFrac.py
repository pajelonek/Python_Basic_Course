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
 #    def __invert__(self):  # odwrotnosc: ~frac
 #        return Frac(self.y, self.x)

 #    def __float__(self):
 #        if self.y == 0:
 #            raise NameError("Y cannot be 0")
 #        return float(self.x / self.y)  # float(frac)


   # def test_is_positive(self):
        # self.assertEqual(Frac([1, 2]), True)
        # self.assertEqual(fracs.is_positive([-1, 2]), False)
        # self.assertEqual(fracs.is_positive([0, 2]), False)
        # self.assertEqual(fracs.is_positive([17, 2]), True)
        # self.assertEqual(fracs.is_positive([-1, -2]), True)
        # self.assertEqual(fracs.is_positive([2, -1]), False)
        #
        # def test_is_zero(self):
        #     self.assertEqual(fracs.is_zero([0, 2]), True)
        #     self.assertEqual(fracs.is_zero([1, 2]), False)
        #     self.assertEqual(fracs.is_zero([0, 0]), True)
        #     self.assertEqual(fracs.is_zero([2, 0]), False)  # <==== doesn't exist!
        #
        # def test_cmp_frac(self):
        #     self.assertEqual(fracs.cmp_frac([1, 2], [1, 3]), -1)
        #     self.assertEqual(fracs.cmp_frac([1, 3], [1, 2]), 1)
        #     self.assertEqual(fracs.cmp_frac([1, 3], [1, 3]), 0)
        #     self.assertEqual(fracs.cmp_frac([1, 2], [-1, 3]), -1)
        #     self.assertEqual(fracs.cmp_frac([-1, 2], [1, 3]), 1)
        #     self.assertEqual(fracs.cmp_frac([0, 2], [1, 3]), 1)
        #     self.assertEqual(fracs.cmp_frac([0, 2], [-1, 3]), -1)
        #
        # def test_frac2float(self):
        #     self.assertEqual(fracs.frac2float([0, 2]), 0)
        #     self.assertEqual(fracs.frac2float([2, 2]), 1)
        #     self.assertEqual(fracs.frac2float([1, 2]), 0.5)
        #     self.assertEqual(fracs.frac2float([1, 3]), 0.3333333333333333)
        #     self.assertEqual(fracs.frac2float([7, 2]), 3.5)


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
