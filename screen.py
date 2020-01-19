import tkinter as tk

# frames, widgets, button, canvas, entry, label, menu, text, scroll bar, Listbox


class Screen:
    def __init__(self):
        self._init_graphics()

    def _init_graphics(self):
        self._root = tk.Tk()
        self._root.title("Boggle Game!")
        self._root.config(bg="white")
        # TODO - add icon

    def start_screen(self):
        tk.mainloop()

    def end_game(self):
        """
        This ends the current game.
        """
        self._root.destroy()
        self._root.quit()
