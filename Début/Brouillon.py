import random

x = int(input("quelle suite : "))

restants = [1]
for k in range(2,x+1):
    restants.append(k)
print(restants)


for i in range(18, 19):
    print(i)
    restants = [1]
    for k in range(2, x + 1):
        restants.append(k)
    random.shuffle(restants)
    print(restants)
    liste = [i]
    restants.remove(i)
    y = 0
    while len(liste) != x:
        last = liste[-1]
        racine = ((restants[y] + last)**0.5) % 1 #regarde si la somme est un carré
        if racine == 0:
            liste.append(restants[y])
            restants.pop(y)
            print(liste)
            y = 0
            if len(liste) == x:
                print(liste)
                exit()
        else:
            y += 1
            if len(restants) == y:
                break
