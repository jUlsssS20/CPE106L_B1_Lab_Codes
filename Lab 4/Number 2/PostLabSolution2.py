import tkinter as tk
from tkinter import filedialog

with filedialog.askopenfile(title="Select a text file", filetypes=[("text file", "*.txt")]) as file_dialog:
    if file_dialog:
        file_path = file_dialog.name
        print(file_path)    