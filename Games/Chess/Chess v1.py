import pygame
import time

global run, lengh, chess_board, surf
global wr, wn, wb, wp, wq, wk, br, bn, bb, bp, bq, bk


def setup():
    global run, lengh, chess_board, surf
    global wr, wn, wb, wp, wq, wk, br, bn, bb, bp, bq, bk, black_pieces, white_pieces

    black_pieces = ["T", "C", "F", "G", "D", "P"]
    white_pieces = ["R", "H", "B", "K", "Q", "S"]

    wr = pygame.image.load("wr.png")
    br = pygame.image.load("br.png")
    wn = pygame.image.load("wn.png")
    bn = pygame.image.load("bn.png")
    wb = pygame.image.load("wb.png")
    bb = pygame.image.load("bb.png")
    wp = pygame.image.load("wp.png")
    bp = pygame.image.load("bp.png")
    wq = pygame.image.load("wq.png")
    bq = pygame.image.load("bq.png")
    wk = pygame.image.load("wk.png")
    bk = pygame.image.load("bk.png")

    run = True
    lengh = 400
    surf = pygame.display.set_mode((lengh, lengh))

    chess_board = "chess bord\nTCFDGFCT \nPPPPPPPP \n________ \n________ \n________ \n________ \nSSSSSSSS \nRHBQKBHR"

    boardx = lengh / 16
    boardy = 0
    for i in range(4):
        for k in range(4):
            pygame.draw.line(surf, (255, 255, 255), (boardx, boardy), (boardx, boardy + (lengh / 8)), int(lengh / 8))
            pygame.draw.line(surf, (255, 255, 255), (boardx + (lengh / 8), boardy + (lengh / 8)),
                             (boardx + (lengh / 8), boardy + (2 * (lengh / 8))), int(lengh / 8))
            boardx += lengh / 4
        boardx = (lengh / 16)
        boardy += lengh / 4

    white()


def white():
    global run, lengh, chess_board, surf
    global black_pieces, white_pieces, piece_move, square_ask

    print_game_pieces()
    pygame.display.flip()
    print(" \n\n\n\n\n")
    print(chess_board)
    time.sleep(0.2)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                square_ask = get_square(pygame.mouse.get_pos())
                if chess_board[square_ask] != "_":
                    piece_move = chess_board[square_ask]
                    time.sleep(0.2)
                    print("Pos 1 selected")
                    white_move()
                else:
                    white()


def black():
    global run, lengh, chess_board, surf
    global black_pieces, white_pieces, piece_move, square_ask

    print_game_pieces()
    pygame.display.flip()
    print(" \n\n\n\n\n")
    print(chess_board)
    time.sleep(0.2)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                square_ask = get_square(pygame.mouse.get_pos())
                if chess_board[square_ask] != "_":
                    piece_move = chess_board[square_ask]
                    time.sleep(0.2)
                    print("pièce qui bouge", piece_move)
                    print("Pos 1 selected")
                    black_move()
                else:
                    black()

    white()


def white_move():
    global run, lengh, chess_board, surf
    global black_pieces, white_pieces, piece_move, square_ask

    while run:
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                exit()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                square_ask2 = get_square(pygame.mouse.get_pos())
                print("Pos 2 selected")
                pos_case_1 = [int(str(square_ask)[0]), int(str(square_ask)[1])]
                pos_case_2 = [int(str(square_ask2)[0]), int(str(square_ask2)[1])]
                if square_ask2 != square_ask:
                    if piece_move == "R":
                        if pos_case_2[0] == pos_case_1[0] or pos_case_2[1] == pos_case_1[1]:
                            chess_board = chess_board[:square_ask2] + chess_board[square_ask] + chess_board[
                                                                                                (square_ask2 + 1):]
                            chess_board = chess_board[:square_ask] + "_" + chess_board[(square_ask + 1):]
                            black()
                        else:
                            white()
                    elif piece_move == "B":
                        for i in range(7):
                            if (pos_case_2[0] + i == pos_case_1[0] and pos_case_2[1] + i == pos_case_1[1]
                            ) or (pos_case_2[0] - i == pos_case_1[0] and pos_case_2[1] + i == pos_case_1[1]
                            ) or (pos_case_2[0] + i == pos_case_1[0] and pos_case_2[1] - i == pos_case_1[1]
                            ) or (pos_case_2[0] - i == pos_case_1[0] and pos_case_2[1] - i == pos_case_1[1]):
                                chess_board = chess_board[:square_ask2] + chess_board[square_ask] + chess_board[
                                                                                                    (square_ask2 + 1):]
                                chess_board = chess_board[:square_ask] + "_" + chess_board[(square_ask + 1):]
                                black()
                            else:
                                white()
                    elif piece_move == "H":
                        if (pos_case_2[0] + 2 == pos_case_1[0] and pos_case_2[1] + 1 == pos_case_1[1]
                        ) or (pos_case_2[0] + 2 == pos_case_1[0] and pos_case_2[1] - 1 == pos_case_1[1]
                        ) or (pos_case_2[0] + 1 == pos_case_1[0] and pos_case_2[1] + 2 == pos_case_1[1]
                        ) or (pos_case_2[0] + 1 == pos_case_1[0] and pos_case_2[1] - 2 == pos_case_1[1]
                        ) or (pos_case_2[0] - 2 == pos_case_1[0] and pos_case_2[1] + 1 == pos_case_1[1]
                        ) or (pos_case_2[0] - 2 == pos_case_1[0] and pos_case_2[1] - 1 == pos_case_1[1]
                        ) or (pos_case_2[0] - 1 == pos_case_1[0] and pos_case_2[1] + 2 == pos_case_1[1]
                        ) or (pos_case_2[0] - 1 == pos_case_1[0] and pos_case_2[1] - 2 == pos_case_1[1]):
                            chess_board = chess_board[:square_ask2] + chess_board[square_ask] + chess_board[
                                                                                                (square_ask2 + 1):]
                            chess_board = chess_board[:square_ask] + "_" + chess_board[(square_ask + 1):]
                            black()
                        else:
                            white()

                else:
                    print("Position identique a la première")
                    white()


def black_move():
    global run, lengh, chess_board, surf
    global black_pieces, white_pieces, piece_move, square_ask

    while run:
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                exit()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                square_ask2 = get_square(pygame.mouse.get_pos())
                print("Pos 2 selected")
                pos_case_1 = [int(str(square_ask)[0]), int(str(square_ask)[1])]
                pos_case_2 = [int(str(square_ask2)[0]), int(str(square_ask2)[1])]
                if square_ask2 != square_ask:
                    if piece_move == "T":
                        if pos_case_2[0] == pos_case_1[0] or pos_case_2[1] == pos_case_1[1]:
                            chess_board = chess_board[:square_ask2] + chess_board[square_ask] + chess_board[
                                                                                                (square_ask2 + 1):]
                            chess_board = chess_board[:square_ask] + "_" + chess_board[(square_ask + 1):]
                            white()
                        else:
                            black()
                    elif piece_move == "F":
                        for i in range(7):
                            if (pos_case_2[0] + i == pos_case_1[0] and pos_case_2[1] + i == pos_case_1[1]
                            ) or (pos_case_2[0] - i == pos_case_1[0] and pos_case_2[1] + i == pos_case_1[1]
                            ) or (pos_case_2[0] + i == pos_case_1[0] and pos_case_2[1] - i == pos_case_1[1]
                            ) or (pos_case_2[0] - i == pos_case_1[0] and pos_case_2[1] - i == pos_case_1[1]):
                                chess_board = chess_board[:square_ask2] + chess_board[square_ask] + chess_board[(square_ask2 + 1):]
                                chess_board = chess_board[:square_ask] + "_" + chess_board[(square_ask + 1):]
                                white()
                            else:
                                black()
                    elif piece_move == "C":
                        if (pos_case_2[0] + 2 == pos_case_1[0] and pos_case_2[1] + 1 == pos_case_1[1]
                        ) or (pos_case_2[0] + 2 == pos_case_1[0] and pos_case_2[1] - 1 == pos_case_1[1]
                        ) or (pos_case_2[0] + 1 == pos_case_1[0] and pos_case_2[1] + 2 == pos_case_1[1]
                        ) or (pos_case_2[0] + 1 == pos_case_1[0] and pos_case_2[1] - 2 == pos_case_1[1]
                        ) or (pos_case_2[0] - 2 == pos_case_1[0] and pos_case_2[1] + 1 == pos_case_1[1]
                        ) or (pos_case_2[0] - 2 == pos_case_1[0] and pos_case_2[1] - 1 == pos_case_1[1]
                        ) or (pos_case_2[0] - 1 == pos_case_1[0] and pos_case_2[1] + 2 == pos_case_1[1]
                        ) or (pos_case_2[0] - 1 == pos_case_1[0] and pos_case_2[1] - 2 == pos_case_1[1]):
                            chess_board = chess_board[:square_ask2] + chess_board[square_ask] + chess_board[(square_ask2 + 1):]
                            chess_board = chess_board[:square_ask] + "_" + chess_board[(square_ask + 1):]
                            white()
                        else:
                            black()

                else:
                    print("Position identique a la première")
                    black()


def get_square(mouse_pos):
    global run, lengh, surf

    case_lengh = lengh / 8
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]

    for i in range(8):
        for k in range(8):
            if case_lengh * i <= mouse_pos_y <= case_lengh * (i + 1):
                if case_lengh * k <= mouse_pos_x <= case_lengh * (k + 1):
                    return (i + 1) * 10 + (k + 1)


def print_game_pieces():
    global run, lengh, surf
    global wr, wn, wb, wp, wq, wk, br, bn, bb, bp, bq, bk

    surf.fill((0, 0, 0))
    boardx = lengh / 16
    boardy = 0
    new_lengh = lengh / 8

    for i in range(4):
        for k in range(4):
            pygame.draw.line(surf, (255, 255, 255), (boardx, boardy), (boardx, boardy + (lengh / 8)), int(lengh / 8))
            pygame.draw.line(surf, (255, 255, 255), (boardx + (lengh / 8), boardy + (lengh / 8)),
                             (boardx + (lengh / 8), boardy + (2 * (lengh / 8))), int(lengh / 8))
            boardx += lengh / 4
        boardx = (lengh / 16)
        boardy += lengh / 4

    for i in range(11, 89):
        pos = [int(str(i)[0]) - 1, int(str(i)[1]) - 1]
        if chess_board[i] == "R":
            surf.blit(wr, (new_lengh * pos[1], new_lengh * pos[0]))
        if chess_board[i] == "T":
            surf.blit(br, (new_lengh * pos[1], new_lengh * pos[0]))
        if chess_board[i] == "H":
            surf.blit(wn, (new_lengh * pos[1], new_lengh * pos[0]))
        if chess_board[i] == "C":
            surf.blit(bn, (new_lengh * pos[1], new_lengh * pos[0]))
        if chess_board[i] == "B":
            surf.blit(wb, (new_lengh * pos[1], new_lengh * pos[0]))
        if chess_board[i] == "F":
            surf.blit(bb, (new_lengh * pos[1], new_lengh * pos[0]))
        if chess_board[i] == "K":
            surf.blit(wk, (new_lengh * pos[1], new_lengh * pos[0]))
        if chess_board[i] == "G":
            surf.blit(bk, (new_lengh * pos[1], new_lengh * pos[0]))
        if chess_board[i] == "Q":
            surf.blit(wq, (new_lengh * pos[1], new_lengh * pos[0]))
        if chess_board[i] == "D":
            surf.blit(bq, (new_lengh * pos[1], new_lengh * pos[0]))
        if chess_board[i] == "S":
            surf.blit(wp, (new_lengh * pos[1], new_lengh * pos[0]))
        if chess_board[i] == "P":
            surf.blit(bp, (new_lengh * pos[1], new_lengh * pos[0]))


if __name__ == "__main__":
    setup()
