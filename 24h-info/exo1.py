# lire le fichier 1.1
fichier = open("1-1.txt", "r")
contenu = fichier.readlines()
fichier.close()
print(contenu)

points = []
for line in contenu:
    points.append(line.split())

tab = {}
for point in points:
    if point[0] not in tab:
        tab[point[0]] = 1
    else:
        tab[point[0]] += 1

    if point[1] not in tab:
        tab[point[1]] = 1
    else:
        tab[point[1]] += 1

print(tab)


