# Algorytmy i struktury danych w języku python 

Zestaw 10.

## Jak uruchomić

Wystarczy pobrać pliki pythonowe i uruchomić w dowolnym środowisku.
## Treści zadań


##### ZADANIE 10.2 (STACK)
Poprawić implementację tablicową stosu tak, aby korzystała z wyjątków w przypadku pojawienia się błędu. 
Metoda pop() ma zgłaszać błąd w przypadku pustego stosu. 
Metoda push() ma zgłaszać błąd w przypadku przepełnienia stosu. Napisać kod testujący stos.

##### ZADANIE 10.4 (QUEUE)
Poprawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek. 
Poprawić metodę put() w tablicowej implementacji kolejki, 
aby w przypadku przepełnienia kolejki zwracała wyjątek. Napisać kod testujący kolejkę.

##### ZADANIE 10.8 (RANDOMQUEUE)
Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności. Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.
```
class RandomQueue:

    def __init__(self): pass

    def insert(self, item): pass

    def remove(self): pass   # zwraca losowy element

    def is_empty(self): pass

    def is_full(self): pass

    def clear(self): pass     # czyszczenie listy
```
## Użyto

* [anaconda2019](https://www.anaconda.com/distribution/) - środowisko pythona
* [pycharm](https://www.jetbrains.com/pycharm/download/) - dependency management

## Autor

* **Paweł Jelonek** 