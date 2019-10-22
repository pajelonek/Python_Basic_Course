import math


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a + b < c or a + c < b or c + b < a:
        raise ValueError("Nie spelniony warunek trojkata")
    return math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4.0


def main():
    print(heron(3, 4, 5))


if __name__ == '__main__':
    main()  # uruchamia wszystkie testy
