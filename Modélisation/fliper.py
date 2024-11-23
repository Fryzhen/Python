import math
from random import random

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import matshow

from Crypto.cesar2 import maths

# PARTIE 1
# Equation paramétrée du cercle B de centre C (xC ; yC) et de rayon r
BX = np.sin(np.linspace(0, 2 * np.pi, 101))
BY = np.cos(np.linspace(0, 2 * np.pi, 101))

plt.plot(BX, BY)
plt.show()

# PARTIE 2


# Annimation d'un carré
dt = 0.01
nImage = 100

x = np.array([0, 1, 1, 0, 0])
y = np.array([0, 0, 1, 1, 0])

for i in range(nImage):
    if i == 0:
        line, = plt.plot(x, y)
        plt.axis([-1, 10, -1, 10])
    else:
        x = x + 0.1
        y = y + 0.1
        line.set_data(x, y)
    plt.pause(dt)


# Annimation d'un cercle
dt = 0.01
nImage = 100

r = 0.1 # Rayon du cercle
cX = 1 # Coordonée x du centre du cercle
cY = 1 # Coordonée y du centre du cercle
x = np.sin(np.linspace(0, 2 * np.pi, 101)) * r + cX
y = np.cos(np.linspace(0, 2 * np.pi, 101)) * r + cY

arriveeX = 10
arriveeY = 5

for i in range(nImage):
    if i == 0:
        line, = plt.plot(x, y)
        plt.axis([-1, 10, -1, 10])
    else:
        x = x + (arriveeX - cX) / nImage
        y = y + (arriveeY - cY) / nImage
        line.set_data(x, y)
    plt.pause(dt)

# PARTIE 3

dt = 0.01
r = 0.3  # Rayon du cercle
cX = 5  # Coordonnées du cercle x
cY = 5  # Coordonnées du cercle y
x = np.sin(np.linspace(0, 2 * np.pi, 101)) * r + cX
y = np.cos(np.linspace(0, 2 * np.pi, 101)) * r + cY

vitesse = 0.2
vecteurX = math.sin(math.pi / 4)
vecteurY = math.cos(math.pi / 4)

line, = plt.plot(x, y)
plt.gca().set_aspect('equal')
plt.axis([-1, 11, -1, 11])

# Limites de la zone de rebondissement
plt.plot([0, 10, 10, 0, 0], [0, 0, 10, 10, 0])

while 0 == 0:
    # Calcul de la nouvelle position du cercle
    x = x + vecteurX * vitesse
    y = y + vecteurY * vitesse

    # Calcul du centre du cercle
    cX = cX + vecteurX * vitesse
    cY = cY + vecteurY * vitesse

    line.set_data(x, y)
    plt.pause(dt)

    # Rebondissement sur les murs
    if cX <= 0 + r or cX >= 10 - r:
        vecteurX = -vecteurX
        print(vecteurX, vecteurY)

    if cY <= 0 + r or cY >= 10 - r:
        vecteurY = -vecteurY
        print(vecteurX, vecteurY)

# PARTIE 4

dt = 0.01
r = 0.3  # Rayon du cercle
cX = 5  # Coordonnées du cercle x
cY = 5  # Coordonnées du cercle y
x = np.sin(np.linspace(0, 2 * np.pi, 101)) * r + cX
y = np.cos(np.linspace(0, 2 * np.pi, 101)) * r + cY

vitesse = 0.2
vecteurX = math.sin(math.pi / 4)
vecteurY = math.cos(math.pi / 4)

line, = plt.plot(x, y)
plt.gca().set_aspect('equal')
plt.axis([-1, 11, -1, 11])

# Limites de la zone de rebondissement
plt.plot([0, 10, 10, 0, 0], [0, 0, 10, 10, 0])

# Obstacle en cercle de rayon 2 et de centre (3, 3)
obsX_1 = 3
obsY_1 = 4
obsR_1 = 2
plt.plot(np.sin(np.linspace(0, 2 * np.pi, 101)) * obsR_1 + obsX_1, np.cos(np.linspace(0, 2 * np.pi, 101)) * obsR_1 + obsY_1)

# Obstacle en cercle de rayon 2 et de centre (3, 3)
obsX_2 = 7
obsY_2 = 8
obsR_2 = 1.5
plt.plot(np.sin(np.linspace(0, 2 * np.pi, 101)) * obsR_2 + obsX_2, np.cos(np.linspace(0, 2 * np.pi, 101)) * obsR_2 + obsY_2)

while 0 == 0:
    # Calcul de la nouvelle position du cercle
    x = x + vecteurX * vitesse
    y = y + vecteurY * vitesse

    # Calcul du centre du cercle
    cX = cX + vecteurX * vitesse
    cY = cY + vecteurY * vitesse

    line.set_data(x, y)
    plt.pause(dt)

    # Rebondissement sur les murs
    if cX <= 0 + r or cX >= 10 - r:
        vecteurX = -vecteurX
        print(vecteurX, vecteurY)

    if cY <= 0 + r or cY >= 10 - r:
        vecteurY = -vecteurY
        print(vecteurX, vecteurY)


    # Rebondissement sur le cercle
    if (obsX_1 - cX) ** 2 + (obsY_1 - cY) ** 2 <= (obsR_1 + r) ** 2:
        # Calcul de la normale au cercle
        normaleX = cX - obsX_1
        normaleY = cY - obsY_1
        norme = math.sqrt(normaleX ** 2 + normaleY ** 2)
        normaleX = normaleX / norme
        normaleY = normaleY / norme

        # Calcul de la nouvelle vitesse
        produitScalaire = vecteurX * normaleX + vecteurY * normaleY
        vecteurX = vecteurX - 2 * produitScalaire * normaleX
        vecteurY = vecteurY - 2 * produitScalaire * normaleY
        print(vecteurX, vecteurY)

    # Rebondissement sur le cercle
    if (obsX_2 - cX) ** 2 + (obsY_2 - cY) ** 2 <= (obsR_2 + r) ** 2:
        # Calcul de la normale au cercle
        normaleX = cX - obsX_2
        normaleY = cY - obsY_2
        norme = math.sqrt(normaleX ** 2 + normaleY ** 2)
        normaleX = normaleX / norme
        normaleY = normaleY / norme

        # Calcul de la nouvelle vitesse
        produitScalaire = vecteurX * normaleX + vecteurY * normaleY
        vecteurX = vecteurX - 2 * produitScalaire * normaleX
        vecteurY = vecteurY - 2 * produitScalaire * normaleY
        print(vecteurX, vecteurY)


# PARTIE 5 Ajout d'une vitesse variable et d'une vitesse maximale

dt = 0.01
r = 0.2  # Rayon du cercle
cX = 5  # Coordonnées du cercle x
cY = 5  # Coordonnées du cercle y
x = np.sin(np.linspace(0, 2 * np.pi, 101)) * r + cX
y = np.cos(np.linspace(0, 2 * np.pi, 101)) * r + cY

vitesse = 0.2
vitesseMax = 0.4
vecteurX = math.sin(math.pi / 4)
vecteurY = math.cos(math.pi / 4)

line, = plt.plot(x, y)
plt.gca().set_aspect('equal')
plt.axis([-1, 11, -1, 11])

# Limites de la zone de rebondissement
plt.plot([0, 10, 10, 0, 0], [0, 0, 10, 10, 0])

# Obstacle en cercle de rayon 2 et de centre (3, 3)
obsX_1 = 3
obsY_1 = 4
obsR_1 = 2
plt.plot(np.sin(np.linspace(0, 2 * np.pi, 101)) * obsR_1 + obsX_1, np.cos(np.linspace(0, 2 * np.pi, 101)) * obsR_1 + obsY_1)

# Obstacle en cercle de rayon 2 et de centre (3, 3)
obsX_2 = 7
obsY_2 = 8
obsR_2 = 1.5
plt.plot(np.sin(np.linspace(0, 2 * np.pi, 101)) * obsR_2 + obsX_2, np.cos(np.linspace(0, 2 * np.pi, 101)) * obsR_2 + obsY_2)

while 0 == 0:
    vitesse = vitesse * 0.99
    # Calcul de la nouvelle position du cercle
    x = x + vecteurX * vitesse
    y = y + vecteurY * vitesse

    # Calcul du centre du cercle
    cX = cX + vecteurX * vitesse
    cY = cY + vecteurY * vitesse

    line.set_data(x, y)
    plt.pause(dt)

    # Rebondissement sur les murs
    if cX <= 0 + r or cX >= 10 - r:
        vecteurX = -vecteurX
        print(vecteurX, vecteurY)

    if cY <= 0 + r or cY >= 10 - r:
        vecteurY = -vecteurY
        print(vecteurX, vecteurY)


    # Rebondissement sur le cercle
    if (obsX_1 - cX) ** 2 + (obsY_1 - cY) ** 2 <= (obsR_1 + r) ** 2:
        vitesse = vitesse * 2 + 0.1
        if vitesse > vitesseMax :
            vitesse = vitesseMax
        # Calcul de la normale au cercle
        normaleX = cX - obsX_1
        normaleY = cY - obsY_1
        norme = math.sqrt(normaleX ** 2 + normaleY ** 2)
        normaleX = normaleX / norme
        normaleY = normaleY / norme

        # Calcul de la nouvelle vitesse
        produitScalaire = vecteurX * normaleX + vecteurY * normaleY
        vecteurX = vecteurX - 2 * produitScalaire * normaleX
        vecteurY = vecteurY - 2 * produitScalaire * normaleY
        print(vecteurX, vecteurY)

    # Rebondissement sur le cercle
    if (obsX_2 - cX) ** 2 + (obsY_2 - cY) ** 2 <= (obsR_2 + r) ** 2:
        vitesse = vitesse * 2 + 0.1
        if vitesse > vitesseMax :
            vitesse = vitesseMax
        # Calcul de la normale au cercle
        normaleX = cX - obsX_2
        normaleY = cY - obsY_2
        norme = math.sqrt(normaleX ** 2 + normaleY ** 2)
        normaleX = normaleX / norme
        normaleY = normaleY / norme

        # Calcul de la nouvelle vitesse
        produitScalaire = vecteurX * normaleX + vecteurY * normaleY
        vecteurX = vecteurX - 2 * produitScalaire * normaleX
        vecteurY = vecteurY - 2 * produitScalaire * normaleY
        print(vecteurX, vecteurY)