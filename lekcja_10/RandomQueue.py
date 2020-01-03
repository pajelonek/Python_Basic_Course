import random


class RandomQueue:
    def __init__(self, size=5):
        self.items = []
        self.size = size

    def insert(self, item):
        if self.is_full():
            raise ValueError("Queue is full!")
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        index = random.randint(0, len(self.items) - 1)
        element = self.items[index]
        self.items[index] = self.items[-1]
        del self.items[-1]
        return element

    def is_empty(self):
        return self.items is 0

    def is_full(self):
        return len(self.items) is self.size
