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
        self.assertEqual(heap_test_show.show_all_nodes(), "5 2 9 11 ")

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
        self.assertEqual(heap.show_all_nodes(), "5 2 9 11 ")

    def test_error_cutting(self):
        heap_test_pop = FibHeap()
        self.assertEqual(heap_test_pop.show_main_nodes(), "")
        heap_test_pop.push(5)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 ")
        heap_test_pop.push(2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 2 ")
        heap_test_pop.push(9)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 2 9 ")
        heap_test_pop.push(11)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 2 9 11 ")
        self.assertEqual(heap_test_pop.pop(), 2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 11 ")
        self.assertEqual(heap_test_pop.show_all_nodes(), "5 9 11 ")

    def test_error_cutting2(self):
        heap_test_pop = FibHeap()
        heap_test_pop.push(5)
        heap_test_pop.push(2)
        heap_test_pop.push(9)
        heap_test_pop.push(11)
        heap_test_pop.push(1)
        heap_test_pop.push(4)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 2 9 11 1 4 ")
        self.assertEqual(heap_test_pop.pop(), 1)
        self.assertEqual(heap_test_pop.show_main_nodes(), "2 4 ")
        self.assertEqual(heap_test_pop.show_all_nodes(), "2 9 11 5 4 ")

    def test_error_cutting3(self):
        heap_test_pop = FibHeap()
        heap_test_pop.push(2)
        heap_test_pop.push(7)
        heap_test_pop.push(9)
        heap_test_pop.push(11)
        self.assertEqual(heap_test_pop.show_main_nodes(), "2 7 9 11 ")
        self.assertEqual(heap_test_pop.pop(), 2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "7 11 ")
        self.assertEqual(heap_test_pop.show_all_nodes(), "7 9 11 ")

    def test_error_cutting4(self):
        heap_test_pop = FibHeap()
        heap_test_pop.push(11)
        heap_test_pop.push(7)
        heap_test_pop.push(9)
        heap_test_pop.push(2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "11 7 9 2 ")
        self.assertEqual(heap_test_pop.pop(), 2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "7 9 ")
        self.assertEqual(heap_test_pop.show_all_nodes(), "7 11 9 ")

    def test_error_cutting5(self):
        heap_test_pop = FibHeap()
        heap_test_pop.push(2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "2 ")
        self.assertEqual(heap_test_pop.pop(), 2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "")
        self.assertEqual(heap_test_pop.show_all_nodes(), "")

    def test_error_is_empty(self):
        heap = FibHeap()
        self.assertEqual(heap.is_empty(), True)
        heap.push(5)
        self.assertEqual(heap.is_empty(), False)

    def test_error_is_decrease(self):
        heap = FibHeap()
        self.assertEqual(heap.is_empty(), True)
        heap.push(5)
        self.assertEqual(heap.is_empty(), False)
        heap.decrease_key(5, 2)
        self.assertEqual(heap.show_all_nodes(), "2 ")
        heap.push(11)
        heap.push(7)
        heap.push(9)
        heap.push(19)
        heap.push(3)
        self.assertEqual(heap.show_all_nodes(), "2 11 7 9 19 3 ")
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.show_all_nodes(), "7 9 19 11 3 ")
        self.assertEqual(heap.show_main_nodes(), "7 3 ")


if __name__ == '__main__':
    unittest.main()
