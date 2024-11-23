from collections import OrderedDict

import requests

dictville = {}

towns = requests.get("http://api.laboulangerie.net/town").json()
nations = requests.get("http://api.laboulangerie.net/nation").json()

for t in towns:
    if len(t) == 2:
        ville = requests.get("http://api.laboulangerie.net/town/" + t["name"]).json()
        dictville[round(ville['balance']/len(ville["residents"]))] = t['name'].capitalize()

dictville = OrderedDict(sorted(dictville.items(),reverse=True))
i = 1
for v in dictville:
    print(i, str(v), str(dictville[v]))
    i += 1
