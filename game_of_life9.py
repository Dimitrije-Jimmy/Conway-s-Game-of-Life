import numpy as np
import scipy.signal as sc
import tkinter as tk
from tkinter import simpledialog, messagebox
import os
from PIL import Image

# rules of the game
#  my rule: all edge pieces will be killed
#   each cell with 1 or 0 neighbors dies - underpopulation
#   each cell with 4 or more neighbors dies - overpopulation
#   each cell with 2 or 3 neighbors lives
#   dead cell revived if surrounded by 3 neighbors 


# previous one was fucked let's try again
# this one is written with ChatGPT help utilizing the convolve2d function from scipy

# this one has the pressable canvas feature added
# this one has the expandable grid on mouse scroll added
# this version is trying to fix the zoom in and out feature and quality of life changes

# failed, got the canvas size fixed and working, and added some good functions
#  for making bigger matrix or smaller one
#  version 8 trying to get the zoom in and zoom out working (it's weird)

# 26.07: Zoom in/out working

# version 9: adding two pop-up windows for saving and loading presets


# The game _____________________________________________________________________

def count_alive_neighbors(matrix):
    # Function returns matrix with values of how many neighbours each cell has

    # Define the neighborhood kernel
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    # Perform convolution to count alive neighbors
    neighbors_count = sc.convolve2d(matrix, kernel, mode='same', boundary='fill')

    return neighbors_count


def update_game_of_life(matrix):
    # Get the number of alive neighbors for each cell
    neighbors_count = count_alive_neighbors(matrix)

    # Create a new matrix to represent the next generation
    next_generation = np.zeros_like(matrix)

    # Apply Conway's rules to update the cells
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 0:
                # Dead cell with exactly three live neighbors becomes a live cell (reproduction)
                if neighbors_count[i, j] == 3:
                    next_generation[i, j] = 1
            else:
                # Live cell with fewer than two live neighbors dies (underpopulation)
                # Live cell with more than three live neighbors dies (overpopulation)
                if neighbors_count[i, j] < 2 or neighbors_count[i, j] > 3:
                    next_generation[i, j] = 0
                else:
                    # Live cell with two or three live neighbors lives on
                    next_generation[i, j] = 1
    return next_generation


# will make automatic matrix generator later
custom_matrix = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
)

custom_matrix = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0]
    ]
)

custom_matrix = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
)


pretty_matrix = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
)

# Control ______________________________________________________________________

def start_game():
    global is_playing
    is_playing = True
    #play_game()
    while is_playing:
        play_game()
        draw_cells()
        root.update()


def stop_game():
    global is_playing
    is_playing = False

def clear_game():
    global is_playing, matrix, generation
    is_playing = False
    matrix = np.zeros((rows, cols))
    generation = 0
    generation_label.config(text=f"Generation: {generation}")
    canvas.delete("cell")
    draw_cells()

# The randomize button
def random_initialize():
    global matrix, generation
    matrix = np.random.choice([0, 1], size=(rows, cols), p=[0.85, 0.15])  # Fill matrix with random 0s and 1s with 65% to 35% ratio
    generation = 0
    generation_label.config(text=f"Generation: {generation}")
    canvas.delete("cell")
    draw_cells()

# Function to update the game state (one generation)
def play_game():
    global generation, is_playing, matrix
    if is_playing:
        matrix = update_game_of_life(matrix)
        canvas.delete("cell")
        draw_cells()
        generation += 1
        generation_label.config(text=f"Generation: {generation}")
        root.after(speed_scale.get(), play_game)  # Adjust the speed of the game based on the slider value

def draw_cells():
    canvas.delete("cell")
    for i in range(rows):
        for j in range(cols):
            x0, y0 = j * cell_size, i * cell_size
            x1, y1 = (j + 1) * cell_size, (i + 1) * cell_size
            if matrix[i, j] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", tags="cell")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill="grey", tags="cell")            

def handle_click(event):
    global matrix
    x, y = event.x // cell_size, event.y // cell_size
    if 0 <= x < cols and 0 <= y < rows:
    #    matrix[y, x] = 1 - matrix[y, x]  # Toggle the cell state (0 to 1 or 1 to 0)
    #    draw_cells()  # Redraw the cells based on the updated matrix

    # Toggle the cell state (alive <-> dead)
        matrix[y, x] = 1 - matrix[y, x]
    draw_cells()  # Redraw the cells based on the updated matrix

# Scrollwheel canvas adjusting
"""
def on_mousewheel(event):
    global cell_size, rows, cols, matrix

    # Determine the direction of the mousewheel scroll
    if event.delta < 0 and cell_size < max_cell_size:
        rows += 1
        cols += 1
        #cell_size += 1
        cell_size = max(min_cell_size, cell_size - 1)
        #cell_size = max(min_cell_size, cell_size + 1)
        #cell_size = min(max_cell_size, cell_size + 1)
        #matrix = np.array([[0] * cols] + [[0] + row + [0] for row in matrix] + [[0] * cols])
        #matrix = add_border(matrix)
        matrix = create_centered_matrix(matrix, rows, cols)

    elif event.delta > 0 and cell_size > min_cell_size:
        rows -= 1
        cols -= 1
        #cell_size -= 1
        cell_size = min(max_cell_size, cell_size+1)
        #cell_size = min(max_cell_size, cell_size - 1)
        #cell_size = max(min_cell_size, cell_size - 1)
        matrix = remove_outer_layer(matrix)
    draw_cells()
"""

# This is so fucking bizarre
def on_mousewheel(event):
    global cell_size, rows, cols, matrix
    global SCREEN_HEIGHT, SCREEN_WIDTH

    # Determine the direction of the mousewheel scroll
    if event.delta < 0 and cell_size <= max_cell_size:
        #rows += 1
        #cols += 1
        #cell_size += 1
        cell_size = max(min_cell_size, cell_size - 1)
        #cell_size = max(min_cell_size, cell_size + 1)
        #cell_size = min(max_cell_size, cell_size + 1)
        #matrix = np.array([[0] * cols] + [[0] + row + [0] for row in matrix] + [[0] * cols])
        #matrix = add_border(matrix)
        #matrix = create_centered_matrix(matrix, rows, cols)

    elif event.delta > 0 and cell_size >= min_cell_size:
        #rows -= 1
        #cols -= 1
        #cell_size -= 1
        cell_size = min(max_cell_size, cell_size + 1)
        #cell_size = min(max_cell_size, cell_size - 1)
        #cell_size = max(min_cell_size, cell_size - 1)
        #matrix = remove_outer_layer(matrix)
    print(cell_size)
    rows = SCREEN_HEIGHT // cell_size
    cols = SCREEN_WIDTH // cell_size
    matrix = create_centered_matrix(matrix, rows, cols)
    draw_cells()


# these two functions cause problems when faced with non square matrixes
"""
def remove_outer_layer(matrix):
    # Shrink the matrix by removing rows and columns from the top, bottom, left, and right
    return matrix[1:-1, 1:-1]

def add_border(matrix):
    # Expand the matrix by adding zeros to the top, bottom, left, and right

    # Calculate the new shape
    new_shape = tuple(dim + 2 for dim in matrix.shape)
    
    # Create a new matrix with zeros and place the original matrix in the center
    new_matrix = np.zeros(new_shape, dtype=matrix.dtype)
    new_matrix[1:-1, 1:-1] = matrix
    
    return new_matrix

"""

def create_centered_matrix(input_matrix, input_rows, input_cols):
    if input_rows < input_matrix.shape[0] or input_cols < input_matrix.shape[1]:
        #raise ValueError("Target size is smaller than the input matrix")
        # this may be a total disaster or really cool
        return reduce_matrix_size(input_matrix, input_rows, input_cols)

    # Create a new matrix of zeros with the target size
    centered_matrix = np.zeros((input_rows, input_cols), dtype=input_matrix.dtype)

    # Calculate the starting indices to place the input_matrix at the center
    start_row = (input_rows - input_matrix.shape[0]) // 2
    start_col = (input_cols - input_matrix.shape[1]) // 2

    # Calculate the ending indices
    end_row = start_row + input_matrix.shape[0]
    end_col = start_col + input_matrix.shape[1]

    # Place the input_matrix at the center of the new matrix
    centered_matrix[start_row:end_row, start_col:end_col] = input_matrix

    return centered_matrix

def reduce_matrix_size(matrix, desired_rows, desired_cols):
    # Get the dimensions of the input matrix
    rows, cols = matrix.shape

    # Calculate the number of rows and columns to remove from top, bottom, left, and right
    rows_to_remove_top = max(0, (rows - desired_rows) // 2)
    rows_to_remove_bottom = max(0, rows - desired_rows - rows_to_remove_top)

    cols_to_remove_left = max(0, (cols - desired_cols) // 2)
    cols_to_remove_right = max(0, cols - desired_cols - cols_to_remove_left)

    # Remove rows and columns from the top, bottom, left, and right sides of the matrix
    new_matrix = matrix[rows_to_remove_top:rows - rows_to_remove_bottom, cols_to_remove_left:cols - cols_to_remove_right]

    return new_matrix

# Customizable canvas size
def change_canvas_size():
    global rows, cols, cell_size, matrix
    try:
        new_rows = int(rows_var.get())
        new_cols = int(cols_var.get())
        if new_rows > 0 and new_cols > 0:
            rows, cols = new_rows, new_cols
            cell_size = min(600 // rows, 600 // cols)
            canvas.config(width=cols * cell_size, height=rows * cell_size)
            matrix = np.zeros((rows, cols))
            canvas.delete("cell")
            draw_cells()
    except ValueError:
        pass


def save_matrix_as_image_and_dat(matrix, filename):
    # Convert matrix to image and save as PNG and DAT

    # Map matrix values to colors: 0 (dead) -> dark grey, 1 (alive) -> yellow
    color_dead = (50, 50, 50) # dark grey
    color_alive = (255, 255, 0) # yellow
    color_map = {0: color_dead, 1: color_alive}

    # Create a numpy array for the image and set the color of each pixel based on the matrix
    image_array = np.array([[color_map[cell] for cell in row] for row in matrix], dtype=np.uint8)
    
    # Create a PIL Image from the numpy array
    #image = Image.fromarray(image_array)
    image = Image.fromarray(image_array, mode="RGB")
    
    # Get the directory of the currently executing script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Create the "Presets" folder in the script directory
    presets_directory = os.path.join(script_directory, "Presets")
    os.makedirs(presets_directory, exist_ok=True)
        
    # Save the image in the "Presets" folder
    image_path = os.path.join(presets_directory, f"{filename}.png")
    image.save(image_path)

    # Save the matrix as .dat file in the "Presets" folder
    file_path = os.path.join(presets_directory, f"{filename}.dat")
    """
    with open(file_path, "w") as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")
    """
    # Save the matrix to the .dat file
    np.savetxt(file_path, matrix, fmt="%d")


def load_matrix_from_file(filename):
    presets_folder = os.path.join(os.path.dirname(__file__), "Presets")

    # Check if the "Presets" folder exists
    if not os.path.exists(presets_folder):
        raise FileNotFoundError("The 'Presets' folder does not exist.")

    # Form the full path to the .dat file
    file_path = os.path.join(presets_folder, filename + ".dat")

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{filename}.dat' does not exist in the 'Presets' folder.")
    
    """
    # Read the data from the .dat file and convert it to a matrix
    with open(file_path, "r") as file:
        lines = file.readlines()
        matrix = [[int(cell) for cell in line.strip()] for line in lines]
    """

    # Read the data from the .dat file and convert it to a NumPy array
    matrix = np.loadtxt(file_path, dtype=int)
    
    return matrix


"""
def save_preset_popup():
    # Create a popup window to ask for the preset name
    popup = tk.Toplevel(root)
    popup.title("Save Preset")
    popup.geometry("300x100")
    
    def save_preset():
        preset_name = entry.get()
        if preset_name:
            save_matrix_as_image_and_dat(matrix, preset_name)
            popup.destroy()
    
    label = tk.Label(popup, text="Enter the preset name:")
    label.pack(pady=5)
    
    entry = tk.Entry(popup)
    entry.pack(pady=5)
    
    save_button = tk.Button(popup, text="Save Preset", command=save_preset)
    save_button.pack(pady=10)
"""

def save_preset_popup():
    # Create a popup window to ask for the preset name

    # Function to handle the save button press
    def save_preset():
        # Get the name entered in the Entry widget
        filename = entry.get()

        # Check if the filename is not empty and contains only valid characters
        if filename.strip() and all(c not in r'\/:*?"<>|' for c in filename):
            try:
                # Call the function to save the matrix with the entered filename
                save_matrix_as_image_and_dat(matrix, filename)
                messagebox.showinfo("Success", f"Preset '{filename}' saved successfully!")
                popup_window.destroy()  # Close the pop-up window after saving
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving: {e}")
        else:
            messagebox.showwarning("Invalid Filename", "Please enter a valid filename.")


    # Create the pop-up window
    popup_window = tk.Toplevel(root)
    popup_window.title("Save Preset")
    #popup_window.geometry("300x100")

    label = tk.Label(popup_window, text="Enter the preset name:")
    label.pack(pady=5)

    """
    # Create and position the label with "(Type here)" text
    label = tk.Label(popup_window, text="(Type here)", fg="gray50")
    """
    label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    

    # Create and position the Entry widget for filename input
    entry = tk.Entry(popup_window)
    entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Function to handle the entry click event
    def on_entry_click(event):
        if entry.get() == "(Type here)":
            entry.delete(0, tk.END)  # Clear the default text
            entry.config(fg="black")  # Change text color to black

    # Bind the on_entry_click function to the Entry widget
    entry.bind("<Button-1>", on_entry_click)

    # Create and position the Save button with two lines "Save \n Preset"
    save_button = tk.Button(popup_window, text="Save\nPreset", command=save_preset)
    save_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    # Set the minimum size of the pop-up window
    popup_window.minsize(300, 0)


# Set up the GUI _______________________________________________________________

root = tk.Tk()
root.title("Conway's Game of Life")

# Your existing matrix
matrix = np.array([[0, 0, 0],
                   [1, 1, 1],
                   [0, 0, 0]])
"""
matrix = custom_matrix
matrix = create_centered_matrix(custom_matrix, 60)
"""
matrix = custom_matrix
matrix = pretty_matrix

reduction = 800
SCREEN_WIDTH, SCREEN_HEIGHT = 1920-reduction, 1080-int(reduction*0.56)

init_rows, init_cols = matrix.shape
init_cell_size = 10
min_cell_size = 5
max_cell_size = 35


#width, height = init_cols*init_cell_size, init_rows*init_cell_size

cell_size = init_cell_size
#rows, cols = matrix.shape
#rows, cols = init_rows, init_cols  


# Calculate the target matrix size based on the standard monitor size and cell size
target_rows = SCREEN_HEIGHT // init_cell_size
target_cols = SCREEN_WIDTH // init_cell_size

rows, cols = target_rows, target_cols # temporary fix needs changing when making zoom in/out

# Create a centered matrix with zeros around based on the calculated target size
matrix = create_centered_matrix(matrix, target_rows, target_cols)
#print(custom_matrix)
#print(custom_matrix.shape)
#print(matrix.shape)


#canvas_width = matrix.shape[1] * init_cell_size
#canvas_height = matrix.shape[0] * init_cell_size
canvas_width, canvas_height = SCREEN_WIDTH, SCREEN_HEIGHT


# Create Canvas to draw the cells
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.bind("<Button-1>", handle_click)
canvas.bind("<MouseWheel>", on_mousewheel)  # Binding the mousewheel scroll event
canvas.pack()


# Draw the initial cells
draw_cells()

# Create buttons
start_button = tk.Button(root, text="Start", command=start_game)
start_button.pack(side="left")

stop_button = tk.Button(root, text="Stop", command=stop_game)
stop_button.pack(side="left")

clear_button = tk.Button(root, text="Clear", command=clear_game)
clear_button.pack(side="left")

# Generation counter
generation = 0
generation_label = tk.Label(root, text=f"Generation: {generation}")
generation_label.pack(side="left", padx=10)

# Speed control slider
speed_scale = tk.Scale(root, from_=500, to=5, orient="horizontal", label="Speed (ms)",
                       sliderlength=20, length=200, showvalue=0)
speed_scale.set(200)  # Set the initial speed
speed_scale.pack(side="right", padx=10)

# Randomizer
random_button = tk.Button(root, text="Randomize", command=random_initialize)
random_button.pack(side="left")

# Canvas size selection
canvas_size_label = tk.Label(root, text="Canvas Size:")
canvas_size_label.pack(side="left", padx=10)

rows_var = tk.StringVar(root, value=str(rows))
rows_entry = tk.Entry(root, textvariable=rows_var, width=4)
rows_entry.pack(side="left")

# in between row and col input field -> row 'x' col
x_label = tk.Label(root, text="x")
x_label.pack(side="left")

cols_var = tk.StringVar(root, value=str(cols))
cols_entry = tk.Entry(root, textvariable=cols_var, width=4)
cols_entry.pack(side="left")

update_button = tk.Button(root, text="Update", command=change_canvas_size)
update_button.pack(side="left")

# Add the "Save" button
save_button = tk.Button(root, text="Save", command=save_preset_popup)
save_button.pack(side=tk.LEFT, padx=10)


# Never added the load button


# Set up the game loop (main event loop)
is_playing = False
root.mainloop()