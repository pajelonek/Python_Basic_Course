import unittest
from RandomQueue import RandomQueue


class TestRandomQueue(unittest.TestCase):

    def test_insert_push(self):
        queue = RandomQueue()
        queue.insert(1)
        queue.insert(2)
        queue.insert(3)
        queue.insert(4)
        queue.insert(5)
        self.assertEqual(queue.is_full(), True)
        self.assertEqual(queue.items[0], 1)
        self.assertEqual(queue.items[1], 2)
        self.assertEqual(queue.items[2], 3)
        self.assertEqual(queue.items[3], 4)
        self.assertEqual(queue.items[4], 5)

    def test_remove_pop(self):
        queue = RandomQueue()
        queue.insert(4)
        queue.insert(3)
        queue.insert(7)
        queue.remove()
        self.assertEqual(queue.is_empty(), False)
        queue.remove()
        queue.remove()
        self.assertEqual(queue.is_empty(), False)

    def test_error_is_full(self):
        queue = RandomQueue()
        queue.insert(4)
        queue.insert(3)
        queue.insert(7)
        queue.insert(8)
        queue.insert(1)
        with self.assertRaises(ValueError):
            queue.insert(4)

    def test_error_is_empty(self):
        queue = RandomQueue()
        with self.assertRaises(ValueError):
            queue.remove()


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
