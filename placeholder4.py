import os
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def load_matrix_from_dat(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        matrix = [[int(val) for val in line.strip().split()] for line in lines]
    return np.array(matrix)

def load_preset():
    presets_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Presets")
    preset_files = [file for file in os.listdir(presets_directory) if file.endswith(".dat")]

    def on_preset_selected(event):
        selected_preset = preset_listbox.get(preset_listbox.curselection())
        preview_matrix = load_matrix_from_dat(os.path.join(presets_directory, selected_preset))
        update_preview(preview_matrix)

    def update_preview(matrix):
        nonlocal preview_photo
        image = np.array(matrix, dtype=np.uint8) * 255
        image = Image.fromarray(image, mode='L')
        image = image.resize((200, 200), Image.ANTIALIAS)
        preview_photo = ImageTk.PhotoImage(image)
        preview_label.config(image=preview_photo)

    def load_selected_preset():
        selected_preset = preset_listbox.get(preset_listbox.curselection())
        loaded_matrix = load_matrix_from_dat(os.path.join(presets_directory, selected_preset))
        global matrix
        matrix = loaded_matrix
        root_load.destroy()

    root_load = tk.Toplevel(root)
    root_load.title("Load Preset")

    # Create a listbox to display the names of preset files
    preset_listbox = tk.Listbox(root_load, width=30, height=10)
    preset_listbox.pack(side=tk.LEFT, padx=10, pady=10)
    for file in preset_files:
        preset_listbox.insert(tk.END, file)

    # Bind the listbox selection to the preview update function
    preset_listbox.bind("<<ListboxSelect>>", on_preset_selected)

    # Create the preview frame on the right side
    preview_frame = tk.Frame(root_load, width=200, height=200, bd=1, relief=tk.SOLID)
    preview_frame.pack(side=tk.RIGHT, padx=10, pady=10)

    # Load and display the default image on the preview frame
    example_image = Image.open("path_to_example_image.png")  # Replace with your example image
    example_image = example_image.resize((200, 200), Image.ANTIALIAS)
    preview_photo = ImageTk.PhotoImage(example_image)
    preview_label = tk.Label(preview_frame, image=preview_photo)
    preview_label.pack()

    # Create the "Load preset" button
    load_button = tk.Button(root_load, text="Load Preset", command=load_selected_preset)
    load_button.pack(pady=10)

def main():
    # Your existing GUI elements here...

    # Create a button for loading a preset
    load_button = tk.Button(root, text="Load", command=load_preset)
    load_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
