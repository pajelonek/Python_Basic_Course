# Algorytmy i struktury danych w języku python 

Zestaw 9.

## Jak uruchomić

Wystarczy pobrać pliki pythonowe i uruchomić w dowolnym środowisku.
## Treści zadań


##### ZADANIE 9.1 (SINGLELIST)
Do klasy SingleList dodać nowe metody.

```
class SingleList:
# ... inne metody ...

    def remove_tail(self): pass   # klasy O(N)
    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.

    def merge(self, other): pass   # klasy O(1)
    # Węzły z listy other są przepinane do listy self na jej koniec.

    def clear(self): pass     # czyszczenie listy
```
##### ZADANIE 9.7 (BINARYSEARCHTREE)
Dla drzewa BST napisać funkcje znajdujące największy i najmniejszy element przechowywany w drzewie. Mamy łącze do korzenia, nie ma klasy BinarySearchTree. Drzewo BST nie jest modyfikowane, a zwracana jest znaleziona wartość (węzeł). 
W przypadku pustego drzewa należy wyzwolić wyjątek ValueError.```
Załóżmy, że drzewo binarne przechowuje liczby. Napisać funkcję calc_total(top), która podaje sumę liczb przechowywanych w drzewie.
```
def bst_max(top): pass

def bst_min(top): pass
```
## Użyto

* [anaconda2019](https://www.anaconda.com/distribution/) - środowisko pythona
* [pycharm](https://www.jetbrains.com/pycharm/download/) - dependency management

## Autor

* **Paweł Jelonek** 