import datetime
from datetime import datetime as dt
from Scripts import Villes as m
from Scripts import Joueurs as mt


def date():
    return str(dt.today())[:10] + "-" + str(dt.today())[11:16].replace(":", "-")


def main():
    temp = 0
    start = str(dt.today())

    joueur = open("./Argent/Joueurs/"
                  + str(dt.today().year) + "/"
                  + str(dt.today().month) + "/"
                  + date()
                  + ".txt", "w+")
    ville = open("./Argent/Villes/"
                 + str(dt.today().year) + "/"
                 + str(dt.today().month) + "/"
                 + date()
                 + ".txt", "w+")

    joueurs = mt.get_money_total(temp)
    joueur.writelines(joueurs)
    joueur.close()

    villes = m.get_argent_villes_nations(temp) + "\n"

    fin = str(dt.today()) + "\n"

    ville.writelines(start + fin + villes)
    ville.close()

if __name__ == "__main__":
    main()
