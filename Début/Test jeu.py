
class Player :

    def __init__(self, pseudo, life, attack, defense):

        self.pseudo = pseudo
        self.life = life
        self.attack = attack
        self.defense = defense






player1 = Player("Fryzhen", 20, 3, 0)
print("Bienvenue au joueur", player1.pseudo)

player2 = Player("Kévin", 20, 3, 0)
print("Bienvenue au joueur", player2.pseudo)

