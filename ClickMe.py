import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.withdraw()