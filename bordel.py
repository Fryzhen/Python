# import math.plotlib as plt
#
# # n = 92749999275009
# #
# # start = 10
# #
# # # n modulo  26^start
# alph = [chr(i) for i in range(65, 91)]
# while n > 0:
#     print(alph[n//(26**start)], n//(26**start) , n)
#     n = n % 26**start
#     start -= 1
#
#     IEGXZD


def multiply_matrices_modulo(A, B, mod):
    # Vérifier si les matrices peuvent être multipliées
    if len(A[0]) != len(B):
        raise ValueError(
            "Le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième matrice.")

    # Initialiser la matrice résultat avec des zéros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Effectuer la multiplication et appliquer le modulo
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod

    return result


def tln(lettre):
    if lettre.isalpha() and len(lettre) == 1:
        lettre = lettre.upper()
        return ord(lettre) - ord('A')
    else:
        return "L'entrée n'est pas une lettre de l'alphabet."


def lettre2chiffre(a, b):
    return 26 * tln(a) + tln(b)


# print(lettre2chiffre('T','U'))


def tnl(nombre):
    return chr(nombre + ord('A'))


def chiffre2lettre(n):
    a = n // 26
    b = n % 26
    return tnl(a) + tnl(b)


# # Séparer les lettres par groupes de 2
# code = "ZYSHTEDDAOWZQCBUADFRSILXZSDIQQAVOWTBUAIA"
# code = [code[i:i + 2] for i in range(0, len(code), 2)]
# code = [[lettre2chiffre(i[0], i[1])] for i in code]

# def chiffre3lettre(n):
#     a = n // (26 ** 2)
#     b = (n % 26 ** 2) // 26
#     c = n % 26
#     return tnl(a) + tnl(b) + tnl(c)
#
#
# def lettre3chiffre(a, b, c):
#     return ((26 ** 2) * tln(a)) + (26 * tln(b)) + tln(c)
#
#
# code = "MCDSBPTYNXXKKSJVDUZUGRJFVGYPBDOIUFWT"
# code = [code[i:i + 3] for i in range(0, len(code), 3)]
# code = [lettre3chiffre(i[0], i[1], i[2]) for i in code]

# decrypt = code.pop(0)
# for a in range(0, 675):
#     print(a)
#     for b in range(0, 675):
#         mat = [[a, b]]
#         if multiply_matrices_modulo(mat, decrypt, 676) == [[326]]:
#             for c in range(0, 675):
#                 for d in range(0, 675):
#                     mat2 = [[c, d]]
#                     if (a * d - b * c) % 676 != 0:
#                         if multiply_matrices_modulo(mat2, decrypt, 676) == [[221]]:
#                             clef = [[a, b], [c, d]]
#                             mot = "MOIN"
#                             for duoCode in code:
#                                 out = multiply_matrices_modulo(clef, duoCode, 676)
#                                 mot += chiffre2lettre(out[0][0]) + chiffre2lettre(out[1][0])
#                             if mot[4] == "S":
#                                 nombres = ["UN", "DEUX", "TROIS", "QUATRE", "CINQ", "SIX", "SEPT", "HUIT", "NEUF", "DIX", "ONZE", "DOUZE", "TREIZE", "QUATORZE", "QUINZE", "SEIZE", "VINGT", "TRENTE", "QUARANTE", "CINQUANTE", "SOIXANTE", "CENT", "MILLE"]
#                                 count = 0
#                                 for nombre in nombres:
#                                     if nombre in mot:
#                                         count += 1
#                                 if count >= 2:
#                                     print(mot)
def chiffre3lettre(n):
    a = n // (26 ** 2)
    b = (n % 26 ** 2) // 26
    c = n % 26
    return tnl(a) + tnl(b) + tnl(c)


def lettre3chiffre(a, b, c):
    return ((26 ** 2) * tln(a)) + (26 * tln(b)) + tln(c)


code = "MCDSBPTYNXXKKSJVDUZUGRJFVGYPBDOIUFWT"
code = [code[i:i + 3] for i in range(0, len(code), 3)]
code = [lettre3chiffre(i[0], i[1], i[2]) for i in code]
#
# code = [code[i:i + 2] for i in range(0, len(code), 2)]
# code = [lettre2chiffre(i[0], i[1]) for i in code]
for a in range(1, 26 ** 3):
    print(a, end=" ")
    for b in range(0, 26 ** 3):
        mot = ""
        try:
            aprime = pow(a, -1, mod=(26 ** 3))
            for index in range(len(code)):
                code[index] = code[index] - b
                code[index] = (aprime * code[index]) % (26 ** 3)
                mot += chiffre3lettre(code[index])
            count = 0
            nombres = ["UN", "DEUX", "TROIS", "QUATRE", "CINQ", "SIX", "SEPT", "HUIT", "NEUF", "DIX", "ONZE", "DOUZE",
                       "TREIZE", "QUATORZE", "QUINZE", "SEIZE", "VINGT", "TRENTE", "QUARANTE", "CINQUANTE", "SOIXANTE",
                       "CENT", "MILL"]
            for nombre in nombres:
                if nombre in mot:
                    count += 1
            if count >= 3:
                print(mot)
        except:
            pass
