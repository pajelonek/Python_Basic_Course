import unittest
from Queue import Queue


class TestQueue(unittest.TestCase):

    def test_error_push(self):
        queue = Queue(size=3)
        queue.put(1)
        queue.put(2)
        queue.put(3)
        with self.assertRaises(ValueError):
            queue.put(4)
        queue.get()
        queue.put(4)
        with self.assertRaises(ValueError):
            queue.put(5)

    def test_error_pop(self):
        queue = Queue(size=3)
        queue.put(5)
        queue.get()
        with self.assertRaises(ValueError):
            queue.get()

    def test_error_is_full(self):
        queue = Queue(size=3)
        self.assertEqual(queue.is_full(), False)
        queue.put(5)
        self.assertEqual(queue.is_full(), False)
        queue.put(5)
        queue.put(5)
        self.assertEqual(queue.is_full(), True)

    def test_error_is_empty(self):
        queue = Queue(size=3)
        self.assertEqual(queue.is_empty(), True)
        queue.put(5)
        self.assertEqual(queue.is_empty(), False)
        queue.get()
        self.assertEqual(queue.is_empty(), True)


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
