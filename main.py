import ntpath
from operator import truediv
from pickle import TRUE
from select import select
from tkinter.tix import ROW
from turtle import width
import numpy as np
import pygame
import sys
import math


# rgb color
GREY = (128, 128, 128)  # BOJA POZADINE
ROSEGOLD = (183, 136, 110)  # IGRAC 2
BLACK = (0, 0, 0)  # IGRAC 1
WHITE = (255, 255, 255)  # PRAZNO POLJE


ROW_COUNT = 6
COLUMN_COUNT = 7

# FUNKCIJE


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):  # ako nam je polje prazno prikazuje 0
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):  # izmjena redosljeda, printanje od dole prema gore
    print(np.flip(board, 0))


def winning_move(board, piece):
    # pregled svih horizontalnih lokacija za pobjedu
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # pegled svih vertikalnih lokacija za pobjedu
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # pregled dijagonale s pozitivnim nagibom (lijevo na desno)
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # pregled dijagonale s negativnim nagibom (desno na lijevo)
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(
                screen, GREY, (c*SQUARESIZE, r * SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(
                screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), radius)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(
                    screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(
                    screen, ROSEGOLD, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), radius)

    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

# Link to Pygame Documentation: https: // www.pygame.org/docs/
pygame.init()
SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)
radius = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)
            # Ask player 1 for input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                # if turn == 0:
                # col = int(input("Player 1 Make your selection (0-6):"))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        print("PLAYER 1 WINS!")
                        game_over = True

                # Ask player 2 for input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                # col = int(input("Player 2 Make your selection (0-6):"))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 1):
                        print("PLAYER 2 WINS!")
                        game_over = True

            print_board(board)
            draw_board(board)

            # izmjena izmedju prvog i drugog igraca
            turn += 1
            turn = turn % 2
