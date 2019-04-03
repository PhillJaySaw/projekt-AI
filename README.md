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
