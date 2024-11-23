import requests


def main():
    string = ""
    fusion = open("stats_fusion.txt", "w")
    starttxt = open("Argent/Joueurs/2023/3/2023-03-01.txt", "r")
    for lignes in starttxt:

        fintxt = open("Argent/Joueurs/2023/3/2023-03-19-15-00.txt", "r")
        for lignef in fintxt:

            tabs = lignes.split()
            tabf = lignef.split()
            if tabs[0] == tabf[0]:
                string += tabs[0] + " "
                for i in range(1, len(tabs)):
                    string += str(int(tabf[i]) - int(tabs[i])) + " "
                string += "\n"

    fusion.writelines(string)

    fusion.close()
    starttxt.close()
    fintxt.close()


if __name__ == "__main__":
    main()
