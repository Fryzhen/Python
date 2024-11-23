import random
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


Solitaire

1) afficher la grille
2) demander la position au joueur 
3) vérifier si la position est libre ou non
4) vérifier si le joueur a gagné
5) vérifier si il reste des places de libre
6) faire en sorte que l'ordinateur fasse un bon coup    


options suplémentaires

1) l'aficher dans un tableau/app à part

"""""


def setup():
    global player_turn, line, clear, number_of_players
    global x_center, x_side, x_corner, o_center, o_side, o_corner, xplays, oplays
    global lengh, lengh_2, lengh_max, surf, run

    lengh = 200
    lengh_2 = lengh * 2 + 3
    lengh_max = lengh * 3 + 6

    x_center = 0
    x_side = 0
    x_corner = 0
    o_center = 0
    o_side = 0
    o_corner = 0

    xplays = x_side + x_center + x_corner
    oplays = o_side + o_center + o_corner

    clear = "\n" * 3
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

    main_solo()


def main_solo():
    global player_turn, line, clear, number_of_players
    global x_center, x_side, x_corner, o_center, o_side, o_corner, xplays, oplays
    global lengh, lengh_2, lengh_max, surf, run

    # étape 1 afficher la grille
    print(clear)
    print(line)

    # étape 2 demander la position au joueur
    position = game_get_pos()

    # étape 3 vérifier si la position existe et est libre ou non et  y placer un X

    check_position(position)

    # comptes pour l'ordinateur
    if position == 11 or position == 31 or position == 13 or position == 33:
        x_corner += 1
    elif position == 21 or position == 12 or position == 23 or position == 32:
        x_side += 1
    else:
        x_center += 1

    xplays = x_side + x_center + x_corner
    oplays = o_side + o_center + o_corner

    # étape 4 vérifier si le joueur a gagné
    win_verification()

    # étape 5 verifier si il reste des places de libre pour jouer
    empty_spaces_check()

    # étape 6 faire en sorte que l'ordinateur fasse un bon coup

    bot_position = bot_play_v1()

    line = line[:bot_position * 2] + "O" + line[bot_position * 2 + 1:]

    new_pos = [int(str(bot_position)[0]), int(str(bot_position)[1])]

    circle_radius = (lengh - 20) / 2
    circle_center_x = (new_pos[1] * lengh) - 100 + (3 * new_pos[1])
    circle_center_y = (new_pos[0] * lengh) - 100 + (3 * new_pos[0])

    pygame.draw.circle(surf, (0, 0, 255), (circle_center_x, circle_center_y), circle_radius, 3)

    if bot_position == 11 or bot_position == 31 or bot_position == 13 or bot_position == 33:
        o_corner += 1
    elif bot_position == 21 or bot_position == 12 or bot_position == 23 or bot_position == 32:
        o_side += 1
    else:
        o_center += 1

    xplays = x_side + x_center + x_corner
    oplays = o_side + o_center + o_corner

    # étape 4 vérifier si le robot a gagné
    win_verification()

    main_solo()


def check_position(position):
    global player_turn, line, clear
    global x_center, x_side, x_corner, o_center, o_side, o_corner, xplays, oplays
    global lengh, lengh_2, lengh_max, surf, run

    new_pos = [int(str(position)[0]), int(str(position)[1])]

    xright = ((new_pos[1]-1) * lengh) + ((new_pos[1]-1) * 3) + 10
    xleft = ((new_pos[1]) * lengh) + ((new_pos[1]-1) * 3) - 10

    ytop = ((new_pos[0]-1) * lengh) + ((new_pos[0]-1) * 3) + 10
    yfloor = ytop + 180

    line = line[:position * 2] + "X" + line[position * 2 + 1:]

    pygame.draw.line(surf, (255, 0, 0), (xright, ytop), (xleft, yfloor), 3)
    pygame.draw.line(surf, (255, 0, 0), (xleft, ytop), (xright, yfloor), 3)


def win_verification():
    global line

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
    global x_center, x_side, x_corner, o_center, o_side, o_corner, center, side, corner, xplays, oplays
    global lengh, lengh_2, lengh_max, surf, run

    # on cherche si il reste des "_" dans "line"
    letter = ""
    verif = 0
    while letter != "_":
        letter = line[verif]
        verif += 1
        if verif >= len(line):
            restart(1)


def bot_play_v1():
    global player_turn, line, clear, number_of_players
    global x_center, x_side, x_corner, o_center, o_side, o_corner, center, side, corner, xplays, oplays
    global lengh, lengh_2, lengh_max, surf, run

    if xplays == 1:
        if x_side == 1 or x_corner == 1:
            return 22
        else:
            return 11

    if xplays == 2:

        if x_center == 1 and x_corner == 1:
            if line[26] == "X":
                return 31
            elif line[62] == "X":
                return 13
            elif line[66] == "X":
                return 13

        if x_center == 1 and x_side == 1:
            if line[24] == "X":
                return 32
            if line[42] == "X":
                return 23
            if line[64] == "X":
                return 12
            if line[46] == "X":
                return 21

        if x_side == 1 and x_corner == 1:
            if line[22] == "X":
                if line[24] == "X":
                    return 13
                if line[42] == "X":
                    return 31
                if line[64] == "X":
                    return 31
                if line[46] == "X":
                    return 13
            if line[26] == "X":
                if line[24] == "X":
                    return 11
                if line[42] == "X":
                    return 11
                if line[64] == "X":
                    return 33
                if line[46] == "X":
                    return 33
            if line[66] == "X":
                if line[24] == "X":
                    return 13
                if line[42] == "X":
                    return 31
                if line[64] == "X":
                    return 31
                if line[46] == "X":
                    return 13
            if line[62] == "X":
                if line[24] == "X":
                    return 11
                if line[42] == "X":
                    return 11
                if line[64] == "X":
                    return 33
                if line[46] == "X":
                    return 33

        if x_corner == 2:

            if line[22] == line[26] == "X":
                return 12
            elif line[66] == line[26] == "X":
                return 23
            elif line[66] == line[62] == "X":
                return 32
            elif line[22] == line[62] == "X":
                return 21
            else:
                return 12

        if x_side == 2:
            if line[24] == line[46] == "X":
                return 13
            elif line[64] == line[46] == "X":
                return 33
            elif line[64] == line[42] == "X":
                return 31
            elif line[24] == line[42] == "X":
                return 11
            elif line[42] == line[46] == "X":
                return 12
            elif line[64] == line[24] == "X":
                return 21

    if xplays >= 3:
        # vérif si le bot peux win
        if o_center == 1:
            if line[22] == "O" and line[66] == "_":
                return 33
            if line[24] == "O" and line[64] == "_":
                return 32
            if line[26] == "O" and line[62] == "_":
                return 31
            if line[46] == "O" and line[42] == "_":
                return 21
            if line[66] == "O" and line[22] == "_":
                return 11
            if line[64] == "O" and line[24] == "_":
                return 12
            if line[62] == "O" and line[26] == "_":
                return 13
            if line[42] == "O" and line[46] == "_":
                return 23

        if x_center == 1:

            if line[22] == "O" and line[62] == "O" and line[42] == "_":
                return 21
            if line[66] == "O" and line[62] == "O" and line[64] == "_":
                return 32
            if line[66] == "O" and line[26] == "O" and line[46] == "_":
                return 23
            if line[22] == "O" and line[26] == "O" and line[24] == "_":
                return 12

            if line[42] == "O":
                if line[22] == "O" and line[62] == "_":
                    return 31
                if line[62] == "O" and line[22] == "_":
                    return 11
            if line[24] == "O":
                if line[22] == "O" and line[26] == "_":
                    return 13
                if line[26] == "O" and line[22] == "_":
                    return 11
            if line[46] == "O":
                if line[26] == "O" and line[62] == "_":
                    return 31
                if line[62] == "O" and line[26] == "_":
                    return 13
            if line[64] == "O":
                if line[62] == "O" and line[66] == "_":
                    return 33
                if line[66] == "O" and line[62] == "_":
                    return 31

        # vérif si on doit bloquer l'adversaire
        if o_center == 1:

            if line[22] == "X" and line[62] == "X" and line[42] == "_":
                return 21
            if line[66] == "X" and line[62] == "X" and line[64] == "_":
                return 32
            if line[66] == "X" and line[26] == "X" and line[46] == "_":
                return 23
            if line[22] == "X" and line[26] == "X" and line[24] == "_":
                return 12

            if line[42] == "X":
                if line[22] == "X" and line[62] == "_":
                    return 31
                if line[62] == "X" and line[22] == "_":
                    return 11
            if line[24] == "X":
                if line[22] == "X" and line[26] == "_":
                    return 13
                if line[26] == "X" and line[22] == "_":
                    return 11
            if line[46] == "X":
                if line[26] == "X" and line[62] == "_":
                    return 31
                if line[62] == "X" and line[26] == "_":
                    return 13
            if line[64] == "X":
                if line[62] == "X" and line[66] == "_":
                    return 33
                if line[66] == "X" and line[62] == "_":
                    return 31

        if x_center == 1:
            if line[22] == "X" and line[66] == "_":
                return 33
            if line[24] == "X" and line[64] == "_":
                return 32
            if line[26] == "X" and line[62] == "_":
                return 31
            if line[46] == "X" and line[42] == "_":
                return 21
            if line[66] == "X" and line[22] == "_":
                return 11
            if line[64] == "X" and line[24] == "_":
                return 12
            if line[62] == "X" and line[26] == "_":
                return 13
            if line[42] == "X" and line[46] == "_":
                return 23

    count = 0
    remainings = []

    for charachter in line:
        count += 1
        if charachter == "_":
            remainings.append(count / 2)

    soluce = int(random.choice(remainings))
    return soluce


def restart(tie=0):
    global player_turn, line, clear, number_of_players
    global x_center, x_side, x_corner, o_center, o_side, o_corner, center, side, corner, xplays, oplays
    global lengh, lengh_2, lengh_max, surf, run, root, frame

    print(clear)
    print(line)

    pygame.display.flip()
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    if tie == 1:
        button = tk.Button(frame,
                           text="Egalitée clickez pour recommencer",
                           command=end)
        button.pack(side=tk.LEFT)

        root.mainloop()

    else:
        button = tk.Button(frame,
                           text="Le Robot a gagné clickez pour recommencer",
                           command=end)
        button.pack(side=tk.LEFT)

        root.mainloop()


def end():
    global player_turn, line, clear, number_of_players
    global x_center, x_side, x_corner, o_center, o_side, o_corner, center, side, corner, xplays, oplays
    global lengh, lengh_2, lengh_max, surf, run, root, frame

    root.destroy()
    setup()


def game_get_pos():
    global player_turn, line, clear, number_of_players
    global x_center, x_side, x_corner, o_center, o_side, o_corner, center, side, corner, xplays, oplays
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
