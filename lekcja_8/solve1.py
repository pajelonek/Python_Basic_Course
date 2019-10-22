import matplotlib.pyplot as plt

def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b != 0:
        return (-c) / 1
    if b == 0:
        return (-c) / a

    # def f(x):
    #     return (a * x + c) / b
    #
    # argx = range(0, 100)
    # argy = []
    # for i in range(0, 100):
    #     argy.append(f(i))
