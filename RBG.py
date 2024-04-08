import tkinter as tk
from tkinter import colorchooser

def change_keyboard_rgb(color_hex):
    # This is where you'd implement the code to change the RGB colors.
    # Since there's no universal way to do this, we're just printing the color.
    print(f"Changing keyboard RGB to {color_hex}")

def choose_color():
    # Open a color chooser dialog and set the chosen color as keyboard RGB
    color_code = colorchooser.askcolor(title ="Choose color")
    change_keyboard_rgb(color_code[1])

# Setting up the GUI
root = tk.Tk()
root.title("Keyboard RGB Changer")

# Instructions label
instructions_label = tk.Label(root, text="Choose your keyboard RGB color:")
instructions_label.pack(pady=20)

# Button to choose color
choose_color_button = tk.Button(root, text="Choose Color", command=choose_color)
choose_color_button.pack()

root.mainloop()
