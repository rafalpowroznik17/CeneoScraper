# CeneoScraper
## Etap 1 - pobranie opinii o produkcie
- pobranie kodu pojedyńczej strony z opiniami o produkcie
- wydobycie z kody strony fragmentu odpowiadającego pojedyńczej
- zapisanie do pojedyńczych zmiennych wartości składowych opinii
- obsługa błędów
- transformacja danych do docelowych typów

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|
|Opinia|div.js_product-review|opinion|bs4.element.Tag|
|Identyfikator opinii|["data-entry-id"]|opinionId|str|
|Autor|span.user-post__author-name|author|str|
|Rekomendacja|span.user-post__author-recomendation >  em|rcmd|bool|
|Liczba gwiazdek|span.user-post__score-count|stars|float|
|Treść opinii|div.user-post__text|content|str|
|Lista zalet|div[class*="positives"] ~ div.review-feature__item|pros|list|
|Lista wad|div[class*="negatives"] ~ div.review-feature__item|cons|list|
|Czy potwierdzona zakupem|div.review-pz|purchased|bool|
|Data wystawienia|span.user-post__published > time:nth-child(1)["datetime"]|publishDate|str|
|Data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchaseDate|str|
|Dla ilu osób przydatna|span[id^="votes-yes"]|useful|int|
|Dla ilu osób nieprzydatna|span[id^="votes-no"]|useless|int|

## Etap 2 - Ekstrakcja wszystkich opinii o produkcie z pojedynczej strony.
- utworzenie słownika do przechowywania wszystkich składowych pojedyńczej opinii
- utworzenie listy, do której będą dodawane słowniki reprezentujące pojedyńcze opinie
- dodanie pętli, w której pobierane były składowe kolejnych opinii z pojedyńczej strony

## Etap 3 - Ekstracja wszsystkich opinii o produkcie ze wszystkich stron.
- dodanie pętli, w której:
    * pobierana jest strona z opiniami
    * dla każdej opinii na stronie pobierane są jej składowe
    * sprawdzane jest, czy istnieje kolejna strona z opiniami, które powinny zostać pobrane
- zapisanie wszystkich opinii o produkcie do pliku .json

## Etap 4 - Refaktoryzacja kodu
- parametryzacja identyfikatora opinii