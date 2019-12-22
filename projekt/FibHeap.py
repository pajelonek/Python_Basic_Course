class FibHeap:

    def __init__(self):
        self.min = None
        self.first = None
        self.last = None
        self.number_of_elements = 0

    def __str__(self):  # TODO
        pass

    def __link_roots(self, firstnode, secondnode):
        if not firstnode.has_key() or not secondnode.has_key():
            raise ValueError("Node cant be linked, has no key")

        firstnode, secondnode = FibHeap.__set_first_as_lower(firstnode, secondnode)

        self.cut_node_from_heap(secondnode)

        if firstnode.has_children():
            firstnode.get_children().set_left_sibling(secondnode)
            secondnode.set_right_sibling(firstnode.get_children())
        firstnode.set_children(secondnode)
        secondnode.set_parent(firstnode)

        firstnode.increment_rank()

    @staticmethod
    def __set_first_as_lower(firstnode, secondnode):
        if firstnode.get_key() > secondnode.get_key():
            container = secondnode
            secondnode = firstnode
            firstnode = container
            return firstnode, secondnode

    def __compare_with_min(self, node):
        if self.min.has_key() and node.has_key():
            if self.min.get_key() > node.get_key():
                self.min = node

    def __cut_min(self):

        self.cut_node_from_heap(self.min)
        self.number_of_elements = self.number_of_elements - 1

        if self.min.has_children():
            node_children = self.min.get_children()
            node_children.set_parent(None)
            self.min.set_children(None)
            if self.first.is_not_empty():
                self.first = node_children
                self.min = node_children
                if self.first.get_right_sibling().is_not_empty():
                    while node_children.has_right_sibling():
                        node_children = node_children.get_right_sibling()
                        node_children.set_parent(None)
                    self.last = node_children
                else:
                    self.last = self.first
            else:
                self.min = self.first
                while node_children.is_not_empty():
                    self.last.set_right_sibling(node_children)
                    node_children.set_left_sibling(self.last)
                    self.last = node_children
                    node_children.set_parent(None)
                    node_children = node_children.get_right_sibling()

            if self.first.is_not_empty():
                iterator = self.first
                while iterator.is_not_empty():
                    self.__compare_with_min(iterator)
                    iterator = iterator.get_right_sibling()
            else:
                self.min = None
        else:
            if self.first.is_not_empty():
                self.min = self.first
                iterator = self.first
                while iterator.is_not_empty():
                    self.__compare_with_min(iterator)
                    iterator = iterator.get_right_sibling()

    @staticmethod
    def cut_node_x_node(node_to_cut):
        node_to_cut.get_left_sibling().set_right_sibling(node_to_cut.get_right_sibling())
        node_to_cut.get_right_sibling().set_left_sibling(node_to_cut.get_left_sibling())
        node_to_cut.set_left_sibling(None)
        node_to_cut.set_right_sibling(None)

    def cut_x_node(self, node_to_cut):
        node_to_cut.get_right_sibling().set_left_sibling(None)
        self.first = self.min.get_right_sibling()
        node_to_cut.min.set_right_sibling(None)

    def cut_node_x(self, node_to_cut):
        node_to_cut.get_left_sibling().set_right_sibling(None)
        self.last = node_to_cut.get_left_sibling()
        node_to_cut.set_left_sibling(None)

    def cut_node_from_heap(self, node_to_cut):
        # case : node - X - node
        if node_to_cut.has_left_sibling() and node_to_cut.has_right_sibling():
            FibHeap.cut_node_x_node(node_to_cut)
        # case : X - node
        elif not node_to_cut.has_left_sibling() and node_to_cut.has_right_sibling():
            self.cut_x_node(self.min)
        # case : node - X
        elif node_to_cut.has_left_sibling() and not node_to_cut.has_right_sibling():
            self.cut_node_x(node_to_cut)
        # case : X
        else:
            self.first = None
            self.last = None

    def __consolidate_heap(self):  # TODO
        pass

    def push(self, x):
        new_node = Node().init_node(x)
        if self.size() == 0:
            self.first = new_node
            self.last = new_node
            self.min = new_node
        else:
            if self.size() == 1:
                self.first.set_right_sibling(new_node)
                new_node.set_left_sibling(self.first)
            else:
                self.last.set_right_sibling(new_node)
                new_node.set_left_sibling(self.last)
            self.last = new_node
            self.__compare_with_min(new_node)

        self.number_of_elements = self.number_of_elements + 1

    def __find(self):  # TODO
        pass

    def pop(self):
        if not self.is_empty():
            lowest_value = self.min.get_key()
            self.__cut_min()
            # self.__consolidate_heap()
            return lowest_value
        else:
            print("No elements in heap")

    def top(self):
        if not self.is_empty() and self.min.is_not_empty():
            return self.min.get_key()
        else:
            raise ValueError("Cant get value from heap")

    def size(self):
        return self.number_of_elements

    def decrease_key(self, old_key, new_key):  # TODO
        pass

    def remove(self, key):  # TODO
        pass

    def is_empty(self):
        return not self.number_of_elements

    def show_main_nodes(self):
        tree = ""
        if self.size() > 0:
            iterator = self.first
            while True:
                tree += str(iterator.get_key()) + " "
                if iterator.has_right_sibling():
                    iterator = iterator.get_right_sibling()
                else:
                    break
        return tree


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
        if isinstance(other, Node) and other is None:
            self.__parent = other
        else:
            raise TypeError("Other must be a Node or None")

    def get_parent(self):
        if self.__parent is not None:
            return self.__parent
        else:
            return None

    def has_parent(self):
        if self.get_parent() is not None:
            return True
        return False

    def set_children(self, other):
        if isinstance(other, Node) and other is None:
            self.__children = other
        else:
            raise TypeError("Other must be a Node or None")

    def get_children(self):
        if self.__children is not None:
            return self.__children
        else:
            return None

    def has_children(self):
        if self.get_children() is not None:
            return True
        return False

    def set_left_sibling(self, other):
        if isinstance(other, Node) and other is None:
            self.__left = other
        else:
            raise TypeError("Other must be a Node or None")

    def set_right_sibling(self, other):
        if isinstance(other, Node) and other is None:
            self.__right = other
        else:
            raise TypeError("Other must be a Node or None")

    def get_right_sibling(self):
        if self.__right is not None:
            return self.__right
        return None

    def has_right_sibling(self):
        if self.__right is not None:
            return True
        return False

    def has_left_sibling(self):
        if self.__left is not None:
            return True
        return False

    def get_left_sibling(self):
        if self.__left is not None:
            return self.__left
        return None

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
