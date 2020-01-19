from tkinter import *
from PIL import ImageTk, Image

# frames, widgets, button, canvas, entry, label, menu, text, scroll bar, Listbox
# Red : #FF6D6D
# Turquoise : #1ABCB4


class Screen:
    def __init__(self):
        self._init_graphics()

    def _init_graphics(self):
        self._root = Tk()
        self._root.geometry("1100x700")
        self._root.title("Boggle Game!")
        self._root.config(bg="white")
        self._root.resizable(0, 0)

        f1 = Frame(self._root)
        f2 = Frame(self._root)
        f3 = Frame(self._root)
        f1.pack(side=LEFT)
        f2.pack(side=LEFT)
        f3.pack(side=LEFT)
        button1 = Button(f1, text="Push me", fg="red")
        button2 = Button(f2, text="Push me", fg="blue")
        button3 = Button(f3, text="Push me", fg="green")
        button1.pack()
        button2.pack()
        button3.pack()

    def start_screen(self):
        mainloop()

    def end_game(self):
        """
        This ends the current game.
        """
        self._root.destroy()
        self._root.quit()
