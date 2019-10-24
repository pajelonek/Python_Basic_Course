import unittest
from RandomQueue import RandomQueue


class TestRandomQueue(unittest.TestCase):

    def test_insert_push(self):
        queue = RandomQueue(size=3)
        queue.insert(1)
        queue.insert(2)
        queue.insert(3)
        self.assertEqual(queue.is_full(), True)
        self.assertEqual(queue.items[1], 1)
        self.assertEqual(queue.items[2], 2)
        self.assertEqual(queue.items[3], 3)

    def test_remove_pop(self):
        queue = RandomQueue(size=5)
        queue.insert(4)
        queue.insert(3)
        queue.insert(7)
        queue.remove()
        self.assertEqual(queue.is_empty(), False)
        queue.remove()
        queue.remove()
        self.assertEqual(queue.is_empty(), True)

    def test_error_is_full(self):
        queue = RandomQueue(size=3)
        queue.insert(4)
        queue.insert(3)
        queue.insert(7)
        with self.assertRaises(ValueError):
            queue.insert(4)

    def test_error_is_empty(self):
        queue = RandomQueue(size=3)
        with self.assertRaises(ValueError):
            queue.remove()


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
