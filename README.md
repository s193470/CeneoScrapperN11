# CeneoScrapperN11
## Etap 1 - Pobranie składowej pojedyńczej opinii z serwisu [Ceneo.pl] (https://www.ceneo.pl/)
1. Pobranie kodu pojedyńczej strony z opiniami o produkcie
2. Analiza struktóry kodu pojedyńczej opinii

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|:-------|:-----------|:-------------|:---------|
|Opinia|`div.js_product-review`|review|dict|
|Identyfikator opinii|`["data-entry-id"]`|review_id|str|
|Autor opinii|`span.user-post__author-name`|author|str|
|Rekomendacja|`span.user-post__author-recomendation`|recommendation|bool|
|Liczba gwiazdek|`span.user-post__score-count`|stars|float|
|Treść Opinii|`div.user-post__text`|content|str|
|Lista zalet|`iv.review-feature__col:has(> div[class*="positives"]) > div.review-feature__item`<br> `div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item`<br>`div.review-feature__title--positives ~ div.review-feature__item`|pros|\[str\]|
|Lista wad|`iv.review-feature__col:has(> div[class*="negatives"]) > div.review-feature__item`<br> |||`div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item`<br>`div.review-feature__title--negatives ~ div.review-feature__item`|cons|\[str\]|
|Dla ile osób przydatna|`span[id^="votes-yes"]`<br>`button.vote-yes["data-total-vote"]`<br>`button.vote-yes > span`|useful|int|
|Dla ilu osób nieprzydatnych|`span[id^="votes-no"]`<br>`button.vote-no["data-total-vote"]`<br>`button.vote-no > span`|useless|int|
|Czy Potwierdzona zakupem|`div.review-pz`|purchased|bool|
|Data wystawienia opinii|`span.user-post__publish > time:nth-child(1)["datetime"]`|review_date|str|
|Data zakupu produktu|`span.user-post__published > time:nth-child(2)["datetime"]`|purchase_date|str|

3.Pobieranie składowych opinii do pojedyńczych zmiennych

## Etap 2 - pobranie wszystkich opinii z pojedynczej strony
1. Zdezdefiniowanie s łownika do przechwywania skladowych pojedyncej opinii
2.  Zdefinowwanie listy do przechowanyania słowników z opniiamii
3. Dodanie petli wykonującej operację ekstracji na wszystkich opiniach z pojedynczej strony

## Etap 3- Pobranie wszystkich opinii o produkcie
1. Dodanie petli wykonującej operacje ekstrakcji z wszytkich stron z opiniami dla daego produktu
2. Dodanie kodu produktu z standardowego wejscia 
3. Parametryzacja adresy strony z opniiamii
4. Eksport opinii o produkcie do pliku .json

## Etap 3 - Analiza Opinii

