
def syracuse(k):
    liste=[k]
    while k != 1:
        if k % 2 == 0:
            k = k/2
            liste.append(k)
        else:
            k=3*k+1
            liste.append(k)

    return liste


print(liste)
print(len(liste))

# liste.sort()
# print(liste)
