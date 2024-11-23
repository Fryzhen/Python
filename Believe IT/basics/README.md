# Bases

## Méthode

- Copiez ces fichiers sur votre poste de travail: `main.py/js`, `README.md`
- Commentez votre code et accordez une attention particulière à la lisibilité et à la présentation
- Versionnez votre code
- Utilisez extensivement `print()` et `console.log()`
- Exécutez régulièrement votre code:

```
    $ python main.py  // Python
    $ node main.js  // Javascript
```

## Objectifs

Editer `main.py/js` et écrire:

- Des variables globales
- Des variables locales à la fonction `main()`
- Une fonction d'addition utilisable de cette manière:

```
    // Deux versions possible: avec nombre de paramètres déterminé et non déterminé
    add(1, 2, 3) -> 6
```

- Une classe `SuperAddition` utilisable de cette manière:

```
    a = SuperCalculator()
    a.add(1)
    a.add(2)
    a.add(3, 4, 5)
    a.addAll([6, 7, 8])
    a.minus(6, 7, 8)
    a.minusAll([6, 7, 8])
    ....
    a.result()
```
