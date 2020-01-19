from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image


class Screen:
    def __init__(self, runner, board):
        self._init_graphics(board)
        self._board = board
        self.runner = runner

    def _init_graphics(self, board):
        self._root = Tk()
        self._root.title("Boggle Game!")
        self._root.config(bg="white")
        self._root.resizable(0, 0)  # don't allow resizing
        self._root.geometry("1100x700")
        # TODO - add icon

        # bind all main sections
        left_sec = Frame(self._root, width=300, height=300, bg="#FFF")
        mid_sec = Frame(self._root, width=500, height=700, bg="#FFF")
        right_sec = Frame(self._root, width=300, height=700, bg="#FFF")

        right_sec.pack_propagate(False)
        mid_sec.pack_propagate(False)
        left_sec.pack_propagate(False)

        left_sec.pack(fill=Y, side=LEFT)
        mid_sec.pack(fill=Y, side=LEFT)
        right_sec.pack(fill=Y, side=LEFT)

        # TODO - add icon
        self.__correct, self.__wrong = self._build_lists(right_sec)

        # build board at center
        self.__boardframe = self._build_board(board, mid_sec)
        # word place under the board
        self._build_wordplace(mid_sec)
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
        img = Label(fr, image=render, borderwidth=0, highlightthickness=0)
        img.image = render
        img.place(x=0, y=0)

    def draw_stats_box(self, fr):
        font = Font(family="Segoe UI", size=12)
        title_font = Font(family="Segoe UI", size=14)

        # draw stats box
        box = Frame(fr, height=230, width=230, bg="white",
                    highlightthickness=1, highlightbackground="#000")
        box.pack_propagate(False)
        box.pack()
        box_title = Label(box, bg="#1ABCB4", font=title_font, fg="#FFF",
                          text="Time              Score")
        box_title.pack(fill=X)

        # add start button
        restart_btn = Button(box, text="Start", bg="#1ABCB4", font=font,
                             fg="white", width=7, activebackground="white")
        restart_btn.pack(side=BOTTOM, pady=12)

        # draw time and score
        time = self.draw_time(box)
        score = self.draw_score(box)

    def draw_time(self, fr):
        font = Font(family="Segoe UI", size=20)

        # create time label
        time_label = Label(fr, bg="white", width=16, height=10)
        time_label.pack(side=LEFT)
        time_label.pack_propagate(False)

        # add time icon
        time_img = Image.open("style/time.png")
        time_img = time_img.resize((60, 62), Image.ANTIALIAS)
        render_time = ImageTk.PhotoImage(time_img)
        t_img = Label(time_label, image=render_time, borderwidth=0,
                      highlightthickness=0)
        t_img.image = render_time
        t_img.place(x=25, y=25)

        # add time seconds
        time_lbl = Label(time_label, width=8, height=2, bg="white")
        time_lbl.pack(side=BOTTOM)
        time_lbl.propagate(False)
        time = Label(time_lbl, text="3:00", font=font, bg="white", fg="black")
        time.pack()
        return time

    def draw_score(self, fr):
        font = Font(family="Segoe UI", size=20)

        # create score label
        score_label = Label(fr, bg="white", width=16, height=10)
        score_label.pack(side=RIGHT)
        score_label.pack_propagate(False)

        # add score icon
        score_img = Image.open("style/score.png")
        score_img = score_img.resize((60, 62), Image.ANTIALIAS)
        render_score = ImageTk.PhotoImage(score_img)
        s_img = Label(score_label, image=render_score, borderwidth=0,
                      highlightthickness=0)
        s_img.image = render_score
        s_img.place(x=25, y=25)

        # add points amount
        scr_lbl = Label(score_label, width=6, height=2, bg="white")
        scr_lbl.pack(side=BOTTOM)
        scr_lbl.propagate(False)
        score = Label(scr_lbl, text="0", font=font, bg="white", fg="black")
        score.pack()
        return score

    def update_score(self, points=0):
        pass

    def update_time(self):
        pass

    def _build_lists(self, root):
        """
        Build graphics for correct\wrong lists initial state
        :return: Tuple (correct content, wrong content)
        """
        # define fonts
        font = Font(family="Segoe UI", size=16)
        title_font = Font(family="Segoe UI", size=18)

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

    def _build_board(self, board, root):
        """
        Build the board of the game using a board object
        :return: Frame
        """
        b_font = Font(family="Segoe UI", size=23)
        button_style = {"bg": "#FFF", "fg": "#1ABCB4", "width": 3, "height": 1, "font": b_font,
                        "borderwidth":"0"}

        matrix = board.get_board()
        fr = Frame(root)
        for i in range(len(matrix)):
            rowframe = Frame(fr)
            for j in range(len(matrix[0])):
                blueframe = Frame(rowframe, highlightbackground="#1ABCB4", highlightthickness=3)
                button = Button(blueframe, text=matrix[i][j], **button_style)
                button["command"] = lambda i=i, j=j, b=button: self._pressed_letter(i, j, b)
                button.pack()
                blueframe.pack(side=LEFT, padx=2, pady=2)
            rowframe.pack()
        fr.pack()
        return fr

    def _pressed_letter(self, i, j, button):
        """
        invoked when a button is pressed
        :param i: button row
        :param j: button col
        :return: None
        """
        if (i, j) in self._board.get_selected_indices():
            if self._board.cancel_letter(i, j):
                button["bg"] = "#FFF"
                button["fg"] = "#1ABCB4"

        elif self._board.add_letter((i, j)):
            button["bg"] = "#1ABCB4"
            button["fg"] = "#FFF"

    def _build_wordplace(self, root):
        """
        Build the line of text in which a work will be assembled by the user.
        :param root: root of the frame
        :return: label
        """
        fr = Frame(root, width=300, height=50)
        fr.pack_propagate(False)

        #label
        label = Label(fr, bg="#1ABCB4", fg="#FFF", width=36)
        label.pack(side="left", fill=BOTH)

        #button
        b_font = Font(family="Segoe UI", size=20, weight="bold")
        blueframe=Frame(fr, highlightbackground="#1ABCB4", highlightthickness=3)
        add_word_button = Button(blueframe, text="+", bg="#FFF", fg="#1ABCB4",font=b_font, borderwidth=0, width=2)
        add_word_button["command"] = self._add_word_pressed
        add_word_button.pack()
        blueframe.pack(side=RIGHT)

        fr.pack(pady=20)

    def _add_word_pressed(self):
        """
        called when work is added
        :return: None
        """
        pass

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