## Opis
Program służy do rozwiązywania mnożenia macierzy Toeplitza przez wektor w czas O(n*logn)

## Główny program
Mnożenie jest zrealizowane w pliku `main.py`. Przyjmuje on na wejście adres do pliku zawierającego macierze Toeplitza i wektory, przez które należy je pomnożyć.

Przykładowe pliki znajdują się w folderze `data`

## Generator plików wejściowych

Do rozwiązania jest załączony generator plików wejściowych `generator.py`

Na wejściu przyjmuje następującą listę argumentów
- *count*: liczba przypadków testowych
- *size*: rozmiar macierzy Toeplitza i wektora
- *min*: minimalna wartość w generowanych 
- *max*: maksymalna wartość w generowanych danych
- *filename*: adres do ścieżki do zapisywanego pliku
- *seed*: ziarno generatora liczb losowych1

