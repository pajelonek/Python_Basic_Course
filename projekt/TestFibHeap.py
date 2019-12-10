import unittest
from FibHeap import FibHeap


class TestQueue(unittest.TestCase):

    def test_error_push(self):
        heap = FibHeap()
        heap.push(5)
        heap.push(2)
        heap.push(9)
        heap.push(11)
        heap.show()

    def test_error_pop(self):
        pass

    def test_error_is_full(self):
        pass

    def test_error_is_empty(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
