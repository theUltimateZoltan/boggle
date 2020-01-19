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
        # self._root.iconbitmap('path')
        # TODO - add icon

        labelframe = LabelFrame(self._root, text="This is a LabelFrame", bg="blue")
        labelframe.pack(side=LEFT, fill="both")
        labelframe2 = LabelFrame(self._root, text="This is a LabelFrame", bg="red")
        labelframe2.pack(side=LEFT, fill="both")
        labelframe3 = LabelFrame(self._root, text="This is a LabelFrame", bg="green")
        labelframe3.pack(side=LEFT, fill="both")

        left = Label(labelframe, text="Inside the LabelFrame")
        left.pack()

        left = Label(labelframe2, text="Inside the LabelFrame")
        left.pack()

        left = Label(labelframe3, text="Inside the LabelFrame")
        left.pack()



    def left_sec(self, fr):
        button1 = Button(fr, text="hi")
        button1.pack()

    def mid_sec(self, fr):
        button1 = Button(fr, text="hi")
        button1.pack()

    def _build_lists(self, root):
        """
        Build graphics for correct\wrong lists initial state
        :return: Tuple (correct content, wrong content)
        """
        # define fonts
        c_font = Font(family="Segoe UI", size=14)
        w_font = Font(family="Segoe UI", size=14)
        c_title_font = Font(family="Segoe UI", size=18)
        w_title_font = Font(family="Segoe UI", size=18)

        correct = Frame(root, height="200")
        wrong = Frame(root, height="200")
        correct.pack(expand=False)
        wrong.pack(expand=False)
        correct_title = Text(correct, height=1, bg="#1ABCB4", font=c_title_font, fg="#FFF")
        correct_title.insert(END, "Correct")
        wrong_title = Text(wrong, height=1, bg="#FF6D6D", font=w_title_font, fg="#FFF")
        wrong_title.insert(END, "Wrong")
        correct_title.pack(fill=X)
        wrong_title.pack(fill=X)
        correct_content = Text(correct, fg="#1ABCB4", font=c_font)
        wrong_content = Text(wrong, fg="#FF6D6D", font=w_font)
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
            self.__correct.insert(END, word+"\n")
        else:
            self.__wrong.insert(END, word + "\n")

    @staticmethod
    def start_screen():
        mainloop()

    def end_game(self):
        """
        This ends the current game.
        """
        self._root.destroy()
        self._root.quit()
