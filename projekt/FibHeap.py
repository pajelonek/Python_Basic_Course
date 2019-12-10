class FibHeap:

    def __init__(self):
        self.min = None
        self.first = None
        self.last = None
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
        new_node = Node().init_node(x)
        if self.size() == 0:
            self.first = new_node
            self.last = new_node
            self.min = new_node
        elif self.size() == 1:
            self.first.set_right_sibling(x)
            new_node.set_left_sibling(self.first)
            self.last = new_node
        else:
            self.last.set_right_sibling(new_node)
            new_node.set_left_sibling(self.last)
            self.last = new_node
            self.__compare_with_min(new_node)

        self.number_of_elements = self.number_of_elements + 1

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
        self.__parent = None
        self.__children = None
        self.__left = None
        self.__right = None
        self.__rank = None
        self.__key = None
        self.__mark = None

    def is_not_empty(self):
        return self.__parent is None and self.__children is None and self.__left is None \
               and self.__right is None and self.__rank is None and self.__key is None \
               and self.__mark is None

    def has_key(self):
        if self.get_key() is not None:
            return True
        return False

    def get_key(self):
        return self.__key

    def get_mark(self):
        return self.__mark

    def get_rank(self):
        return self.__rank

    def set_parent(self, other):
        if isinstance(other, Node):
            self.__parent = other
        else:
            raise TypeError("Other must be a Node")

    def set_children(self, other):
        if isinstance(other, Node):
            self.__children = other
        else:
            raise TypeError("Other must be a Node")

    def set_left_sibling(self, other):
        if isinstance(other, Node):
            self.__left = other
        else:
            raise TypeError("Other must be a Node")

    def set_right_sibling(self, other):
        if isinstance(other, Node):
            self.__right = other
        else:
            raise TypeError("Other must be a Node")

    def set_key(self, other):
        if not self.has_key() is None or isinstance(self.get_key(), other):
            self.__key = other
        else:
            raise TypeError("Key must stay the same")

    def set_rank(self, other):
        if self.get_rank() is None or isinstance(other, int):
            self.__rank = other
        else:
            raise TypeError("Key must stay the same")

    def increment_rank(self):
        if self.get_rank() is not None:
            self.set_rank(self.get_rank() + 1)
        else:
            raise ValueError("Rank is None")

    def decrement_rank(self):
        if self.get_rank() is not None:
            self.set_rank(self.get_rank() - 1)
        else:
            raise ValueError("Rank is None")

    def set_mark(self, other):
        if self.get_mark() is None or isinstance(self.__mark, other):
            self.__mark = other
        else:
            raise TypeError("Type of mark is not correct")

    def init_node(self, other):
        self.set_key(other)
        self.set_rank(0)
        self.set_mark('N')
        return self
