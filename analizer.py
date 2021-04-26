import os
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)

print(*os.listdir("opinions"), sep="\n")
productId = input("Podaj kod produktu: ")

opinions = pd.read_json("./opinions/{}.json".format(productId))

opinions.stars = opinions.stars.apply(lambda x: float(x.split("/")[0].replace(",", ".")))
average_score = opinions.stars.mean()
#opinions.rcmd = opinions.rcmd.apply(lambda x: True if x == "Polecam" else False if x == "Nie polecam" else x)
opinions.rcmd = opinions.rcmd.apply(
    lambda x:  "Nie mam zdania" if x is None else x)

recommendations = opinions.rcmd.value_counts(dropna = False)

recommendations.plot.pie(label = "", labels = ["Polecam", "Nie mam zdania", "Nie polecam"])
plt.show()
print(opinions.rcmd)
""" rcmd = True if rcmd == "Polecam" else False
        stars = float(stars.split("/")[0].replace(",", "."))
        content = content.replace("\n", " ").replace("\r", " ")
        purchased = bool(purchased)
        useful = int(useful)
        useless = int(useless) """