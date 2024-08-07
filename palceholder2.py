import numpy as np

def remove_outer_layer(matrix):
    return matrix[1:-1, 1:-1]

# Example 1
matrix1 = np.array([[0, 1, 0], [0, 1, 0], [0, 0, 0]])
result1 = remove_outer_layer(matrix1)
print(result1)
# Output: [[1]]

# Example 2
matrix2 = np.array([[0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
result2 = remove_outer_layer(matrix2)
print(result2)
# Output:
# [[0 1 1]
#  [0 1 1]
#  [0 0 0]]


print(matrix2[1:-1, 1:-1])

def add_border(matrix):
    # Calculate the new shape
    new_shape = tuple(dim + 2 for dim in matrix.shape)
    
    # Create a new matrix with zeros and place the original matrix in the center
    new_matrix = np.zeros(new_shape, dtype=matrix.dtype)
    new_matrix[1:-1, 1:-1] = matrix
    
    return new_matrix

# Example
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
expanded_matrix = add_border(matrix)
print(expanded_matrix)


def create_centered_matrix(input_matrix, n):
    if n < input_matrix.shape[0] or n < input_matrix.shape[1]:
        raise ValueError("Target size is smaller than the input matrix")

    # Create a new matrix of zeros with the target size
    centered_matrix = np.zeros((n, n), dtype=input_matrix.dtype)

    # Calculate the starting indices to place the input_matrix at the center
    start_row = (n - input_matrix.shape[0]) // 2
    start_col = (n - input_matrix.shape[1]) // 2

    # Calculate the ending indices
    end_row = start_row + input_matrix.shape[0]
    end_col = start_col + input_matrix.shape[1]

    # Place the input_matrix at the center of the new matrix
    centered_matrix[start_row:end_row, start_col:end_col] = input_matrix

    return centered_matrix

def create_centered_matrix2(input_matrix, input_rows, input_cols):
    if input_rows < input_matrix.shape[0] or input_cols < input_matrix.shape[1]:
        raise ValueError("Target size is smaller than the input matrix")

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

# Example
input_matrix = np.array([[1]])
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
input_matrix = matrix
#target_size = 5
target_rows = 4
target_cols = 4
#centered_matrix = create_centered_matrix(input_matrix, target_size)
centered_matrix = create_centered_matrix(input_matrix, target_rows)
centered_matrix = create_centered_matrix(input_matrix, target_cols)
#print(centered_matrix)

centered_matrix2 = create_centered_matrix2(input_matrix, target_rows, target_cols)
print(matrix)
print(centered_matrix2)



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


#matrix = create_centered_matrix2(custom_matrix, 40, 71)
#print(matrix)


from PIL import Image

def export_matrix_as_image(matrix, file_path):
    # Define the colors for dead (grey) and alive (yellow) cells
    dead_color = (192, 192, 192)  # Grey
    alive_color = (255, 255, 0)   # Yellow

    # Get the dimensions of the matrix
    rows, cols = matrix.shape

    # Calculate the size of the image based on cell size (you can adjust this if needed)
    cell_size = 10
    image_width = cols * cell_size
    image_height = rows * cell_size

    # Create a new image with a white background
    image = Image.new("RGB", (image_width, image_height), (255, 255, 255))
    pixels = image.load()

    # Convert the matrix values to colors and set the pixels in the image
    for row in range(rows):
        for col in range(cols):
            cell_value = matrix[row, col]
            color = alive_color if cell_value == 1 else dead_color
            for y in range(row * cell_size, (row + 1) * cell_size):
                for x in range(col * cell_size, (col + 1) * cell_size):
                    pixels[x, y] = color

    # Save the image to the specified file path
    image.save(file_path)

# Assuming 'matrix' is the numpy matrix you want to export
#export_matrix_as_image(custom_matrix, "output_image2.png")



def reduce_matrix_size(matrix, desired_rows, desired_cols):
    # Get the dimensions of the input matrix
    rows, cols = matrix.shape

    # Calculate the number of rows and columns to remove from each side
    rows_to_remove = (rows - desired_rows) // 2
    cols_to_remove = (cols - desired_cols) // 2

    # Make sure the number of rows and columns to remove is non-negative
    rows_to_remove = max(0, rows_to_remove)
    cols_to_remove = max(0, cols_to_remove)

    # Remove rows and columns from the top, bottom, left, and right sides of the matrix
    new_matrix = matrix[rows_to_remove:rows - rows_to_remove, cols_to_remove:cols - cols_to_remove]

    return new_matrix

def reduce_matrix_size2(matrix, desired_rows, desired_cols):
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

#expanded_matrix = add_border(expanded_matrix)
desired_rows = 4
desired_cols = 5
new_matrix = reduce_matrix_size2(expanded_matrix, desired_rows, desired_cols)
print(expanded_matrix)
print(new_matrix)



import os
from PIL import Image

def save_matrix_as_image_and_dat(matrix, filename):
    # Create a new "Presets" folder if it doesn't exist
    if not os.path.exists("Presets"):
        os.makedirs("Presets")

    # Save the matrix as a .dat file
    with open(f"Presets/{filename}.dat", "w") as file:
        for row in matrix:
            file.write(" ".join(str(cell) for cell in row) + "\n")

    # Map matrix values to colors: 0 (dead) -> dark grey, 1 (alive) -> yellow
    color_map = {0: (50, 50, 50), 1: (255, 255, 0)}

    # Create a numpy array for the image and set the color of each pixel based on the matrix
    image_array = np.array([[color_map[cell] for cell in row] for row in matrix], dtype=np.uint8)

    # Create a PIL Image from the numpy array
    image = Image.fromarray(image_array)

    # Save the image as a PNG file
    image.save(f"Presets/{filename}.png")
    print(1)

"""
def save_matrix_as_image_and_dat(matrix, filename):
    # Convert matrix to image and save as PNG
    image_data = matrix_to_image_data(matrix)
    image = Image.fromarray(image_data, mode="RGB")
    
    # Get the current working directory and create the "Presets" folder
    current_directory = os.getcwd()
    presets_directory = os.path.join(current_directory, "Presets")
    os.makedirs(presets_directory, exist_ok=True)
    
    # Save the image in the "Presets" folder
    image_path = os.path.join(presets_directory, f"{filename}.png")
    image.save(image_path)
    
    # Save the matrix as .dat file in the "Presets" folder
    matrix_path = os.path.join(presets_directory, f"{filename}.dat")
    with open(matrix_path, "w") as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")
"""

def save_matrix_as_image_and_dat2(matrix, filename):
    # Convert matrix to image and save as PNG
    # Map matrix values to colors: 0 (dead) -> dark grey, 1 (alive) -> yellow
    color_map = {0: (50, 50, 50), 1: (255, 255, 0)}
    
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
    matrix_path = os.path.join(presets_directory, f"{filename}.dat")
    with open(matrix_path, "w") as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")


# Example usage:
matrix_to_save = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
save_matrix_as_image_and_dat2(matrix_to_save, "preset_1")