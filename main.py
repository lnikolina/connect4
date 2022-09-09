import ntpath
from select import select
import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COLUMT_COUNT = 7


def create_board():
    board = np.zeros((6, 7))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[5][col] == 0


def get_next_open_row(board, col):  # ako nam je polje prazno prikazuje 0
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):  # izmjena redosljeda, printanje od dole prema gore
    print(np.flip(board, 0))


board = create_board()
print_board(board)
game_over = False
turn = 0


while not game_over:
    # Ask player 1 for input
    if turn == 0:
        col = int(input("Player 1 Make your selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

        print(col)
        print(type(col))

        print_board(board)

    # Ask player 2 for input
    else:
        col = int(input("Player 2 Make your selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    print_board(board)

    # izmjena izmedju prvog i drugog igraca
    turn += 1
    turn = turn % 2
