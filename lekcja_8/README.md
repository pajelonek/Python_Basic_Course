# Algorytmy i struktury danych w języku python 

Zestaw 8.

## Jak uruchomić

Wystarczy pobrać pliki pythonowe i uruchomić w dowolnym środowisku.
## Treści zadań


##### ZADANIE 8.1
Zbadać problem szukania rozwiązań równania liniowego postaci a * x + b * y + c = 0. Podać specyfikację problemu. Podać algorytm rozwiązania w postaci listy kroków, schematu blokowego, drzewa. Podać implementację algorytmu w Pythonie w postaci funkcji solve1(), która rozwiązania wypisuje w formie komunikatów.

```
def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    pass

```
##### ZADANIE 8.3
Obliczyć liczbę pi za pomocą algorytmu Monte Carlo. Wykorzystać losowanie punktów z kwadratu z wpisanym kołem. Sprawdzić zależność dokładności wyniku od liczby losowań. Wskazówka: Skorzystać z modułu random.
```
def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    pass

```
##### ZADANIE 8.4
Zaimplementować algorytm obliczający pole powierzchni trójkąta, jeżeli dane są trzy liczby będące długościami jego boków. Jeżeli podane liczby nie spełniają warunku trójkąta, to program ma generować wyjątek ValueError.
```
def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    pass

```
##### ZADANIE 8.6
Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j). Porównać z wersją rekurencyjną programu. Wskazówka: Wykorzystać tablicę dwuwymiarową (np. słownik) do przechowywania wartości funkcji. Wartości w tablicy wypełniać kolejno wierszami.
```
P(0, 0) = 0.5,
P(i, 0) = 0.0 dla i > 0,
P(0, j) = 1.0 dla j > 0,
P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.
```
## Użyto

* [anaconda2019](https://www.anaconda.com/distribution/) - środowisko pythona
* [pycharm](https://www.jetbrains.com/pycharm/download/) - dependency management

## Autor

* **Paweł Jelonek** 