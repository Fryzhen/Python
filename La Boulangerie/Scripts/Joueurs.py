from datetime import datetime as dt, time
import requests as requests


def get_money(level):
    tot = 0
    for i in range(0, level+1):
        tot += pow(10 * i, 2) / 80
    return tot


def date():
    return str(dt.today())[:10] + "-" + str(dt.today())[11:16].replace(":", "-")


def get_money_total(temp):
    playerlist = requests.get('http://api.laboulangerie.net/player').json()
    pourcent = 0
    tabplayer = []

    joueur = open("./Argent/Joueurs/"
                  + str(dt.today().year) + "/"
                  + str(dt.today().month) + "/"
                  + date()
                  + ".txt", "w+")

    for player in playerlist:
        playerinfo = requests.get('http://api.laboulangerie.net/player/' + player["name"])
        pourcent += 1 / len(playerlist)
        print("Money Total :", round(pourcent * 100, 2), "%")
        if playerinfo.status_code == 200:
            playerinfo = playerinfo.json()
            if playerinfo["isOnline"]:
                joueur.write(player["name"])
                tabplayer.append((
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
                    (playerinfo["mmo"]["talents"][3]["level"])
                ))

    string = ""
    tabplayer = sorted(tabplayer)

    for p in tabplayer:
        for i in range(1, 9):
            string += str(p[i]) + " "
        string += "\n"

    return string


if __name__ == "__main__":
   print(get_money())
