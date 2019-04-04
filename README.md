# projekt-AI

Projekt grupowy z zajęć Sztuczna Inteligencja, pod tytułm "Inteligentny Traktor".

__Członkowie Grupy:__

- Michał Mruk
- Norbert Walczak
- Paweł Butkiewicz
- Phillip Ławniczak

## Opis projektu

Zadaniem inteligentnego traktora jest uprawa pola. Traktor powinien po nim nawigować, sprawdzać stan ziemi, zboża i wykonywać odpowiednie operacje na każdym z nich. 

## Część wspólna projektu

Nad tą częścią pracują wszyscy uczestnicy, czyli stworzenie środowiska dla agenta na podstawie wykładów ( *Techniki i narzędzia reprezentacji wiedzy*) oraz zastosowanie metod rozwiązywania problemów do planwania ruchu agenta w środowisku (*Strategie rozwiązywania problemów*)

1. Implementacja środowiska - środowiskiem jest pole, które na którym się znajdują 
2. Implementacja agenta - traktor będzie się poruszał po polu i wykonywał odpowiednie czynnośći na konkretnych uprawach. Trzeba przeanalizować jakie akcje może wykonywać traktor w stosunku do stanów pola. Ustalić jego cel, sensory i efektory.
3. Reprezentacja wiedzy
  Techniki:
  - sieci semantyczne
  - systemy ram
  - grafy konceptualne
  - logika pierwszego rzędu
  - logika klauzul/Prolog
  - zbiory rozmyte
4. Planowanie ruchu
5. Zgodność ze specyfikacją zadania
6. Bezawaryjne działanie

## Podprojekty

1. ```Michał``` Przygotowanie danych wejściowych/zbioru uczącego i testowanego
2. ```Phillip``` Poprawność implementacji/integracji opracowanej metody w projekcie
3. ```Norbert i Paweł``` Pełność i poprawnośc omówienia tematu i przygotwanie raportu

## Strategie rozwiązywania problemów
1. przeszukiwanie przestrzeni stanów (strategie niepoinformowane)
  - DFS
  - DLS
  - IDDFS 
  - BFS
  - UCS
2. przeszukiwanie przestrzeni stanów (strategie poinformowane)
  - A*
  - IDA*

## Standarty kodu

Projekt będzie pisany w Python (wersji 3). W tej sekcji należy podać jeszcze wykorzystywane biblioteki, umieścić przydatne linki i mini tutoriale odnośnie pracy w projekcie. 

## Praca z GitHub

### Podstawowe Info

Każdy z członków grupy jest dodany do repozytorium jako 'Collaborator', co oznacza że nie należy forkować tego repozytorium, lecz bezpośrednio je klonować do siebie na maszyne lokalną. 

```master``` zawiera wersje projektu 'ready to deploy', czyli aktualnie działającą i stabilną wersje. Sub-brach ```dev``` zawiera aktualnie rozwijaną wersję projektu, która powinna być z reguły funkcjonalna.
Każdy nowy branch jest tworzony od ```dev```. Te tak zwane feature branche powinny być tworzone w celu zaimplementowania konkretnej funkcji/zmiany. 

Podstawowy schemat Git Flow w tym projekcie:
1. Zastanawiamy się nad zmianą jaką chcemy wprowadić do projektu.
2. Tworzymy sub-branch od ```dev``` o nazwie ```kolabolator-nazwa-zmiany```
3. Gdy dokonamy wszytskich zmian, pushujemy brancha na zdalne repozytorium 
4. Po pushu wykonujemy pull-request do dev
5. Admin repozytorium zatwierdza zmiany lub je odrzuca i daje odpowiedni komentarz.
6. Jeżeli branch zostaje zatwierdzony, zostanie zmergowany z ```dev``` i usunięty. W przeciwnym wypadku wróc do kroku 3.

### Szczegułowe info

Tu będą znajdować się wszytskie polecenia potrzebne do pracy z projektem wraz z wytłumaczeniami.

### Ćwiczenie GitHub 4.04

0. Przed wykonaniem tych poleceń, upewnić się ze wasz git jest odpowiednio skonfigurowany i ma wasze informajce (login hasło). W razie problemów wyszukajcie git setup w necie.

1. Sklonować repozytorium.
  ```git clone <url repo>```
2. Zmienić branch ```master``` na ```dev```
  ```
  git checkout dev
  ```
  Jeżeli po wykonaniu tej operacji, dostaniecie komunikat:
  ```
  Branch 'dev' set up to track remote branch 'dev' from 'origin'. Switched to a new branch 'dev'
  ```
  To krok 3 jest zbędny. 
3. Ustawiamy ```origin/dev``` jako _upstream_ naszego lokalnego ```dev```. Dzięki temu, aby uaktualnić nasze lokalne repozytorium, wystarczy wpisać ```git pull```
  ```
  git branch --set-upstream-to=origin/dev dev
  ```
4. Tworzymy nowego feature brancha od ```dev```
  ```
  git checkout -b phillip-test-branch dev
  ```
  Tu po utworzeniu nowego feature brancha, można wykonać polecenie z kroku trzeciego, aby nasz branch śledził zmiany na dev.
5. Tworzymy plik <imię>-test.txt
6. Następnie wykonujemy git status, analizujemy zmiany, a nastepnie add i commit
  ```
  git status
  git add nazwa_pliku.txt
  git commit -m "tutaj napisac jakiś sensowny commit message"
  ```
7. Teraz możemy wykonać push całego naszego brancha
  ```
  git push origin <nazwa brancha>
  ```
8. Następnie, wchodzicie na repozytorium GitHub, szukacie zakładki z listą branchów i wykonujecie pullrequest waszego brancha. **UWAGA:** Pamiętać aby pull request był wykonany z feature brancha do ```dev```, a nie do ```master```.
9. Po wykonaniu pull requesta, czekacie na jego zatwierdzenie przez właściciela Repo.
10. Jeżeli pullrequest waszego brancha zosatanie zatwierdzony, należy go usunąć z Github (chyba że już to zrobiła osoba zatwierdzająca pull) oraz z lokalnego repozytorium.

