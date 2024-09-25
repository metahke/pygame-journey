## NEXT
- przerzucić enemy na klasę


## POPRAWKI
- przy zmienianiu kierunku ruchu postać powinna od zmieniać animację, a nie czekać na zmianę okresu czasu is_walking
- postać, a raczej jej rectange jest o wiele większa od obrazka, który się w niej zawiera (proporcje character image?)
- dodanie animacji chodzenia po skosie?
- dodanie tekstury tła
- zamienić postać na klasę ?
- jak się powol idzie w dół i zatrzymuje, to po pewnym czasie wyskakuje błąd
- trzymanie na raz strzałek lewa/prawa i góra/dół sprawia, że postać i tak chodzi
- odliczanie czasu, np. 30 sekund
- celem jest zdobycie jak najlepszej liczby punktów
- gra pamięta poprzednią najlepszą punktację


## player.py
- dodać metodę typu "switch" pozwalającą na zmianę stanu ruchu, np. player.switch_movement() (?)
- self.is_walking i self.position w zamyśle spełnia tę samą funkcję: idle/False oraz walk/True
- może jak się idzie do góry i w dół to animacji nie widać


## DONE

### 25/09/2024
- oddzielić player_data (state i sprites) od kodu głównego

### do 24/09/2024
- refaktoryzacja kodu i ogólne poprawienie elementów, zbudowanie gry
