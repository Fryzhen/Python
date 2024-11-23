import requests


def get_money(level):
    tot = 0
    for i in range(0, level):
        tot += pow(10 * i, 2) / 80
    return tot


def main():
    playerlist = requests.get('http://api.laboulangerie.net/player').json()

    classementgen = []
    stringgen = "Classement Général par xp\n\n"
    i = 0

    for player in playerlist:

        playerinfo = requests.get('http://api.laboulangerie.net/player/' + (player["name"]))
        i += 1

        if playerinfo.status_code == 200:
            playerinfo = playerinfo.json()
            classementgen.append((
                (playerinfo["firstPlayed"]),
                (playerinfo["name"]),
                (int(playerinfo["mmo"]["talents"][0]["xp"]) +
                 int(playerinfo["mmo"]["talents"][1]["xp"]) +
                 int(playerinfo["mmo"]["talents"][2]["xp"]) +
                 int(playerinfo["mmo"]["talents"][3]["xp"])),
                round(get_money(playerinfo["mmo"]["talents"][0]["level"]) +
                      get_money(playerinfo["mmo"]["talents"][1]["level"]) +
                      get_money(playerinfo["mmo"]["talents"][2]["level"]) +
                      get_money(playerinfo["mmo"]["talents"][3]["level"])),
                (playerinfo["mmo"]["palier"]),
                (playerinfo["mmo"]["talents"][0]["level"]),
                (playerinfo["mmo"]["talents"][1]["level"]),
                (playerinfo["mmo"]["talents"][2]["level"]),
                (playerinfo["mmo"]["talents"][3]["level"])))

        print(round(i / len(playerlist) * 100, 2), " %")

    classementgen = sorted(classementgen)

    for i in range(len(classementgen)):
        stringgen += str(classementgen[i][1]) + " "
        stringgen += str(classementgen[i][2]) + " "
        stringgen += str(classementgen[i][3]) + " "
        stringgen += str(classementgen[i][4]) + " "
        stringgen += str(classementgen[i][5]) + " "
        stringgen += str(classementgen[i][6]) + " "
        stringgen += str(classementgen[i][7]) + " "
        stringgen += str(classementgen[i][8]) + "\n"

    gentxt = open("classementgen.txt", "w")
    gentxt.writelines(stringgen)
    gentxt.close()


if __name__ == "__main__":
    main()
