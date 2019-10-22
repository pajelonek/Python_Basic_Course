class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        if self.length == 0:  # zabezpieczenie
            self.tail = None
        return node  # zwracamy usuwany node

    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.

    def remove_tail(self):  # klasy O(N)
        if self.length == 0:
            raise ValueError("brak elementow w liscie")
        node = self.tail
        if node == self.head:
            self.head = None
            self.tail = None
            self.length = None
        else:
            new_node = self.head
            while not new_node.next == node:
                new_node = new_node.next
            if new_node.next == node:
                self.tail = new_node
                new_node.next = None
                self.length = self.length - 1
        return node

    def merge(self, other):  # klasy O(1)
        if self.length == 0:
            self = other
        elif other.length != 0:
            self.tail.next = other.head
            self.tail = other.tail
            self.length = self.length + other.length

        # Węzły z listy other są przepinane do listy self na jej koniec.

    def clear(self):  # czyszczenie listy
        self.head = None
        self.tail = None
        self.length = 0


def main():
    # Zastosowanie.
    alist = SingleList()
    alist.insert_head(Node(11))  # [11]
    alist.insert_head(Node(22))  # [22, 11]
    alist.insert_tail(Node(33))  # [22, 11, 33]
    print("length = " + str(alist.length))  # odczyt atrybutu
    print("length = " + str(alist.count()))  # wykorzystujemy interfejs
    # while not alist.is_empty():  # kolejność 22, 11, 33
    #    print("remove head " + str(alist.remove_head()))
    node = alist.remove_tail()
    print("Remove tail = " + str(node.data))
    node = alist.remove_tail()
    print("Remove tail = " + str(node.data))

    blist = SingleList()
    blist.insert_head(Node(5))
    blist.insert_head(Node(6))
    alist.merge(blist)
    node = alist.remove_tail()
    print("Remove tail = " + str(node.data))
    alist.clear()
    print("Clear = " + str(alist.length))


if __name__ == '__main__':
    main()  # uruchamia wszystkie testy
