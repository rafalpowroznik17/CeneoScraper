import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)

print(*os.listdir("opinions"), sep="\n")
productId = input("Podaj kod produktu: ")

opinions = pd.read_json("./opinions/{}.json".format(productId))

opinions.stars = opinions.stars.apply(lambda x: float(x.split("/")[0].replace(",", ".")))
opinions.rcmd = opinions.rcmd.apply(lambda x:  "Nie mam zdania" if x is None else x)

opinionsCount = len(opinions)
prosCount = opinions.pros.astype(bool).sum()
consCount = opinions.cons.astype(bool).sum()
averageScore = opinions.stars.mean()

print(f"""O produkcie dostępnych jest {opinionsCount} opinii.
W {prosCount} opiniach podana została lista zalet produktu, a w {consCount} lista wad.
Średnia ocena produktu liczona na podstawie liczby gwiazdek w opiniach wynosi {averageScore:.1f}.""")

stars = opinions.stars.value_counts().reindex(np.arange(0, 5.5, 0.5), fill_value = 0)
stars.plot.barh(color = "lightskyblue")
plt.title("Częstość występowania poszczególnych ocen produktu w opiniach")
plt.xlabel("Liczba opinii")
plt.ylabel("Liczba gwiazdek")
plt.savefig(f"./figures/{productId}_stars.png", bbox_inches = "tight")
plt.close()

recommendations = opinions.rcmd.value_counts(dropna = False).sort_index()
recommendations.plot.pie(
    label = "",
    colors = ["lightskyblue", "crimson", "forestgreen"],
    autopct = "%1.1f%%",
    pctdistance = 1.2,
    labeldistance = 1.4
)
plt.title("Udział poszczególnych rekomendacji w ogólnej liczbie opinii")
plt.legend(bbox_to_anchor = (1.0, 1.0))
plt.savefig(f"./figures/{productId}_rcmd.png", bbox_inches = "tight")
plt.close()

stars_rcmd = pd.crosstab(opinions.stars, opinions.rcmd)
print(stars_rcmd)

""" rcmd = True if rcmd == "Polecam" else False
        stars = float(stars.split("/")[0].replace(",", "."))
        content = content.replace("\n", " ").replace("\r", " ")
        purchased = bool(purchased)
        useful = int(useful)
        useless = int(useless) """