import tkinter as tk
import random

# Constants for cell status
DEAD = 0
ALIVE = 1

# Constants for initial grid size and cell size
INIT_CELL_SIZE = 15
MIN_CELL_SIZE = 5
MAX_CELL_SIZE = 40
INIT_ROWS, INIT_COLS = 40, 60
WIDTH, HEIGHT = INIT_COLS * INIT_CELL_SIZE, INIT_ROWS * INIT_CELL_SIZE

# Initialize the matrix with DEAD cells
matrix = [[DEAD for _ in range(INIT_COLS)] for _ in range(INIT_ROWS)]

# Variables for current grid size and cell size
current_rows = INIT_ROWS
current_cols = INIT_COLS
current_cell_size = INIT_CELL_SIZE

def count_alive_neighbors(matrix, row, col):
    # ... (unchanged) ...

def get_next_state(matrix):
    # ... (unchanged) ...

def update_game():
    global matrix
    new_matrix = get_next_state(matrix)
    for i in range(current_rows):
        for j in range(current_cols):
            if matrix[i][j] != new_matrix[i][j]:
                if new_matrix[i][j] == ALIVE:
                    canvas.itemconfig(cells[i][j], fill="black")
                else:
                    canvas.itemconfig(cells[i][j], fill="white")
    matrix = new_matrix
    root.after(100, update_game)

def clear_grid():
    global matrix
    matrix = [[DEAD for _ in range(current_cols)] for _ in range(current_rows)]
    for i in range(current_rows):
        for j in range(current_cols):
            canvas.itemconfig(cells[i][j], fill="white")

def randomize_grid():
    global matrix
    matrix = [[random.randint(0, 1) for _ in range(current_cols)] for _ in range(current_rows)]
    for i in range(current_rows):
        for j in range(current_cols):
            if matrix[i][j] == ALIVE:
                canvas.itemconfig(cells[i][j], fill="black")
            else:
                canvas.itemconfig(cells[i][j], fill="white")

def on_canvas_click(event):
    global matrix
    row, col = event.y // current_cell_size, event.x // current_cell_size
    matrix[row][col] = 1 - matrix[row][col]  # Toggle cell state
    color = "black" if matrix[row][col] == ALIVE else "white"
    canvas.itemconfig(cells[row][col], fill=color)

def on_mousewheel(event):
    global current_rows, current_cols, current_cell_size, matrix

    # Determine the direction of the mousewheel scroll
    if event.delta > 0 and current_cell_size < MAX_CELL_SIZE:
        if current_rows < INIT_ROWS or current_cols < INIT_COLS:
            current_rows += 1
            current_cols += 1
            current_cell_size = max(MIN_CELL_SIZE, current_cell_size - 1)
            # Expand the matrix by adding zeros to the top, bottom, left, and right
            matrix = [[DEAD] * current_cols] + [[DEAD] + row + [DEAD] for row in matrix] + [[DEAD] * current_cols]
    elif event.delta < 0 and current_cell_size > MIN_CELL_SIZE:
        current_rows -= 1
        current_cols -= 1
        current_cell_size = min(MAX_CELL_SIZE, current_cell_size + 1)
        # Shrink the matrix by removing rows and columns from the top, bottom, left, and right
        matrix = [row[1:-1] for row in matrix[1:-1]]

    # Update canvas size
    canvas.config(width=current_cols * current_cell_size, height=current_rows * current_cell_size)

    # Update cell rectangles
    for i in range(INIT_ROWS):
        for j in range(INIT_COLS):
            x1, y1 = j * current_cell_size, i * current_cell_size
            x2, y2 = x1 + current_cell_size, y1 + current_cell_size
            if i < current_rows and j < current_cols:
                canvas.coords(cells[i][j], x1, y1, x2, y2)
            else:
                # Hide cells that are outside the current matrix range
                canvas.coords(cells[i][j], -current_cell_size, -current_cell_size, 0, 0)

# GUI setup
root = tk.Tk()
root.title("Conway's Game of Life")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

cells = [[None for _ in range(INIT_COLS)] for _ in range(INIT_ROWS)]
for i in range(INIT_ROWS):
    for j in range(INIT_COLS):
        x1, y1 = j * INIT_CELL_SIZE, i * INIT_CELL_SIZE
        x2, y2 = x1 + INIT_CELL_SIZE, y1 + INIT_CELL_SIZE
        cells[i][j] = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray", tags="cell")

canvas.bind("<Button-1>", on_canvas_click)
canvas.bind("<MouseWheel>", on_mousewheel)  # Binding the mousewheel scroll event

start_button = tk.Button(root, text="Start", command=update_game)
start_button.pack(side="left", padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_grid)
clear_button.pack(side="left", padx=5, pady=5)

randomize_button = tk.Button(root, text="Randomize", command=randomize_grid)
randomize_button.pack(side="left", padx=5, pady=5)


root.mainloop()