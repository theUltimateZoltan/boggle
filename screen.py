from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image


class Screen:
    def __init__(self):
        self._init_graphics()

    def _init_graphics(self):
        self._root = Tk()
        self._root.title("Boggle Game!")
        self._root.config(bg="white")
        self._root.resizable(0, 0)  # don't allow resizing
        self._root.geometry("1100x700")
        # TODO - add icon

        # bind all main sections
        left_sec = Frame(self._root, width=300, bg="white")
        mid_sec = Frame(self._root, width=500, bg="white")
        right_sec = Frame(self._root, width=300, bg="white")

        right_sec.pack_propagate(False)
        mid_sec.pack_propagate(False)
        left_sec.pack_propagate(False)

        left_sec.pack(fill=Y, side=LEFT)
        mid_sec.pack(fill=Y, side=LEFT)
        right_sec.pack(fill=Y, side=LEFT)

        self.__correct, self.__wrong = self._build_lists(right_sec)

        self.build_left_frame(left_sec)

    def build_left_frame(self, fr):
        # divide left frame into 2 sub-frames
        top_frame = Frame(fr, height=200, width=300, bg="white")
        bottom_frame = Frame(fr, height=900, width=300, bg="white")
        top_frame.pack_propagate(False)
        bottom_frame.pack_propagate(False)
        top_frame.pack(fill=Y)
        bottom_frame.pack(fill=Y, side=BOTTOM)

        # draw logo and statistics box
        self.draw_logo(top_frame)
        self.draw_stats_box(bottom_frame)

    def draw_logo(self, fr):
        load = Image.open("style/bog_logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(fr, image=render)
        img.image = render
        img.place(x=0, y=0)

    def draw_stats_box(self, fr):
        font = Font(family="Segoe UI", size=12)
        title_font = Font(family="Segoe UI", size=14)

        box = Frame(fr, height=230, width=230, bg="white", highlightthickness=1, highlightbackground="#000")
        box.pack_propagate(False)
        box.pack()
        box_title = Label(box, bg="#1ABCB4", font=title_font, fg="#FFF", text="Time")
        box_title.pack(fill=X)

        # add start button
        restart_btn = Button(box, text="Start", bg="#1ABCB4", font=font, fg="white", width=7, activebackground="white")
        restart_btn.pack(side=BOTTOM, pady=15)

        self.draw_time_and_score(box)

    def draw_time_and_score(self, fr):
        pass

    def _build_lists(self, root):
        """
        Build graphics for correct\wrong lists initial state
        :return: Tuple (correct content, wrong content)
        """
        # define fonts
        font = Font(family="Segoe UI", size=14)
        title_font = Font(family="Segoe UI", size=14)

        correct = Frame(root, height=250, width=230, highlightthickness=1, highlightbackground="#000", bg="white")
        wrong = Frame(root, height=250, width=230, highlightthickness=1, highlightbackground="#000", bg="white")
        correct.pack_propagate(False)
        wrong.pack_propagate(False)
        correct.pack(pady=50)
        wrong.pack(pady=10)

        correct_title = Label(correct, bg="#1ABCB4", font=title_font, fg="#FFF", text="Correct")
        wrong_title = Label(wrong, bg="#FF6D6D", font=title_font, fg="#FFF", text="Wrong")
        correct_title.pack(fill=X)
        wrong_title.pack(fill=X)

        correct_content = Label(correct, fg="#1ABCB4", font=font, bg="white")
        wrong_content = Label(wrong, fg="#FF6D6D", font=font, bg="white")
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

    def start_screen(self):
        mainloop()

    def end_game(self):
        """
        This ends the current game.
        """
        self._root.destroy()
        self._root.quit()