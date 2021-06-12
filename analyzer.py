from os import listdir
from matplotlib import show as plt
import pandas as pd


def convert_stars(stars):
    return float(stars.split("/")[0].replace(",","."))


pd.set_option("display.max_columns", None)

print(*[file_name.split(".")[0] for file_name in listdir("reviews")], sep="\n")
product_id=input("Podaj identyfikator produktu: ")

reviews = pd.read_json(f"reviews/{product_id}.json")

reviews.stars = reviews.stars.map (lambda stars : float(stars.split("/")[0].replace(",",".")))

reviews_count = len(reviews.index)
#reviews_count = reviews.review_id.count()
#reviews_count = reviews.["review_id"].count()
#reviews_count = reviews.shape[0]
pros_count = reviews.pros.astype(bool).sum() #tylko nazwa typu danych
#pros_count = reviews.pros.map(bool).sum()
#pros_count = reviews.pros.apply(bool).sum()
cons_count = reviews.cons.astype(bool).sum()
avarage_score= reviews.stars.mean().round(2)

stars = reviews.stars.value_counts(dropna= False).reindex(np.arange(0,5.01,0.5),fill_value=0)
stars.plot.bar(color="red") #można podać również jako # ale nie wszystkie programyt to ogarną
plt.title ("Gwiazdki")
plt.xlabel ("Liczba gwiazdek")
plt.ylabel ("Liczba opinii")
plt.savefig(f"plots/{product_id}.png")
plt.close()