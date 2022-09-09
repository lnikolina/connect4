import ntpath
from select import select
import numpy as np
import pygame
import sys
import math


def create_board():
    board = np.zeros((6, 7))
    return board


board = create_board()
game_over = False
turn = 0

while not game_over:
    # Ask player 1 for input
    if turn == 0:
        selection = int(input("Player 1 Make your selection (0-6):"))

        print(selection)
        print(type(selection))
