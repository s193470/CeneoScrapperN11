# CeneoScrapperN11
## Etap 1 - Pobranie składowej pojedyńczej opinii z serwisu [Ceneo.pl] (https://www.ceneo.pl/)
1. Pobranie kodu pojedyńczej strony z opiniami o produkcie
2. Analiza struktóry kodu pojedyńczej opinii

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|:-------|:-----------|:-------------|:---------|
|Opinia|`.js_product-reviev`|tekst opinii|string|
|Identyfikator opinii|`["data-entry-id"]`||string|
|Autor opinii|`span.user-post__author-name`||string|
|Rekomendacja|`span.user-post__author-recomendation`||string|
|Liczba gwiazdek|`span.user-post__score-count`||number|
|Treść Opinii|`div.user-post__text`|||
|Lista zalet|`iv.review-feature__col:has(> div[class*="positives"]) > div.review-feature__item`<br> |||`div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item`<br>`div.review-feature__title--positives ~ div.review-feature__item`
|Lista wad|`iv.review-feature__col:has(> div[class*="negatives"]) > div.review-feature__item`<br> |||`div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item`<br>`div.review-feature__title--negatives ~ div.review-feature__item``|||
|Dla ile osób przydatna|`span[id^="votes-yes"]`<br>`button.vote-yes["data-total-vote"]`<br>`button.vote-yes > span`|||
|Dla ilu osób nieprzydatnych|`span[id^="votes-no"]`<br>`button.vote-no["data-total-vote"]`<br>`button.vote-no > span`|||
|Czy Potwierdzona zakupem|`div.review-pz`|||
|Data wystawienia opinii|`.user-post__publish`|||
|Data zakupu produktu|`.user-post__publish`|||



