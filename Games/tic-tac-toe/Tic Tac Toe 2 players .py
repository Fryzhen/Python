import pygame
import tkinter as tk

global player_turn, line, clear, number_of_players
global x_center, x_side, x_corner, o_center, o_side, o_corner, center, side, corner, xplays, oplays
global lengh, lengh_2, lengh_max

#    _____
#   //___\\ _
#  /_|_|_|_('>
#    "   "
#   Tortue

"""""
Multijoueurs

1) afficher la grille
2) demander la position au joueur 1/2
3) vérifier si la position est libre ou non
4) vérifier si le joueur 1/2 a gagné
5) vérifier si il reste des places de libre
6) Changer de joueur
"""""


def setup():
    global player_turn, line, clear, number_of_players
    global lengh, lengh_2, lengh_max, surf, run

    lengh = 200
    lengh_2 = lengh * 2 + 3
    lengh_max = lengh * 3 + 6

    clear = "\n" * 100
    line = "\n  1 2 3           \n1|_|_|_|           \n2|_|_|_|           \n3|_|_|_|"
    player_turn = 1

    print(clear)
    print(line)

    surf = pygame.display.set_mode((lengh_max, lengh_max))
    run = True
    pygame.draw.line(surf, (0, 255, 0), (lengh, 0), (lengh, lengh_max), 3)
    pygame.draw.line(surf, (0, 255, 0), (lengh_2, 0), (lengh_2, lengh_max), 3)
    pygame.draw.line(surf, (0, 255, 0), (0, lengh), (lengh_max, lengh), 3)
    pygame.draw.line(surf, (0, 255, 0), (0, lengh_2), (lengh_max, lengh_2), 3)

    main_multiplayer()


def main_multiplayer():
    global player_turn, line, clear, number_of_players
    global lengh, lengh_2, lengh_max, surf, run

    # étape 1 afficher la grille
    print(clear)
    print(line)

    # étape 2 demander la position au joueur 1 ou 2
    position = game_get_pos()

    # étape 3 vérifier si la position existe et est libre ou non et  y placer un X ou un O
    check_position(position)

    # étape 4 vérifier si le joueur 1 ou 2 a gagné
    win_verification()

    # étape 5 verifier si il reste des places de libre pour jouer
    empty_spaces_check()

    # étape 6 Changer de joueur
    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1

    # et on recommence
    main_multiplayer()


def game_get_pos():
    global player_turn, line, clear, number_of_players
    global lengh, lengh_2, lengh_max, surf, run

    while run:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed() == (1, 0, 0):
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] <= 201:
                    if mouse_pos[1] <= 201:
                        if line[22] == "_":
                            return 11
                    if 203 <= mouse_pos[1] <= 404:
                        if line[42] == "_":
                            return 21
                    if 206 <= mouse_pos[1]:
                        if line[62] == "_":
                            return 31
                if 203 <= mouse_pos[0] <= 404:
                    if mouse_pos[1] <= 201:
                        if line[24] == "_":
                            return 12
                    if 203 <= mouse_pos[1] <= 404:
                        if line[44] == "_":
                            return 22
                    if 206 <= mouse_pos[1]:
                        if line[64] == "_":
                            return 32
                if 406 <= mouse_pos[0]:
                    if mouse_pos[1] <= 201:
                        if line[26] == "_":
                            return 13
                    if 203 <= mouse_pos[1] <= 404:
                        if line[46] == "_":
                            return 23
                    if 206 <= mouse_pos[1]:
                        if line[66] == "_":
                            return 33
        pygame.display.flip()


def check_position(position):
    global player_turn, line, clear, number_of_players
    global lengh, lengh_2, lengh_max, surf, run

    new_pos = [int(str(position)[0]), int(str(position)[1])]

    x1top = ((new_pos[1]-1) * lengh) + ((new_pos[1]-1) * 3) + 10
    x1floor = ((new_pos[1]) * lengh) + ((new_pos[1]-1) * 3) - 10
    x2top = x1top + 180
    x2floor = x1floor - 180

    ytop = ((new_pos[0]-1) * lengh) + ((new_pos[0]-1) * 3) + 10
    yfloor = ytop + 180

    circle_radius = (lengh - 20) / 2
    circle_center_x = (new_pos[1] * lengh) - 100 + (3 * new_pos[1])
    circle_center_y = (new_pos[0] * lengh) - 100 + (3 * new_pos[0])

    if player_turn == 1:
        line = line[:position * 2] + "X" + line[position * 2 + 1:]
        pygame.draw.line(surf, (255, 0, 0), (x1top, ytop), (x1floor, yfloor), 3)
        pygame.draw.line(surf, (255, 0, 0), (x2top, ytop), (x2floor, yfloor), 3)

    else:
        line = line[:position * 2] + "O" + line[position * 2 + 1:]
        pygame.draw.circle(surf, (0, 0, 255), (circle_center_x, circle_center_y), circle_radius, 3)


def win_verification():
    global player_turn, line, clear, number_of_players
    global lengh, lengh_2, lengh_max, surf, run

    # Les lignes
    if line[22] == line[24] and line[24] == line[26] and (line[22] == "X" or line[22] == "O"):  # ligne 1
        restart()
    if line[42] == line[44] and line[44] == line[46] and (line[44] == "X" or line[44] == "O"):  # ligne 2
        restart()
    if line[62] == line[64] and line[64] == line[66] and (line[66] == "X" or line[66] == "O"):  # ligne 3
        restart()

    # Les colones
    if line[22] == line[42] and line[42] == line[62] and (line[22] == "X" or line[22] == "O"):  # colone 1
        restart()
    if line[24] == line[44] and line[44] == line[64] and (line[44] == "X" or line[44] == "O"):  # colone 2
        restart()
    if line[26] == line[46] and line[46] == line[66] and (line[66] == "X" or line[66] == "O"):  # colone 3
        restart()

    # Les Diagonales
    if line[22] == line[44] and line[44] == line[66] and (line[44] == "X" or line[44] == "O"):  # diagonale 1
        restart()
    if line[62] == line[44] and line[44] == line[26] and (line[44] == "X" or line[44] == "O"):  # diagonale 2
        restart()


def empty_spaces_check():
    global player_turn, line, clear, number_of_players
    global lengh, lengh_2, lengh_max, surf, run

    # on cherche si il reste des "_" dans "line"
    letter = ""
    verif = 0
    while letter != "_":
        letter = line[verif]
        verif += 1
        if verif >= len(line):
            restart(1)


def restart(tie=0):
    global player_turn, line, clear, number_of_players
    global lengh, lengh_2, lengh_max, surf, run

    print(clear)
    print(line)
    pygame.display.flip()
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    if tie == 1:
        button = tk.Button(frame,
                           text="Egalitée clickez pour recommencer",
                           command=setup)
        button.pack(side=tk.LEFT)

        root.mainloop()

    elif player_turn == 1:
        button = tk.Button(frame,
                           text="Le Joueur 1 a gagné clickez pour recommencer",
                           command=setup)
        button.pack(side=tk.LEFT)

        root.mainloop()

    elif player_turn == 2:
        button = tk.Button(frame,
                           text="Le Joueur 2 a gagné clickez pour recommencer",
                           command=setup)
        button.pack(side=tk.LEFT)
        root.mainloop()


if __name__ == "__main__":
    setup()

"""""
def win(grid):
    if no_x:
        return position_of_first_x
    if x and space_near_x:
        return position_close_to_x
    if x and not space_near_x:
        return position_of_new_first_x
"""""
