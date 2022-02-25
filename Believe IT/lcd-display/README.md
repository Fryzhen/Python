# Affichage LCD

## Méthode

- Copiez ces fichiers sur votre poste de travail: `main.py/js`, `README.md`
- Commentez votre code et accordez une attention particulière à la lisibilité et à la présentation
- Versionnez votre code
- Utilisez extensivement `print()` et `console.log()`
- Exécutez régulièrement votre code:

```
    $ node main.py  // Python
    $ node main.js  // Javascript
```

## Objectifs

L'objectif de cet exercice est de créer la logique pour afficher des numéros sur un écran LCD.

Cet écran dispose d’une grille de 3x3, chaque case peut contenir une espace, un tiret bas ou un pipe.  
Ci dessous les chiffres à afficher:

```
._.   ...   ._.   ._.   ...   ._.   ._.   ._.   ._.   ._.
|.|   ..|   ._|   ._|   |_|   |_.   |_.   ..|   |_|   |_|
|_|   ..|   |_.   ._|   ..|   ._|   |_|   ..|   |_|   ..|
```

Exemple d'utilisation pour 910:

```
$ ./lcd-display 910
._. ... ._.
|_| ..| |.|
..| ..| |_|
```

Contraintes:

- Le code produit doit être fonctionnel
- Le code doit être publié dans un dépot git publique
- Le programme doit être documenté par un README

## Aller plus loin

- Ajouter une aide à l'outil en ligne de commande
- Mieux gérer les erreurs en cas de nombre invalide (ex: "abcd"), afficher de meilleurs message et l'aide
- Ajouter des themes: un theme LCD, un theme unicode, un theme emoji, ...
- Faire des tests unitaires
