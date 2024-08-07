import numpy as np
import matplotlib.pyplot as plt
import sys

# rules of the game
#  my rule: all edge pieces will be killed
#   each cell with 1 or 0 neighbors dies
#   each cell with 4 or more neighbors dies
#   each cell with 2 or 3 neighbors lives
#   dead cell revived if surrounded by 3 neighbors 


# matrix - matrix of values of the atuomaton
# position - (x,y) of the cells coordinates


def alive_or_dead(matrix, x, y):
    # Function checks whether cell is alive or dead

    return (matrix[x, y] == 1)

def check_neighbours(matrix, x, y):
    num_alive_neighbours = 0

    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if alive_or_dead(matrix, x+i, y+j) == True: # for some reason "is True" doesn't work
            #if matrix[x+i, y+j] == 1:
                num_alive_neighbours += 1
            else: 
                num_alive_neighbours += 0
    return num_alive_neighbours 


def check_neighbours_fast(matrix, x, y):
    # upgrade later
   return None


def cell_on_edge(matrix, x, y):
    # Function checks whether cell is on edge

    row_length = len(matrix[0])-1
    column_length = len(matrix)-1
    if x == 0 or x == column_length or y == 0 or y == row_length:
        return True
    else:
        return False



def iterate_life(matrix):
    # Function iterates the entire matrix each cell whether it will live or die 

    new_matrix = np.zeros_like(matrix)

    # this is the iteration
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):

            # I could remove the checking if on edge by just making range from 1 to len
            #  but that would make it so any cell made alive at the start on the edge would remain alive for eternity
            #   this I think is the better outcome, possibly add edge cases in the future, although the code becomes veryy ugly
            if cell_on_edge(matrix, x, y):
                new_matrix[x, y] = 0 
            else:
                num_alive_neighbours = check_neighbours(matrix, x, y)
                #print(num_alive_neighbours)
                if alive_or_dead(matrix, x, y) == True:
                    if num_alive_neighbours >= 4 or num_alive_neighbours <= 1:
                        new_matrix[x, y] = 0
                    else:
                        new_matrix[x, y] = 1
                else:
                    if num_alive_neighbours == 3:
                        new_matrix[x, y] = 1
    #print(new_matrix)

    return new_matrix



def iteration_faster(matrix):
    # upgrade it with numpy to apply the functions to each cell at once in the submatrix (removed edges and corners)

    return None


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
"""
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
"""






def main_func(matrix, gen):
    print("Generation:", 0)
    print(custom_matrix)
    print(" "*20)

    for current_gen in range(1, gen+1):
        
        matrix = iterate_life(matrix)

        print("Generation:", current_gen)
        print(matrix)
        print(" "*20)


main_func(custom_matrix, 2)

