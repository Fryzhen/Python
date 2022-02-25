import random

moyenne = []
note = 0
notelist = []
while note != -1:
    note = input("Ecrire écrire une note puis entrer : ")
    if note != "":
        note = float(note)
        notelist.append(note)
    else:
        break

moyenne = sum(notelist)/len(notelist)
print(moyenne)

parents = 12
if moyenne < parents:
    print("je te renie")
elif parents+3 >= moyenne >= parents:
    print("pas mal mais tu dois mieux faire")
elif parents+3 < moyenne < 20:
    print("bien joué tu aura une PS5")
else:
    print("tu me ment tu est punni")

