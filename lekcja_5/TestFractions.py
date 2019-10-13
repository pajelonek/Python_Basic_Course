import unittest
import fracs


class TestFractions(unittest.TestCase):

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([0, 2], [1, 3]), [1, 3])
        self.assertEqual(fracs.add_frac([-1, 2], [1, 2]), [0, 0])
        self.assertEqual(fracs.add_frac([1, 3], [1, 3]), [2, 3])
        self.assertEqual(fracs.add_frac([49, 100], [51, 100]), [1, 1])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([5, 7], [3, 7]), [2, 7])
        self.assertEqual(fracs.sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.sub_frac([0, 2], [3, 7]), [-3, 7])
        self.assertEqual(fracs.sub_frac([5, 6], [3, 12]), [7, 12])
        self.assertEqual(fracs.sub_frac([5, 7], [0, 7]), [5, 7])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.mul_frac([0, 2], [1, 3]), [0, 0])
        self.assertEqual(fracs.mul_frac([18, 2], [1, 3]), [3, 1])
        self.assertEqual(fracs.mul_frac([1, 2], [0, 3]), [0, 0])
        self.assertEqual(fracs.mul_frac([-1, 2], [-1, 3]), [1, 6])
        self.assertEqual(fracs.mul_frac([-1, 2], [1, 3]), [-1, 6])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(fracs.div_frac([0, 2], [1, 3]), [0, 0])
        self.assertEqual(fracs.div_frac([1, 3], [1, 6]), [2, 1])
        self.assertEqual(fracs.div_frac([-1, 2], [1, 3]), [-3, 2])
        self.assertEqual(fracs.div_frac([1, 2], [0, 3]), [0, 0])

    def test_is_positive(self):
        self.assertEqual(fracs.is_positive([1, 2]), True)
        self.assertEqual(fracs.is_positive([-1, 2]), False)
        self.assertEqual(fracs.is_positive([0, 2]), False)
        self.assertEqual(fracs.is_positive([17, 2]), True)
        self.assertEqual(fracs.is_positive([-1, -2]), True)
        self.assertEqual(fracs.is_positive([2, -1]), False)

    def test_is_zero(self):
        self.assertEqual(fracs.is_zero([0, 2]), True)
        self.assertEqual(fracs.is_zero([1, 2]), False)
        self.assertEqual(fracs.is_zero([0, 0]), True)
        self.assertEqual(fracs.is_zero([2, 0]), False)  # <==== doesn't exist!

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([1, 2], [1, 3]), -1)
        self.assertEqual(fracs.cmp_frac([1, 3], [1, 2]), 1)
        self.assertEqual(fracs.cmp_frac([1, 3], [1, 3]), 0)
        self.assertEqual(fracs.cmp_frac([1, 2], [-1, 3]), -1)
        self.assertEqual(fracs.cmp_frac([-1, 2], [1, 3]), 1)
        self.assertEqual(fracs.cmp_frac([0, 2], [1, 3]), 1)
        self.assertEqual(fracs.cmp_frac([0, 2], [-1, 3]), -1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([0, 2]), 0)
        self.assertEqual(fracs.frac2float([2, 2]), 1)
        self.assertEqual(fracs.frac2float([1, 2]), 0.5)
        self.assertEqual(fracs.frac2float([1, 3]), 0.3333333333333333)
        self.assertEqual(fracs.frac2float([7, 2]), 3.5)


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
