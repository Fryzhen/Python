import requests


def get_money(level):
    tot = 0
    for i in range(0, level):
        tot += pow(10 * i, 2) / 80
    return tot


def main():
    listville = requests.get("http://api.laboulangerie.net/town").json()
    villeask = input("Ville recherché : ")
    i = 0
    somme = 0

    while villeask != listville[i]["name"]:
        i += 1
        if len(listville) == i:
            i = 0
            villeask = input("Ville inconu \nVille recherché : ")

    ville = requests.get("http://api.laboulangerie.net/town/" + villeask).json()

    for resident in ville["residents"]:
        residentinfo = requests.get("http://api.laboulangerie.net/player/" + resident["name"])
        if residentinfo.status_code == 200:
            residentinfo = residentinfo.json()
            somme += round(get_money(residentinfo["mmo"]["talents"][0]["level"]) +
                           get_money(residentinfo["mmo"]["talents"][1]["level"]) +
                           get_money(residentinfo["mmo"]["talents"][2]["level"]) +
                           get_money(residentinfo["mmo"]["talents"][3]["level"]))

    print(somme + ville["balance"])


if __name__ == "__main__":
    main()
