import cmath
from logging import warning


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

        self.cut_main_node_from_heap(secondnode)

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
        self.cut_main_node_from_heap(self.min)
        self.number_of_elements = self.number_of_elements - 1

        if self.min.has_children():
            node_children = self.min.get_children()
            node_children.set_parent(None)
            self.min.set_children(None)
            self.add_children_to_heap(node_children)
            self.find_new_min_in_heap()
        else:
            if self.first is not None:
                self.min = self.first
                self.find_new_min_in_heap()

    def add_children_to_heap(self, children):
        if self.first is None:
            self.add_children_as_new_heap(children)
        else:
            self.add_children_as_end(children)

    def add_children_as_new_heap(self, children):
        self.first = children
        self.min = children
        if self.first.get_right_sibling().is_not_empty():
            while children.has_right_sibling():
                node_children = children.get_right_sibling()
                node_children.set_parent(None)
            self.last = children
        else:
            self.last = self.first

    def add_children_as_end(self, children):
        self.min = self.first
        while children.is_not_empty():
            self.last.set_right_sibling(children)
            children.set_left_sibling(self.last)
            self.last = children
            children.set_parent(None)
            children = children.get_right_sibling()

    def find_new_min_in_heap(self):
        if self.first.is_not_empty():
            iterator = self.first
            while iterator is not None:
                self.__compare_with_min(iterator)
                iterator = iterator.get_right_sibling()
        else:
            self.min = None

    @staticmethod
    def cut_main_node_x_node(node_to_cut):
        node_to_cut.get_left_sibling().set_right_sibling(node_to_cut.get_right_sibling())
        node_to_cut.get_right_sibling().set_left_sibling(node_to_cut.get_left_sibling())
        node_to_cut.set_left_sibling(None)
        node_to_cut.set_right_sibling(None)

    @staticmethod
    def cut_node_x_node(node_to_cut):
        node_to_cut.get_left_sibling().set_right_sibling(node_to_cut.get_right_sibling())
        node_to_cut.get_right_sibling().set_left_sibling(node_to_cut.get_left_sibling())
        node_to_cut.set_left_sibling(None)
        node_to_cut.set_right_sibling(None)
        node_to_cut.set_parent(None)

    def cut_main_x_node(self, node_to_cut):
        node_to_cut.get_right_sibling().set_left_sibling(None)
        self.first = node_to_cut.get_right_sibling()
        node_to_cut.set_right_sibling(None)

    def cut_x_node(self, node_to_cut):
        node_to_cut.get_parent().decrement_rank()
        node_to_cut.get_parent().set_children(node_to_cut.get_right_sibling())
        node_to_cut.get_right_sibling().set_left_sibling(None)
        node_to_cut.set_right_sibling(None)
        node_to_cut.set_parent(None)

    def cut_main_node_x(self, node_to_cut):
        node_to_cut.get_left_sibling().set_right_sibling(None)
        self.last = node_to_cut.get_left_sibling()
        node_to_cut.set_left_sibling(None)

    def cut_node_x(self, node_to_cut):
        node_to_cut.get_parent().decrement_rank()
        node_to_cut.get_left_sibling().set_right_sibling(None)
        node_to_cut.set_left_sibling(None)
        node_to_cut.set_parent(None)

    def cut_main_node_from_heap(self, node_to_cut):
        # case : node - X - node
        if node_to_cut.has_left_sibling() and node_to_cut.has_right_sibling():
            FibHeap.cut_main_node_x_node(node_to_cut)
        # case : X - node
        elif not node_to_cut.has_left_sibling() and node_to_cut.has_right_sibling():
            self.cut_main_x_node(node_to_cut)
        # case : node - X
        elif node_to_cut.has_left_sibling() and not node_to_cut.has_right_sibling():
            self.cut_main_node_x(node_to_cut)
        # case : X
        else:
            self.first = None
            self.last = None

    def cut_node_from_heap(self, node_to_cut):
        if node_to_cut.has_left_sibling() and node_to_cut.has_right_sibling():
            FibHeap.cut_node_x_node(node_to_cut)
            # case : X - node
        elif not node_to_cut.has_left_sibling() and node_to_cut.has_right_sibling():
            self.cut_x_node(node_to_cut)
            # case : node - X
        elif node_to_cut.has_left_sibling() and not node_to_cut.has_right_sibling():
            self.cut_node_x(node_to_cut)
            # case : X
        else:
            node_to_cut.get_parent().set_children(None)
            node_to_cut.get_parent().decrement_rank()
            node_to_cut.set_parent(None)

    def __consolidate_heap(self):
        if not self.is_empty():
            size_of_array = int((((cmath.log(self.size())) / (cmath.log(2))) + 1).real)
            table_of_array = [None] * size_of_array
            iterator = self.first
            while True:
                if iterator is None:
                    break
                else:
                    if table_of_array[iterator.get_rank()] is not None and iterator is not table_of_array[iterator.get_rank()]:
                        index = iterator.get_rank()
                        self.__link_roots(iterator, table_of_array[iterator.get_rank()])
                        table_of_array[index] = None
                        iterator = self.first
                    else:
                        table_of_array[iterator.get_rank()] = iterator
                        iterator = iterator.get_right_sibling()

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

    def __find(self, value):
        if self.is_empty() or self.min.get_key() > value:
            return None
        found_value = FibHeap.find_deeper(self.first, value)
        return found_value

    @staticmethod
    def find_deeper(node, value):
        if node.get_key() == value:
            return node
        if node.has_children():
            node_or_none = FibHeap.find_deeper(node.get_children(), value)
            if isinstance(node_or_none, Node):
                return node_or_none
        if node.has_right_sibling():
            node_or_none = FibHeap.find_deeper(node.get_right_sibling(), value)
            if isinstance(node_or_none, Node):
                return node_or_none

    def pop(self):
        if not self.is_empty():
            lowest_value = self.min.get_key()
            self.__cut_min()
            self.__consolidate_heap()
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

    def decrease_key(self, old_key, new_key):
        if self.is_empty():
            raise ValueError("No nodes in heap")
        node_to_change = self.__find(old_key)
        if not isinstance(node_to_change, Node):
            warning("No nodes with given value in heap")
            return False
        node_to_change.set_key(new_key)
        if node_to_change.has_parent() and node_to_change.get_parent().get_key() > node_to_change.get_key():
            self.fix_violated_order(node_to_change)

    def fix_violated_order(self, node):
        parent = node.get_parent()
        self.cut_node_from_heap(node)
        node.set_mark('N')
        self.meld_in_tree(node)
        if parent.get_mark() is 'N' and parent.get_parent() is not None:
            parent.set_mark('Y')
        else:
            while parent is not None:
                if parent.get_mark() is 'N':
                    break
                elif parent.has_parent():
                    self.cut_parent_from_heap(parent)
                    parent.get_parent().decrement_rank()
                    self.last.set_right_sibling(parent)
                    parent.set_left_sibling(parent)
                    parent.set_mark('N')
                parent = parent.get_parent()
            iterator = self.first
            self.min = self.first
            while iterator is not None:
                self.__compare_with_min(iterator)
                iterator = iterator.get_right_sibling()

    def cut_parent_from_heap(self, parent):
        if parent.has_left_sibling() and parent.has_right_sibling():
            parent.get_left_sibling().set_right_parent(parent.get_right_sibling())
            parent.get_right_sibling().set_left_parent(parent.get_left_sibling())
            parent.set_left_sibling(None)
            parent.set_right_sibling(None)
        elif not parent.has_left_sibling() and parent.has_right_sibling():
            parent.get_right_sibling().set_left_sibling(None)
            parent.get_parent().set_children(parent.get_right_sibling())
            parent.set_children(None)
            parent.set_right_children(None)
        elif parent.has_left_sibling() and not parent.has_right_sibling():
            parent.get_left_sibling().set_right_sibling(None)
            parent.set_left_sibling(None)
        else:
            parent.get_parent().set_children(None)
            parent.set_parent(None)

    def meld_in_tree(self, node):
        if self.size() is 1:
            self.first.set_right_sibling(node)
            node.set_left_sibling(self.first)
            self.last = node
            self.__compare_with_min(node)
        else:
            self.last.set_right_sibling(node)
            node.set_left_sibling(self.last)
            self.last = node
            self.__compare_with_min(node)

    def remove(self, key):  # TODO
        if self.is_empty():
            warning("No nodes in heap so can't remove one")
            return False
        node_to_remove = self.__find(key)
        if not isinstance(node_to_remove, Node):
            warning("No nodes with given value in heap")
            return False
        if self.size() is 1:
            self.last = None
            self.first = None
            node_to_remove.make_it(None)
        else:
            if node_to_remove.has_parent():
                self.cut_node_for_remove(node_to_remove)
                if node_to_remove.has_children():
                    node_to_remove = node_to_remove.get_children()
                    node_to_remove.get_parent().set_children(None)
                    node_to_remove.set_children(None)

                    while node_to_remove is not None:
                        if self.first is self.last:
                            self.last = node_to_remove
                            node_to_remove.set_left_element(self.first)
                            self.first.set_right_sibling(self.last)
                        else:
                            self.last.set_right_sibling(node_to_remove)
                            node_to_remove.set_left_sibling(self.last)
                            self.last = node_to_remove
                            node_to_remove.set_parent(None)
                        self.__compare_with_min(node_to_remove)
                        node_to_remove = node_to_remove.get_right_sibling()
            else:
                if node_to_remove.has_left_sibling() and node_to_remove.has_right_sibling():
                    node_to_remove.get_left_sibling().set_right_sibling(node_to_remove.get_right_sibling())
                    node_to_remove.get_right_sibling().set_left_sibling(node_to_remove.get_left_sibling())
                    node_to_remove.set_left_sibling(None)
                    node_to_remove.set_right_sibling(None)
                elif not node_to_remove.has_left_sibling() and node_to_remove.has_right_sibling():
                    node_to_remove.get_right_sibling().set_left_sibling(None)
                    self.first = node_to_remove.get_right_sibling()
                    node_to_remove.set_right_sibling(None)
                elif node_to_remove.has_left_sibling() and not node_to_remove.has_right_sibling():
                    node_to_remove.get_left_sibling().set_right_sibling(None)
                    self.last = node_to_remove.get_left_sibling()
                    node_to_remove.set_left_sibling(None)
                else:
                    self.last = None
                    self.first = None

                if node_to_remove.has_children():
                    children = node_to_remove.get_children()
                    if self.first is None:
                        self.first = children
                        children.set_parent(None)
                        children = children.get_right_sibling()
                    elif self.first is self.last:
                        self.first.set_right_sibling(children)
                        children.set_parent(None)
                        children.set_left_sibling(self.first)
                        self.last = children
                        children = children.get_right_sibling()

                    while children is not None:
                        self.last.set_right_sibling(children)
                        children.set_left_sibling(self.last)
                        self.last = children
                        children.set_parent(None)
                        children = children.get_right_sibling()

        self.number_of_elements = self.number_of_elements + 1

    def cut_node_for_remove(self, node_to_remove):
        if node_to_remove.has_left_sibling() and node_to_remove.has_right_sibling():
            node_to_remove.get_left_sibling().set_right_sibling(node_to_remove.get_right_sibling())
            node_to_remove.get_right_sibling().set_left_sibling(node_to_remove.get_left_sibling())
            node_to_remove.set_left_sibling(None)
            node_to_remove.set_right_sibling(None)
            node_to_remove.set_parent(None)
        elif node_to_remove.has_left_sibling() and not node_to_remove.has_right_sibling():
            node_to_remove.get_left_sibling().set_right_sibling(None)
            node_to_remove.set_left_sibling(None)
            node_to_remove.set_parent(None)
        elif not node_to_remove.has_left_sibling() and node_to_remove.has_right_sibling():
            node_to_remove.get_right_sibling().set_left_sibling(None)
            node_to_remove.get_parent().set_children(node_to_remove.get_right_sibling())
            node_to_remove.set_right_sibling(None)
            node_to_remove.set_parent(None)
        else:
            node_to_remove.get_parent().set_children(None)
            node_to_remove.set_parent(None)

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

    def show_all_nodes(self):
        tree = ""
        if self.is_empty() is not True:
            tree = FibHeap.print_all_nodes(self.first, tree)
        return tree

    @staticmethod
    def print_all_nodes(node, tree):
        tree += str(node.get_key()) + " "
        if node.has_children():
            tree = FibHeap.print_all_nodes(node.get_children(), tree)
        if node.has_right_sibling():
            tree = FibHeap.print_all_nodes(node.get_right_sibling(), tree)
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

    def is_empty(self):
        return self.__parent is None and self.__children is None and self.__left is None \
               and self.__right is None and self.__rank is None and self.__key is None \
               and self.__mark is None

    def is_not_empty(self):
        return self.__parent is not None or self.__children is not None or self.__left is not None \
               or self.__right is not None or self.__rank is not None or self.__key is not None \
               or self.__mark is not None

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
        if isinstance(other, Node) or other is None:
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
        if isinstance(other, Node) or other is None:
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
        if isinstance(other, Node) or other is None:
            self.__left = other
        else:
            raise TypeError("Other must be a Node or None")

    def set_right_sibling(self, other):
        if isinstance(other, Node) or other is None:
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

    def make_it(self, other):
        if other is None:
            self.__init__()
        if isinstance(other, Node):
            self.__parent = other.get_parent()
            self.__children = other.get_children()
            self.__left = other.get_left_sibling()
            self.__right = other.get_right_sibling()
            self.__rank = other.get_rank()
            self.__key = other.get_key()
            self.__mark = other.get_mark()

    def init_node(self, other):
        self.set_key(other)
        self.set_rank(0)
        self.set_mark('N')
        return self
