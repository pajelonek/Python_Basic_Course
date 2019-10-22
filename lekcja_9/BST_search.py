class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


def bst_max(top):
    if top is None:
        raise ValueError("Empty tree")
    if top.right is None:
        return top
    while top.right is not None:
        top = top.right
    return top


def bst_min(top):
    if top is None:
        raise ValueError("Empty tree")
    if top.left is None:
        return top
    while top.left is not None:
        top = top.left
    return top


def main():
    node = Node(1)
    left = Node(2)
    left2 = Node(3)
    node.left = left
    left.left = left2

    print("Test bst_min = " + str(bst_min(node).data))

    right = Node(2)
    right2 = Node(3)
    node.right = right
    right.right = right2

    print("Test bst_min = " + str(bst_max(node).data))


if __name__ == '__main__':
    main()  # uruchamia wszystkie testy
