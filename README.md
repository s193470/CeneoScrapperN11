# CeneoScrapperN11
## Etap 1 - Pobranie składowej pojedyńczej opinii z serwisu [Ceneo.pl] (https://www.ceneo.pl/)
1. Pobranie kodu pojedyńczej strony z opiniami o produkcie
2. Analiza struktóry kodu pojedyńczej opinii

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|:-------|:-----------|:-------------|:---------|
|Opinia|`div.js_product-review`|review||
|Identyfikator opinii|`["data-entry-id"]`|review_id||
|Autor opinii|`span.user-post__author-name`|author||
|Rekomendacja|`span.user-post__author-recomendation`|recommendation||
|Liczba gwiazdek|`span.user-post__score-count`|stars||
|Treść Opinii|`div.user-post__text`|content||
|Lista zalet|`iv.review-feature__col:has(> div[class*="positives"]) > div.review-feature__item`<br> `div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item`<br>`div.review-feature__title--positives ~ div.review-feature__item`|pros||
|Lista wad|`iv.review-feature__col:has(> div[class*="negatives"]) > div.review-feature__item`<br> |||`div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item`<br>`div.review-feature__title--negatives ~ div.review-feature__item`|cons||
|Dla ile osób przydatna|`span[id^="votes-yes"]`<br>`button.vote-yes["data-total-vote"]`<br>`button.vote-yes > span`|useful||
|Dla ilu osób nieprzydatnych|`span[id^="votes-no"]`<br>`button.vote-no["data-total-vote"]`<br>`button.vote-no > span`|useless||
|Czy Potwierdzona zakupem|`div.review-pz`|purchased||
|Data wystawienia opinii|`span.user-post__publish > time:nth-child(1)["datetime"]`|review_date||
|Data zakupu produktu|`span.user-post__published > time:nth-child(2)["datetime"]`|purchase_date||



