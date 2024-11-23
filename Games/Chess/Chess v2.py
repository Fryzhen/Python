import pygame
import time

global run, lengh, chess_board, surf, player_turn
global wr, wn, wb, wp, wq, wk, br, bn, bb, bp, bq, bk, black_pieces, white_pieces
global xpos1, ypos1, xpos2, ypos2, square_ask1, square_ask2, piece_selected

def setup():
    global run, lengh, chess_board, surf, player_turn
    global wr, wn, wb, wp, wq, wk, br, bn, bb, bp, bq, bk, black_pieces, white_pieces
    global xpos1, ypos1, xpos2, ypos2, square_ask1, square_ask2, piece_selected

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

    print(chess_board)

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
    print_chessboard()

    player_turn = 1
    play()


def play():
    global run, lengh, chess_board, surf, player_turn
    global wr, wn, wb, wp, wq, wk, br, bn, bb, bp, bq, bk, black_pieces, white_pieces
    global xpos1, ypos1, xpos2, ypos2, square_ask1, square_ask2, piece_selected

    pygame.display.flip()
    print("play()")
    print_chessboard()
    time.sleep(0.2)

    while run:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                exit()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                xpos1 = get_square(pygame.mouse.get_pos()[1])
                ypos1 = get_square(pygame.mouse.get_pos()[0])
                square_ask1 = xpos1 * 10 + ypos1
                piece_selected = chess_board[square_ask1]
                if verif_square(square_ask1):
                    pygame.draw.circle(surf, (255, 0, 0), (xpos1 * 50 + 25, ypos1 * 50 + 25), 25, 3)
                    print("Le cercle")
                    while run:
                        for event2 in pygame.event.get():
                            if event2.type == pygame.QUIT:
                                exit()
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                print("L")
                                xpos2 = get_square(pygame.mouse.get_pos()[0])
                                ypos2 = get_square(pygame.mouse.get_pos()[1])
                                square_ask2 = xpos1 * 10 + ypos1
                                if move_square(square_ask2):
                                    print("O")
                                    chess_board = chess_board1[:square_ask1] + "_" + chess_board[(square_ask1 + 1):]
                                    chess_board = chess_board[:square_ask2] + piece_selected + chess_board[(square_ask2 + 1):]
                                    change_player()


def change_player():
    global run, lengh, chess_board, surf, player_turn
    global wr, wn, wb, wp, wq, wk, br, bn, bb, bp, bq, bk, black_pieces, white_pieces
    global xpos1, ypos1, xpos2, ypos2, square_ask1, square_ask2, piece_selected

    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1
    play()


def move_square(square):
    global run, lengh, chess_board, surf, player_turn
    global wr, wn, wb, wp, wq, wk, br, bn, bb, bp, bq, bk, black_pieces, white_pieces
    global xpos1, ypos1, xpos2, ypos2, square_ask1, square_ask2, piece_selected

    chess_case = chess_board[square]

    if chess_case == "P" or chess_case == "S":
        print("o")
        if pawn():
            return True
        else:
            return False
    elif chess_case == "B" or chess_case == "F":
        if bishop():
            return True
        else:
            return False
    elif chess_case == "H" or chess_case == "C":
        if horse():
            return True
        else:
            return False
    elif chess_case == "T" or chess_case == "R":
        if rook():
            return True
        else:
            return False
    elif chess_case == "Q" or chess_case == "D":
        if rook() or bishop():
            return True
        else:
            return False
    elif chess_case == "K" or chess_case == "G":
        if king():
            return True
        else:
            return False
    else:
        return False


def verif_square(square):
    global run, lengh, chess_board, surf, player_turn
    global wr, wn, wb, wp, wq, wk, br, bn, bb, bp, bq, bk, black_pieces, white_pieces
    global xpos1, ypos1, xpos2, ypos2, square_ask1, square_ask2, piece_selected

    if chess_board[square] == "_":
        play()
    else:
        if player_turn == 1:
            for piece in white_pieces:
                if piece_selected == piece in white_pieces:
                    return True
        else:
            for piece in black_pieces:
                if piece_selected == piece:
                    return True


def get_square(mouse_pos):
    global run, lengh, surf

    mouse_pos = int(mouse_pos)
    case_lengh = lengh / 8
    for i in range(8):
        if case_lengh * i <= mouse_pos <= case_lengh * (i + 1):
            return i+1


def print_chessboard():
    global run, lengh, chess_board, surf, player_turn
    global wr, wn, wb, wp, wq, wk, br, bn, bb, bp, bq, bk, black_pieces, white_pieces
    global xpos1, ypos1, xpos2, ypos2, square_ask1, square_ask2, piece_selected

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


def pawn():
    global run, lengh, chess_board, surf, player_turn
    global wr, wn, wb, wp, wq, wk, br, bn, bb, bp, bq, bk, black_pieces, white_pieces
    global xpos1, ypos1, xpos2, ypos2, square_ask1, square_ask2, piece_selected

    if player_turn == 1:
        if ypos1 - 2 == ypos2 and xpos1 == xpos2:
            return True




if __name__ == "__main__":
    setup()
