import numpy as np
import tkinter as tk

def count_alive_neighbors(matrix):
    # ... (same as before)

def update_game_of_life(matrix):
    # ... (same as before)

def start_game():
    # ... (same as before)

def stop_game():
    # ... (same as before)

def clear_game():
    # ... (same as before)

def random_initialize():
    global matrix, generation
    matrix = np.random.choice([0, 1], size=(rows, cols), p=[0.65, 0.35])  # Fill matrix with random 0s and 1s with 65% to 35% ratio
    generation = 0
    generation_label.config(text=f"Generation: {generation}")
    canvas.delete("cell")
    draw_cells()

def play_game():
    global generation
    if is_playing:
        matrix = update_game_of_life(matrix)
        canvas.delete("cell")
        draw_cells()
        generation += 1
        generation_label.config(text=f"Generation: {generation}")
        root.after(speed_scale.get(), play_game)  # Adjust the speed of the game based on the slider value

def draw_cells():
    # ... (same as before)

# Set up the GUI
root = tk.Tk()
root.title("Conway's Game of Life")

# Your existing matrix
matrix = np.array([[0, 1, 0],
                   [1, 0, 1],
                   [0, 1, 0]])

rows, cols = matrix.shape
cell_size = 20

# Create Canvas to draw the cells
canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size, bg="white")
canvas.pack()

# Draw the initial cells
draw_cells()

# Create buttons
# ... (same as before)

# Generation counter
generation = 0
generation_label = tk.Label(root, text=f"Generation: {generation}")
generation_label.pack(side="left", padx=10)

# Speed control slider
speed_scale = tk.Scale(root, from_=1000, to=50, orient="horizontal", label="Speed (ms)",
                       sliderlength=20, length=200, showvalue=0)
speed_scale.set(200)  # Set the initial speed
speed_scale.pack(side="right", padx=10)

# Set up the game loop (main event loop)
is_playing = False
root.mainloop()