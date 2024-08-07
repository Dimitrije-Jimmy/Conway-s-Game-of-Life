import numpy as np
import scipy.signal as sc

def count_alive_neighbors(matrix):
    # Define the neighborhood kernel
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    # Perform convolution to count alive neighbors
    neighbors_count = sc.convolve2d(matrix, kernel, mode='same', boundary='fill') # fill is right, wrap goes around the matrix to the other side

    return neighbors_count

# Example usage
matrix = np.array([[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]])
"""
matrix = np.array(
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
"""
neighbors_count = count_alive_neighbors(matrix)
print(neighbors_count)