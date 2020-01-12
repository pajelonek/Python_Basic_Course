## Fibonacci Heap[PYTHON]

## Opis
Kopiec Fibonacciego to struktura danych realizująca operacje kolejki priorytetowej, składająca się z kolekcji drzew z porządkiem kopcowym. Kopce te mają lepszy czas zamortyzowany, niż wiele innych implementacji kolejek priorytetowych, w tym kopce binarne i dwumianowe. Michael L. Friedman i Robert E. Tarjan odkryli kopce Fibonacciego w 1984 roku i opublikowali ich opis w czasopiśmie naukowym w 1987 roku. Nazwali je kopcami Fibonacciego w nawiązaniu do liczb Fibonacciego, które są używane do ich analizy.
Dla kopców Fibonacciego operacja znalezienia minimum zajmuje czas stały (O(1)) w sensie zamortyzowanym, podobnie jak operacje wstawiania oraz zmniejszania klucza. Usuwanie elementu działa w czasie zamortyzowanym O(log n), gdzie n to rozmiar stosu. Oznacza to, że zaczynając od pustej struktury, dowolny ciąg a operacji wstawiania oraz zmniejszania kluczy i b operacji usunięć zajmie O(a + b log n) czasu (najgorszy przypadek), gdzie n to maksymalny rozmiar kopca. Taki sam ciąg operacji w kopcu dwumianowym miałby złożoność O((a + b) log n ) Możliwa jest także operacja łączenia dwóch kopców Fibonacciego w stałym czasie (zamortyzowanym).

Średnia złożoność w notacji duże O:
+ Push		    Θ(1)
+ Top		  Θ(1)
+ Pop		Θ(log n)	 
+ Decrease-key	Θ(log n)	 


Dokumentacja: https://www.cs.princeton.edu/~wayne/teaching/fibonacci-heap.pdf

## Opis operacji
+ Push(x) - Do naszej kolejki priorytetowej wsadzamy nowego node'a z kluczem x.
+ Top() - Dostajemy wartosc minimum z kolejki nic nie zmienajac. 
+ Pop() - Zwracamy wartość minimum jednocześnie usuwając je z kolejki i przeprowadzając konsolidacje drzewa.
+ Decrease_key(stary_klucz, nowy_klucz): Zakładąc w tej implementacji, że wartości kluczy node'ów się nie powtarzając to zmieniamy wartość klucza 'stary klucz' na wartość 'nowy klucz'.

## Prerekwizyty
Python 2.7

## Autor
Pawel Jelonek
