import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image
import os
import numpy as np


# Example usage:
matrix= np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

def save_matrix_as_image_and_dat(matrix, filename):
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
try:
    loaded_matrix = load_matrix_from_file("your_preset_filename")
    print("Matrix loaded successfully:")
    print(loaded_matrix)
except Exception as e:
    print("Error while loading matrix:", e)
"""

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

root = tk.Tk()

# Create the pop-up window
popup_window = tk.Toplevel(root)
popup_window.title("Save Preset")

# Create and position the label with "(Type here)" text
label = tk.Label(popup_window, text="(Type here)", fg="gray50")
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

# Run the Tkinter main loop
root.mainloop()