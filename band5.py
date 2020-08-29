from tkinter import *

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

langas=Tk()
langas.title("Kryziukai/Nuliukai")

for box in board:
    button = Button(langas, text=box)
    button.pack()

langas.mainloop()