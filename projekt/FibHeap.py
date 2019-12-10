class FibHeap:

    def __init__(self):
        self.min = Node()
        self.first = Node()
        self.last = Node()
        self.number_of_elements = 0

    def __str__(self):
        pass

    @staticmethod
    def __link_roots(firstnode, secondnode):
        pass

    def __compare_with_min(self, node):
        pass

    def __cut_min(self):
        pass

    def __consolidate_heap(self):
        pass

    def __find(self):
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def size(self):
        pass

    def decrease_key(self, old_key, new_key):
        pass

    def remove(self, key):
        pass


class Node:
    def __init__(self):
        self.parent = None
        self.children = None
        self.left = None
        self.right = None
        self.rank = None
        self.key = None
        self.mark = None
