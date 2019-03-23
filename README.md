# projekt-AI

Projekt grupowy z zajęć Sztuczna Inteligencja, pod tytułm "Inteligentny Traktor".

**Członkowie Grupy: **

- Michał Mruk
- Norbert Walczak
- Paweł Butkiewicz
- Phillip Ławniczak

## Opis projektu

Zadaniem inteligentnego traktora jest uprawa pola. Traktor powinien po nim nawigować, sprawdzać stan ziemi, zboża i wykonywać odpowiednie operacje na każdym z nich. 

## Pod projekty

Krytyczne punkty projektu, ich opisy oraz osoby odpowiedzialne.

### Interface

Zaprojektowanie i implementacja interfejsu aplikacji. Jak będzie wyglądała interakcja z programem? Ustawienia itp. 

### Środowisko/Pole/Rzeczywistość po jakim będzie się poruszał traktor

Zaimplementować "środowisko", w którym będzie żył nasz agent. Ustalić co agent będzie mógł analizować i jakie mogą być możliwe stany analizowanych obiektów.

### Agent: Traktor

Implementacja agenta (traktora), który będzie się poruszał po polu i wykonywał odpowiednie czynnośći na konkretnych zbożach. Trzeba przeanalizować jakie akcje może wykonywać traktor w stosunku do stanów pola. Ustalić jego cel, sensory i efektory.

## Standarty kodu

Projekt będzie pisany w Python (wersji 3). W tej sekcji należy podać jeszcze wykorzystywane biblioteki, umieścić przydatne linki i mini tutoriale odnośnie pracy w projekcie. 

## Praca z GitHub

### Podstawowe Info

Każdy z członków grupy jest dodany do repozytorium jako 'Collaborator', co oznacza że nie należy forkować tego repozytorium, lecz bezpośrednio je klonować do siebie na maszyne lokalną. 

```master``` zawiera wersje projektu 'ready to deploy', czyli aktualnie działającą i stabilną wersje. Sub-brach ```dev``` zawiera aktualnie rozwijaną wersję projektu, która powinna być z reguły funkcjonalna.
Każdy nowy branch jest tworzony od ```dev```. Te tak zwane feature branche powinny być tworzone w celu zaimplementowania konkretnej jednej funkcji/zmiany. 

Podstawowy schemat Git Flow w tym projekcie:
1. Zastanawiamy się nad zmianą jaką chcemy wprowadić do projektu.
2. Tworzymy sub-branch od ```dev``` o nazwie ```kolabolator-nazwa-zmiany```
3. Gdy dokonamy wszytskich zmian, pushujemy brancha na zdalne repozytorium 
4. Po pushu wykonujemy pull-request do dev
5. Admin repozytorium zatwierdza zmiany lub je odrzuca i daje odpowiedni komentarz.
6. Jeżeli branch zostaje zatwierdzony, zostanie zmergowany z ```dev``` i usunięty. W przeciwnym wypadku wróc do kroku 3.

### Szczegułowe info

Tu będą znajdować się wszytskie polecenia potrzebne do pracy z projektem wraz z wytłumaczeniami.
