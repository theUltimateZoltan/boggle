from tkinter import *
from tkinter.font import Font

# frames, widgets, button, canvas, entry, label, menu, text, scroll bar, Listbox


class Screen:
    def __init__(self):
        self._init_graphics()

    def _init_graphics(self):
        self._root = Tk()
        self._root.title("Boggle Game!")
        self._root.config(bg="white")
        self._root.resizable(0, 0)  # don't allow resizing
        self._root.geometry("1100x700")
        # bind all main sections
        left_sec = Frame(self._root, width=250, height=300)
        mid_sec = Frame(self._root, width=500, height=700)
        right_sec = Frame(self._root, width=250, height=700, bg="#FFF")

        right_sec.pack_propagate(False)
        mid_sec.pack_propagate(False)
        left_sec.pack_propagate(False)

        left_sec.pack(fill=Y, side=LEFT)
        mid_sec.pack(fill=Y, side=LEFT, padx=50)
        right_sec.pack(fill=Y, side=LEFT)

        # TODO - add icon
        self.__correct, self.__wrong = self._build_lists(right_sec)

        b = Button(left_sec, text="try")
        b.pack()

        c = Button(mid_sec, text="mid")
        c.pack()

    def _build_lists(self, root):
        """
        Build graphics for correct\wrong lists initial state
        :return: Tuple (correct content, wrong content)
        """
        # define fonts
        font = Font(family="Segoe UI", size=16)
        title_font = Font(family="Segoe UI", size=18)

        correct = Frame(root, height=250, width=230, highlightthickness=1, highlightbackground="#000")
        wrong = Frame(root, height=250, width=230, highlightthickness=1, highlightbackground="#000")
        correct.pack_propagate(False)
        wrong.pack_propagate(False)
        correct.pack(pady=50)
        wrong.pack(pady=10)

        correct_title = Label(correct, bg="#1ABCB4", font=title_font, fg="#FFF", text="Correct")
        wrong_title = Label(wrong, bg="#FF6D6D", font=title_font, fg="#FFF", text="Wrong")
        correct_title.pack(fill=X)
        wrong_title.pack(fill=X)

        correct_content = Label(correct, fg="#1ABCB4", font=font)
        wrong_content = Label(wrong, fg="#FF6D6D", font=font)
        correct_content.pack(fill=X)
        wrong_content.pack(fill=X)

        return correct_content, wrong_content



    def add_word(self, word, correct):
        """
        add a word to the correct list
        :param word: word to add
        :param correct: is the word correct? True/False
        :return: None
        """
        if correct:
            self.__correct["text"] += word+"\n"
        else:
            self.__wrong["text"] += word+"\n"

    def clear_lists(self):
        """
        Clear all contents from correct/wrong lists
        :return: None
        """
        self.__correct["text"] = ""
        self.__wrong["text"] = ""

    def start_screen(self):
        mainloop()

    def end_game(self):
        """
        This ends the current game.
        """
        self._root.destroy()
        self._root.quit()