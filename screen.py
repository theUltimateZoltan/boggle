from tkinter import *

# frames, widgets, button, canvas, entry, label, menu, text, scroll bar, Listbox


class Screen:
    def __init__(self):
        self._init_graphics()

    def _init_graphics(self):
        self._root = Tk()
        self._root.title("Boggle Game!")
        self._root.config(bg="white")
        self._root.resizable(0, 0)  # don't allow resizing
        # TODO - add icon

    def build_lists(self):
        """
        Build graphics for correct\wrong lists initial state
        :return: tuple (correct-list, wrong-list)
        """
        correct = Text(self._root, height=530, width=120, fg="#1ABCB4", font="Segoe ui")
        wrong = Text(self._root, height=530, width=120, bg="#FF6D6D", font="Segoe ui")
        correct.pack()
        wrong.pack()
        correct_title = Text(correct, height=30, bg="#1ABCB4", font="Segoe ui", fg="#FFF")
        wrong_title = Text(wrong, height=30, bg="#1ABCB4", font="Segoe ui", fg="#FFF")
        correct_title.pack(fill=X)

    def start_screen(self):
        mainloop()

    def end_game(self):
        """
        This ends the current game.
        """
        self._root.destroy()
        self._root.quit()