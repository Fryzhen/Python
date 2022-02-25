## Symboles généraux

# _      prend le dernier calcul et le met a la place du _
# |      signifie "ou"


## Calculatrice

# x+y   addition
# x-y   soustraction
# x*y   multiplication
# x/y   division classique
# x//y  division euclidienne
# x%y   reste de la division (modulo)
# x**y  puissance


## Variables, listes et suites

# x=y                           affectation d'une valeur a une variable
# x=['a','b','c','d','e']       affecte les valeurs a,b,c,d,e a une variable x et crée une chaine de caractère
# x=[1,2,3,4,5]                 affecte les valeurs 1,2,3,4,5 a une variable x et crée une liste
#.insert(x,"y")                 insert une chaine de caractère nommé "y" à la place x
#.append("y")                   insert une chaine de caractère nommé "y" à la fin
#.pop(x)                        suprime un élément la la place x
#.remove("y")                   suprime l'élément nommé "y"
#.clear                         suprime toute la liste
#.split(":")                    crée une liste avec les éléments séparé par des ":"
#.count('x')                    compte le nombre de 'x' dans une suite
# len(x)                        donne la taille de la liste x

## Les caractères

# [:]    tous les caratcères
# [0]    prend le caractère en position 0
# [-1]   prend le dernier caratère
# [3:]   prend les caractères du début à la position 3
# [2:5]  prend les caractères de la position 2 à 5
# +[x,y] ajoute x et y a la suite
# x[y]=z remplace le caractère de la liste x en position y par z
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1


## Les symboles

#   <   plus petit que
#   >   plus grand que
#   <=  plus petit ou égal à
#   >=  plus grand ou égal à
#   ==  égal à
#   !=  non égal à


## Les conditions

# |toutes les conditions prenent ":" à la fin

# while x<100:                       # tant que a est plus petit que 100 la fonction s'execute
# if x<100:                          # si x est plus petit que 100 le fonction s'execute
# elif x<100:                        # si x est plus petit que 100 et que le précédent if ou elif est faux la fonction s'execute
# else x<100:                        # si x est plus petit que 100 et que tous les  elif et le if est faux la fonction s'execute
# for x in y:                        # x prend les valeurs de y et execute ce qui suit


## Les + de condition

# break                  # termine une boucle
# continue               # passe à la boucle suivante
# pass                   # ne sert a rien (mais permet d'indiquer que qqch manque)
# x=("a","b")[z>y]       # si z est plus grand que y alors x prend la valeur a sinon il prend la valeur b

## Les fonctions sans condition

# print("la valeur de x est",x)      # affiche "la valeur de x est'valeur de x'"
#.format(x)                          # remplace un "{}" dans un print par un x
# range(x)                           # donne des valeurs de 1 à x-1
# range(x,y)                         # donne les valeurs de x à y-1
# range(x,y,z)                       # donne les valeurs de x à y-1 avec un pas de z
# input("entrez une valeur :")       # permet de demander une valeur a l'utilisateur
# sum(x)                             # fait la somme des nombres de la liste de x


##Les Superclasse Les classes et les modules

#super().__init__(diférentes variables a apeler dans la classe parente)
# class "nom de classe"(classe parente)
# def module (variable présente dans le module):
# #globals                         # permet d'utiliser une fonciton utilisé autre part

# srt(x)                             # transforme la valeur x en une chaine de caractère
# int(x)                             # transforme la chaine de caractère en valeur x



