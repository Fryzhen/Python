import time
from collections import OrderedDict
import requests as requests


def get_argent_villes_nations(temp):
    strmoney = ""
    pourcentage = 0

    dictville = {}
    dictnation = {}
    dictmort = {}

    towns = requests.get("http://api.laboulangerie.net/town").json()
    nations = requests.get("http://api.laboulangerie.net/nation").json()

    for t in towns:
        time.sleep(temp)
        if len(t) == 2:
            ville = requests.get("http://api.laboulangerie.net/town/" + t["name"]).json()
            dictville[t['name'].capitalize()] = ville['balance']
            dictmort[round(ville['balance'] / (3 * len(ville['townBlocks'])) - 0.5)] = t['name'].capitalize()

            pourcentage += 1 / len(towns)
            print("Argent Villes :", round(pourcentage * 100, 2), "%")

    for n in nations:
        time.sleep(1)
        pourcentage = 0
        nation = requests.get("http://api.laboulangerie.net/nation/" + n['name']).json()
        sum = nation['balance']
        for t in nation['towns']:
            sum += dictville[t['name'].capitalize()]
        dictnation[n['name'].capitalize()] = sum

        pourcentage += 1 / len(nations)
        print("Argent Nations :", round(pourcentage * 100, 2), "%")

    dictville = OrderedDict(sorted(dictville.items()))
    dictnation = OrderedDict(sorted(dictnation.items()))

    strmoney += "\n|Villes|\n\n"
    for v in dictville:
        strmoney += str(v) + " "
        strmoney += str(dictville[v]) + "\n"



    strmoney += "\n|Nations|\n\n"
    for n in dictnation:
        strmoney += str(n) + " "
        strmoney += str(dictnation[n]) + "\n"

    return strmoney


if __name__ == "__main__":
    print(get_argent_villes_nations(0))
