import ntpath
from operator import truediv
from pickle import TRUE
from select import select
import numpy as np
import pygame
import sys
import math

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

            if winning_move(board, 1):
                print("PLAYER 1 WINS!")
                game_over = True

    # Ask player 2 for input
    else:
        col = int(input("Player 2 Make your selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 1):
                print("PLAYER 2 WINS!")
                game_over = True

    print_board(board)

    # izmjena izmedju prvog i drugog igraca
    turn += 1
    turn = turn % 2
