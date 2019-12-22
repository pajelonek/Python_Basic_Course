import unittest
from FibHeap import FibHeap


class TestQueue(unittest.TestCase):

    def test_error_show(self):
        heap_test_show = FibHeap()
        self.assertEqual(heap_test_show.show_main_nodes(), "")
        heap_test_show.push(5)
        heap_test_show.push(2)
        heap_test_show.push(9)
        heap_test_show.push(11)
        self.assertEqual(heap_test_show.show_main_nodes(), "5 2 9 11 ")

    def test_error_push(self):
        heap = FibHeap()
        self.assertEqual(heap.show_main_nodes(), "")
        heap.push(5)
        self.assertEqual(heap.show_main_nodes(), "5 ")
        heap.push(2)
        self.assertEqual(heap.show_main_nodes(), "5 2 ")
        heap.push(9)
        self.assertEqual(heap.show_main_nodes(), "5 2 9 ")
        heap.push(11)
        self.assertEqual(heap.show_main_nodes(), "5 2 9 11 ")

    def test_error_pop(self):
        heap_test_pop = FibHeap()
        heap_test_pop.push(5)
        heap_test_pop.push(2)
        heap_test_pop.push(9)
        heap_test_pop.push(11)
        self.assertEqual(heap_test_pop.pop(), 2)

    def test_error_is_empty(self):
        heap = FibHeap()
        self.assertEqual(heap.is_empty(), True)
        heap.push(5)
        self.assertEqual(heap.is_empty(), False)


if __name__ == '__main__':
    unittest.main()
