# Jeux de morpion

L'objectif de cet exercice consiste à implémenter le jeu [morpion](https://www.google.com/search?q=tic+tac+toe), avec une taille de grille de 3x3.

Nous allons imprimer la grille sur le terminal, comme les suivantes, avec les pions en lettre majuscule 'X' et 'O'. Ex :
 
``` javascript
// vide       // remplie
  1 2 3          1 2 3
1|_|_|_|       1|_|X|_|
2|_|_|_|       2|O|_|_|
3|_|_|_|       3|_|_|_|
```

A chaque étape, nous demandons au joueur de saisir les coordonnées de pion à placer sous forme de 'XY'. Ex : 
```javascript
// '13' correspond à la cellue de la première à droite
  1 2 3 
1|_|_|X|
2|_|_|_|
3|_|_|_|

// '32' correspond à la cellue de la dernière ligne au milieu
  1 2 3 
1|_|_|_|
2|_|_|_|
3|_|X|_|
```

Une fois un joueur a terminé sa saisie, nous vérifions si les coordonnées saisies sont valides (pas occupées, et dans l'intervalle autorisé) : 
- si valide : on met à jour la grille
- sinon : on imprime une erreur et redemander la saisie

On vérifie ensuite si un des joueurs a gagné :
- si oui : on imprime sur l'écran un message de félicitation, et termine le jeu
- si non : on continue le jeu


**Indices**
- Pour la mise à jour de la grille suite à la saisie d'utilisateur, si une telle fonction n'existe pas dans votre langage d'implémentation pour vider l'écran, vous pourriez tout simplement ce faire à l'aide d'impression d'un ensemble de lignes blanches
