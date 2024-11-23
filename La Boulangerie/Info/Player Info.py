import requests


def get_money(level):
    tot = 0
    for i in range(0, level):
        tot += pow(10 * i, 2) / 80
    return tot


def main():
    listplayer = requests.get("http://api.laboulangerie.net/player").json()
    playerask = input("Joueur recherché : ")
    i = 0
    while playerask != listplayer[i]["name"]:
        i += 1
        if len(listplayer) == i:
            i = 0
            playerask = input("Joueur inconu \nJoueur recherché : ")

    player = requests.get("http://api.laboulangerie.net/player/" + playerask).json()

    print("```")
    print("Joueur     : ", playerask)
    if 'town' in player['resident']:
        print("Ville      : ", player['resident']['town']['name'])
    if 'nation' in player['resident']:
        print("Nation     : ", player['resident']['nation']['name'])

    if len(player['resident']['friends']) != 0:
        print("Amis       : ")
        for p in player['resident']['friends']:
            print("          ", p['name'])

    print("Total      : ",
          player["mmo"]["palier"],
          " " * (5 - len(str(player["mmo"]["palier"]))),
          (get_money(player["mmo"]["talents"][0]["level"]) +
           get_money(player["mmo"]["talents"][1]["level"]) +
           get_money(player["mmo"]["talents"][2]["level"]) +
           get_money(player["mmo"]["talents"][3]["level"])))

    print("Farmer     : ",
          player["mmo"]["talents"][0]["level"],
          " " * (5 - len(str(player["mmo"]["talents"][0]["level"]))),
          get_money(player["mmo"]["talents"][0]["level"]))

    print("Hunter     : ",
          player["mmo"]["talents"][1]["level"],
          " " * (5 - len(str(player["mmo"]["talents"][1]["level"]))),
          get_money(player["mmo"]["talents"][1]["level"]))

    print("Lumberjack : ",
          player["mmo"]["talents"][2]["level"],
          " " * (5 - len(str(player["mmo"]["talents"][2]["level"]))),
          get_money(player["mmo"]["talents"][2]["level"]))

    print("Miner      : ",
          player["mmo"]["talents"][3]["level"],
          " " * (5 - len(str(player["mmo"]["talents"][3]["level"]))),
          get_money(player["mmo"]["talents"][3]["level"]))
    print("```")


if __name__ == "__main__":
    print(get_money(30))
