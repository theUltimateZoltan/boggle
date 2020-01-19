from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
from boggle import GameRunner


class Screen:
    def __init__(self, board):
        self._init_graphics(board)
        self._board = board

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
        self.__wordplace = self._build_wordplace(mid_sec)
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
        if self._board.check_valid_position(i, j):
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