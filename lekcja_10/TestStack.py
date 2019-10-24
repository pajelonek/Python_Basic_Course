import unittest
from Stack import Stack


class TestStack(unittest.TestCase):

    def test_error_push(self):
        stack = Stack(size=3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        with self.assertRaises(ValueError):
            stack.push(4)
        stack.pop()
        stack.push(4)
        with self.assertRaises(ValueError):
            stack.push(5)

    def test_error_pop(self):
        stack = Stack(size=3)
        stack.push(5)
        stack.pop()
        with self.assertRaises(ValueError):
            stack.pop()

    def test_error_is_full(self):
        stack = Stack(size=3)
        self.assertEqual(stack.is_full(), False)
        stack.push(5)
        self.assertEqual(stack.is_full(), False)
        stack.push(5)
        stack.push(5)
        self.assertEqual(stack.is_full(), True)

    def test_error_is_empty(self):
        stack = Stack(size=3)
        self.assertEqual(stack.is_empty(), True)
        stack.push(5)
        self.assertEqual(stack.is_empty(), False)
        stack.pop()
        self.assertEqual(stack.is_empty(), True)


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
