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
        if not self.is_empty() and self.min.is_not_empty():
            return self.min.get_key()
        else:
            raise ValueError("Cant get value from heap")

    def size(self):
        return self.number_of_elements

    def decrease_key(self, old_key, new_key):
        pass

    def remove(self, key):
        pass

    def is_empty(self):
        return not self.number_of_elements


class Node:
    def __init__(self):
        self.parent = None
        self.children = None
        self.left = None
        self.right = None
        self.rank = None
        self.key = None
        self.mark = None

    def is_not_empty(self):
        return self.parent is None and self.children is None and self.left is None \
               and self.right is None and self.rank is None and self.key is None \
               and self.mark is None

    def has_hey(self):
        return self.key is not None

    def get_key(self):
        return self.key

    def set_parent(self, other):
        if isinstance(self, other):
            self.parent = other
        else:
            raise TypeError("Other must be a Node")

    def set_children(self, other):
        if isinstance(self, other):
            self.children = other
        else:
            raise TypeError("Other must be a Node")

    def set_left_sibling(self, other):
        if isinstance(self, other):
            self.left = other
        else:
            raise TypeError("Other must be a Node")

    def set_right_sibling(self, other):
        if isinstance(self, other):
            self.right = other
        else:
            raise TypeError("Other must be a Node")

    def set_key(self, other):
        if isinstance(self.key, other):
            self.key = other
        else:
            raise TypeError("Other must be a Node")

    def set_rank(self, other):
        if isinstance(other, int):
            self.rank = other

    def increment_rank(self):
        if self.rank is not None:
            self.rank = self.rank + 1
        else:
            raise ValueError("Rank is None")

    def decrement_rank(self):
        if self.rank is not None:
            self.rank = self.rank - 1
        else:
            raise ValueError("Rank is None")

    def set_mark(self, other):
        if isinstance(self.mark, other):
            self.mark = other
        else:
            raise TypeError("Type of mark is not correct")
