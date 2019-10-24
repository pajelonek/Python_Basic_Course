import random


class RandomQueue:
    def __init__(self, size=10):
        self.n = size + 1
        self.items = self.n * [None]
        self.head = 0
        self.tail = 0

    def insert(self, item):
        if self.is_full():
            raise ValueError("Queue is full!")
        else:
            self.tail = (self.tail + 1) % self.n
            self.items[self.tail] = item

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        else:
            x = random.randint(self.head, (self.tail-1))
            return_element = self.items[x]
            switch_variable = self.items[self.head]
            self.items[self.head] = self.items[x]
            self.items[x] = switch_variable
            self.items[self.head] = None
            self.head = (self.head + 1) % self.n
        return return_element

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail