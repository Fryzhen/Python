# Serveur de statistiques Github

## Doc

- Requetes HTTP: http://sdz.tdct.org/sdz/les-requetes-http.html
- Format JSON: https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/JSON
- API Http: https://practicalprogramming.fr/api-rest
- Documentation API Github: https://docs.github.com/en/rest/reference/

## Lancer le serveur

- Ouvrir powershell
- cd "C:\Users\noe34\Belive IT\github-api\python"
- .venv\Scripts\activate.bat
- $env:FLASK_APP = "main"
- python -m flask run

A caque modification du serveur:
- CTRL C + CTRL C
- python -m flask run

## Contexte

Github est une plateforme sociale pour codeurs.

Sur Github vous pouvez publier du code, partager avec d'autres codeurs et vos utilisateurs.

## Objectifs

L'objectif de cet exercice est de créer une API de mise à disposition de statistiques sur des dépôts Github.

Vous devez créer un serveur HTTP avec une route `/api/statistics/repository/$KEY` qui peut être utilisé de cette manière:

```
    // Statistiques sur le dépôt rust-lang/rust

    $ curl http://localhost:5000/api/statistics/repository/rust-lang/rust
    {
      "owner": "rust-lang",
      "repository": "rust",
      "forks": 8839,
      "stars": 63481,
      "watching": 63481
      "statistics": {
        "contributors": {
          "top10": [
            {
              "contributions": 22953,
              "login": "bors"
            },
            {
              "contributions": 5507,
              "login": "brson"
            },
           ...
          ]
        },
        "issues": {
          "totalOpen": 8377
          "top10 of newest issues": [
            {
              "comments": 413,
              "title": "Allocator traits and std::heap"
            },
            {
              "comments": 353,
              "title": "Tracking issue for `?` operator and `try` blocks (RFC 243, `question_mark` & `try_blocks` features)"
            },
            {
              "comments": 284,
              "title": "Tracking issue for promoting `!` to a type (RFC 1216)"
            },
           ...
          ]
        }
  }
}
```

Documentation:

- https://docs.github.com/en/rest

## Méthode

- Copiez ces fichiers sur votre poste de travail: `js/` ou `python/`, `README.md`
- Commentez votre code et accordez une attention particulière à la lisibilité et à la présentation
- Versionnez votre code
- Utilisez extensivement `print()` et `console.log()`
- Exécutez régulièrement votre code:

```
    // La première fois uniquement, installer les dépendances
    $ ./_install.sh

    // Démarrer le serveurs
    $ ./run.sh

    // Interroger le serveurs
    $ curl -v http://localhost:5000/api/statistics/repository/rust-lang/rust
```

## Aller plus loin

- Plus de stats sur les dépots de code
- Nouvelle route HTTP qui sert des statistiques sur les utilisateurs
- Mettre en cache les résultats pour une journée
  -> Ecrire la réponse sur disque (https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file)
  -> Lire le disque à chaque requete, vérifier si une réponse "en cache" existe, si oui la retourner
- Authentification basique: 
  -> https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Authorization
  -> Demande d'un username:password
  -> Si mauvais identifiants -> code 403
- Interface web minimaliste
  -> Index.html + requete XHR JS + un petit peu de mise en forme
  -> formulaire d'authentification
- Valider les entrées (owner, repository, ...)
- Paralléliser les requêtes HTTP
