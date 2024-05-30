## Opis
Program służy do rozwiązywania mnożenia macierzy Toeplitza przez wektor w czas O(n*logn)

## Główny program
Mnożenie jest zrealizowane w pliku `main.py`. Przyjmuje on na wejście adres do pliku zawierającego macierze Toeplitza i wektory, przez które należy je pomnożyć.

Przykładowe pliki znajdują się w folderze `data`

Przykład wywołania
```
python3 main.py data/manual.txt
```

Przykład wyjścia
```
Multiplication result no. 1 is [ 57. 120.  92.  22.]
Multiplication result no. 2 is [ 60. 10.  44.  12.]
```

## Generator plików wejściowych

Do rozwiązania jest załączony generator plików wejściowych `generator.py`

Na wejściu przyjmuje następującą listę argumentów
- *count*: liczba przypadków testowych
- *size*: rozmiar macierzy Toeplitza i wektora
- *min*: minimalna wartość w generowanych 
- *max*: maksymalna wartość w generowanych danych
- *filename*: adres do ścieżki do zapisywanego pliku
- *seed*: ziarno generatora liczb losowych

Przykład wywołania
```
python3 generator.py 10 5 0 20 data/sample.txt 42
```
Co oznacza wygenerowanie 10 macierzy o rozmarze 5x5 i 10 wektorów, z wartościami od 0 do 20, zapisanych do pliku `data/sample.txt` z ziarnem 42.


## Testy
Do rozwiązania dołączony jest skrypt testujący `test.py`. Testuje on poprawność rozwiązania na podanym pliku. 

Przykład wywołania
```
python3 test.py data/manual.txt
```

Przykład wyjścia
```
Total time for normal multiplication: 0.00008
Total time for fast multiplication: 0.00002
Success rate: 1/1
```