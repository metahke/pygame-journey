## NEXT
- przerzucić enemy na klasę
- poprawienie kolizji player z enemy


## POPRAWKI
- przy zmienianiu kierunku ruchu postać powinna od razu zmieniać animację, a nie czekać na zmianę okresu czasu is_walking
- dodanie animacji chodzenia po skosie?
- dodanie tekstury tła
- jak się powoli idzie w dół i zatrzymuje, to po pewnym czasie wyskakuje błąd
- trzymanie na raz strzałek lewa/prawa i góra/dół sprawia, że postać i tak chodzi
- odliczanie czasu, np. 30 sekund
- celem jest zdobycie jak najlepszej liczby punktów
- gra pamięta poprzednią najlepszą punktację


## player.py


## DONE

### 26/09/2024
- refaktoryzacja kodu, poprawienie zarządzania sprite'ami (uproszczenie logiki)

### 25/09/2024
- oddzielić player_data (state i sprites) od kodu głównego

### do 24/09/2024
- refaktoryzacja kodu i ogólne poprawienie elementów, zbudowanie gry, zmiana player na klasę
