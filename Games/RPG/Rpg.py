import pygame
import time
import math

global yplayer, xplayer, player_direction, time_stand
global run, lenghx, lenghy, surf, screen
global mc_north1, mc_north2, mc_south1, mc_south2, mc_east1, mc_east2, mc_west1, mc_west2


def setup():
    global yplayer, xplayer, player_direction, time_stand
    global run, lenghx, lenghy, surf, screen
    global mc_north1, mc_north2, mc_south1, mc_south2, mc_east1, mc_east2, mc_west1, mc_west2

    # lengh doit etre un multiple de 32 car les sprites font 32 pixels de large et de long
    lenghx = 1024
    lenghy = 672

    surf = pygame.display.set_mode((lenghx, lenghy))
    run = True

    screen = 505
    player_direction = 0
    xplayer = 16
    yplayer = 10
    time_stand = 0

    mc_north1 = pygame.image.load("mc_north1.png")
    mc_north2 = pygame.image.load("mc_north2.png")
    mc_south1 = pygame.image.load("mc_south1.png")
    mc_south2 = pygame.image.load("mc_south2.png")
    mc_west1 = pygame.image.load("mc_west1.png")
    mc_west2 = pygame.image.load("mc_west2.png")
    mc_east1 = pygame.image.load("mc_east1.png")
    mc_east2 = pygame.image.load("mc_east2.png")

    main_move()


def main_invertory():
    pass


def main_move():
    global yplayer, xplayer, player_direction, time_stand
    global run, lenghx, lenghy, surf, screen

    while run:
        disp_player(-1)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    main_save()
                if event.key == pygame.K_l:
                    main_load()
                if event.key == pygame.K_UP:
                    colision(0)
                elif event.key == pygame.K_RIGHT:
                    colision(1)
                elif event.key == pygame.K_DOWN:
                    colision(2)
                elif event.key == pygame.K_LEFT:
                    colision(3)
    exit()


def colision(move):
    global mc_north1, mc_north2
    global yplayer, xplayer, player_direction, time_stand
    global run, lenghx, lenghy, surf, screen

    new_pos = (0, 0)

    if move == 0:
        new_pos = (xplayer, yplayer - 1)
        print("up")
    elif move == 1:
        new_pos = (xplayer + 1, yplayer)
        print("right")
    elif move == 2:
        new_pos = (xplayer, yplayer + 1)
        print("down")
    elif move == 3:
        new_pos = (xplayer - 1, yplayer)
        print("left")

    print(new_pos)

    if screen == 505:
        screen_colision = [(3, 4), (8, 7)]
        for col in screen_colision:
            if new_pos == col:
                player_direction = move
                main_move()
    disp_player(move)


def disp_player(move):
    global mc_north1, mc_north2
    global yplayer, xplayer, player_direction, time_stand
    global run, lenghx, lenghy, surf, screen

    # print("  ")
    # print("x:", xplayer)
    # print("y:", yplayer)
    # print("direction:", player_direction)

    # Moving
    if player_direction == move:
        yplayer_move = 0
        xplayer_move = 0
        if move == 0:
            for _ in range(2):
                for _ in range(8):
                    yplayer_move += 1
                    time.sleep(0.005)
                    disp_screen()
                    surf.blit(mc_north1, (xplayer * 32, yplayer * 32 - yplayer_move))
                    pygame.display.flip()
                for _ in range(8):
                    yplayer_move += 1
                    time.sleep(0.005)
                    disp_screen()
                    surf.blit(mc_north2, (xplayer * 32, yplayer * 32 - yplayer_move))
                    pygame.display.flip()
            yplayer -= 1
        if move == 1:
            for _ in range(2):
                for _ in range(8):
                    xplayer_move += 1
                    time.sleep(0.005)
                    disp_screen()
                    surf.blit(mc_east1, (xplayer * 32 + xplayer_move, yplayer * 32))
                    pygame.display.flip()
                for _ in range(8):
                    xplayer_move += 1
                    time.sleep(0.005)
                    disp_screen()
                    surf.blit(mc_east2, (xplayer * 32 + xplayer_move, yplayer * 32))
                    pygame.display.flip()
            xplayer += 1
        if move == 2:
            for _ in range(2):
                for _ in range(8):
                    yplayer_move += 1
                    time.sleep(0.005)
                    disp_screen()
                    surf.blit(mc_south1, (xplayer * 32, yplayer * 32 + yplayer_move))
                    pygame.display.flip()
                for _ in range(8):
                    yplayer_move += 1
                    time.sleep(0.005)
                    disp_screen()
                    surf.blit(mc_south2, (xplayer * 32, yplayer * 32 + yplayer_move))
                    pygame.display.flip()
            yplayer += 1
        if move == 3:
            for _ in range(2):
                for _ in range(8):
                    xplayer_move += 1
                    time.sleep(0.005)
                    disp_screen()
                    surf.blit(mc_west1, (xplayer * 32 - xplayer_move, yplayer * 32))
                    pygame.display.flip()
                for _ in range(8):
                    xplayer_move += 1
                    time.sleep(0.005)
                    disp_screen()
                    surf.blit(mc_west2, (xplayer * 32 - xplayer_move, yplayer * 32))
                    pygame.display.flip()
            xplayer -= 1
    elif move != -1:
        player_direction = move

    # Stand animation
    if player_direction == 0:
        time_stand += 1
        if time_stand == 500:
            disp_screen()
            surf.blit(mc_north1, (xplayer * 32, yplayer * 32))
            pygame.display.flip()
        if time_stand == 1000:
            disp_screen()
            surf.blit(mc_north2, (xplayer * 32, yplayer * 32))
            pygame.display.flip()
            time_stand = 0
    elif player_direction == 1:
        time_stand += 1
        if time_stand == 500:
            disp_screen()
            surf.blit(mc_east1, (xplayer * 32, yplayer * 32))
            pygame.display.flip()
        if time_stand == 1000:
            disp_screen()
            surf.blit(mc_east2, (xplayer * 32, yplayer * 32))
            pygame.display.flip()
            time_stand = 0
    elif player_direction == 2:
        time_stand += 1
        if time_stand == 500:
            disp_screen()
            surf.blit(mc_south1, (xplayer * 32, yplayer * 32))
            pygame.display.flip()
        if time_stand == 1000:
            disp_screen()
            surf.blit(mc_south2, (xplayer * 32, yplayer * 32))
            pygame.display.flip()
            time_stand = 0
    elif player_direction == 3:
        time_stand += 1
        if time_stand == 500:
            disp_screen()
            surf.blit(mc_west1, (xplayer * 32, yplayer * 32))
            pygame.display.flip()
        if time_stand == 1000:
            disp_screen()
            surf.blit(mc_west2, (xplayer * 32, yplayer * 32))
            pygame.display.flip()
            time_stand = 0

    # Screen Change
    if yplayer < 0:
        yplayer = int((lenghy / 32) - 1)
        screen_change(0)
    if xplayer >= lenghx / 32:
        xplayer = 0
        screen_change(1)
    if yplayer >= lenghy / 32:
        yplayer = 0
        screen_change(2)
    if xplayer < 0:
        xplayer = int((lenghx / 32) - 1)
        screen_change(3)


def screen_change(move):
    global yplayer, xplayer, player_direction
    global run, lenghx, lenghy, surf, screen

    if move == 0:
        screen -= 100
    if move == 1:
        screen += 1
    if move == 2:
        screen += 100
    if move == 3:
        screen -= 1

    disp_screen()

    main_move()


def disp_screen():
    if screen == 505:
        surf.fill((255, 255, 255))
    else:
        surf.fill((0, 0, 0))


def main_save():
    global yplayer, xplayer, player_direction, time_stand
    global run, lenghx, lenghy, surf, screen

    print("Sauvegarde en cours ...")
    save_file = open("save.txt", "w")

    save_info = [str(xplayer), "\n", str(yplayer), "\n", str(player_direction), "\n", str(screen)]
    save_file.writelines(save_info)

    save_file.close

    print("Sauvegarde terminée !")


def main_load():
    global yplayer, xplayer, player_direction, time_stand
    global run, lenghx, lenghy, surf, screen

    save_file = open("save.txt", "r")

    saves = save_file.readlines()
    save_info = []
    for line in saves:
        save_info.append(line)
        print(line)
    print(save_info)

    xplayer = int(save_info[0])
    yplayer = int(save_info[1])
    player_direction = int(save_info[2])
    screen = int(save_info[3])

    save_file.close


if __name__ == "__main__":
    setup()
