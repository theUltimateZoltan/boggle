from tkinter import *
from tkinter.font import Font
from boggle_utilities import Utilities
from PIL import ImageTk, Image
from boggle_config import GameConfig as Cfg


class BoggleApp:  # Runner and Graphics Unit

    def __init__(self):
        self.__util = Utilities(self)
        self.__board = self.__util.get_board()
        self.__root = Tk()
        self._stats_box = None
        self.__time = [None, Cfg.GAME_TIME]
        self.__score = None
        self.__start_btn = None
        self.init_graphics(self.__util.get_board())

    def init_graphics(self, board):
        self.__root.title("Boggle Game!")
        self.__root.config(bg="white")
        self.__root.resizable(0, 0)
        self.__root.geometry("1100x700")
        self.__root.iconbitmap("style/game_ico.ico")
        self.build_main_frames(board)

    def build_main_frames(self, board):

        left_sec = Frame(self.__root, width=300, height=300, bg="#FFF")
        mid_sec = Frame(self.__root, width=500, height=700, bg="#FFF")
        right_sec = Frame(self.__root, width=300, height=700, bg="#FFF")

        right_sec.pack_propagate(False)
        mid_sec.pack_propagate(False)
        left_sec.pack_propagate(False)

        left_sec.pack(fill=Y, side=LEFT)
        mid_sec.pack(fill=Y, side=LEFT)
        right_sec.pack(fill=Y, side=LEFT)

        self.__correct, self.__wrong = self._build_lists(right_sec)
        # build message bar before board
        self._msg_bar = self._build_message_bar(mid_sec)
        # build board at center
        self._board_buttons = list()
        self.__boardframe = self._build_board(board, mid_sec)
        # word place under the board
        self.__wordplace, self.__add_word_button = self._build_wordplace(mid_sec)

        # time and score labels
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
        self._stats_box = Frame(fr, height=230, width=230, bg="white",
                    highlightthickness=1, highlightbackground="#000")
        self._stats_box.pack_propagate(False)
        self._stats_box.pack()
        box_title = Label(self._stats_box, bg="#1ABCB4", font=title_font, fg="#FFF",
                          text="Time              Score")
        box_title.pack(fill=X)

        self.add_start_button(self._stats_box)

        # draw time and score
        self.draw_time(self._stats_box), self.draw_score(self._stats_box)

    def add_start_button(self, fr):
        font = Font(family="Segoe UI", size=12)

        self.__start_btn = Button(fr, text="Start", bg="#1ABCB4", font=font,
                             fg="white", width=7, activebackground="white",
                           command=self.start_play)
        self.__start_btn.pack(side=BOTTOM, pady=12)

    def add_restart_button(self):
        self.__start_btn["text"] = "Restart"
        self.__start_btn["command"] = self.restart_game

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
        self.__time[0] = Label(time_lbl, text="3:00", font=font, bg="white", fg="black")
        self.__time[0].pack()

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
        self.__score = Label(scr_lbl, text="0", font=font, bg="white", fg="black")
        self.__score.pack()

    def update_score(self, score):
        self.__score["text"] = str(score)

    def time_on(self):
        time_lbl, time_left = self.__time[0], self.__time[1]
        if not time_left:
            self.__util.times_up()
            return

        self.__time[1] -= 1

        # build text in minute format
        minutes = str(time_left // 60)
        sec = time_left % 60
        seconds = str(sec) if sec >= 10 else "0"+str(sec)

        time_lbl["text"] = "{0}:{1}".format(minutes, seconds)
        self.__root.after(1000, self.time_on)

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

    def _build_message_bar(self, root):
        """
        Build the top message bar
        :return: Label
        """
        fr = Frame(root, bg="#FFF")
        font = Font(size=15, family="Segoe UI")
        label = Label(fr, text=Cfg.welcome_message, width=30, height=2, bg="#1ABCB4", fg="#FFF", font=font)
        label.pack_propagate(False)
        label.pack(fill=X, pady=50)
        fr.pack()
        return label

    def message(self, msg):
        self._msg_bar["text"] = msg

    def activate_board_and_addword(self):
        """
        activate the buttons we disabled when initialising
        :return: None
        """
        for button in self._board_buttons:
            button["bg"] = "#FFF"
            button["state"] = NORMAL
        self.__add_word_button["state"] = NORMAL

    def _build_board(self, board, root):
        """
        Build the board of the game using a board object
        :return: Frame
        """
        b_font = Font(family="Segoe UI", size=23)
        button_style = {"bg": "#1ABCB4", "fg": "#1ABCB4", "width": 4, "height": 1, "font": b_font,
                        "borderwidth": "0", "disabledforeground": "#1ABCB4" }

        matrix = board.get_board()
        fr = Frame(root)
        for i in range(len(matrix)):
            rowframe = Frame(fr)
            for j in range(len(matrix[0])):
                blueframe = Frame(rowframe, highlightbackground="#1ABCB4", highlightthickness=3)
                button = Button(blueframe, text=matrix[i][j], **button_style)

                # disable buttons untill time starts
                button["state"] = DISABLED

                button["command"] = lambda i=i, j=j, b=button: self._pressed_letter(i, j, b)
                self._board_buttons.append(button)
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
        if (i, j) in self.__board.get_selected_indices():
            if self.__board.cancel_letter(i, j):
                button["bg"] = "#FFF"
                button["fg"] = "#1ABCB4"

        elif self.__board.add_letter((i, j)):
            button["bg"] = "#1ABCB4"
            button["fg"] = "#FFF"

        self.__wordplace["text"] = self.__board.get_current_word()

    def _build_wordplace(self, root):
        """
        Build the line of text in which a work will be assembled by the user.
        :param root: root of the frame
        :return: label
        """
        fr = Frame(root, width=300, height=50)
        fr.pack_propagate(False)

        #label
        font = Font(family="Segoe UI", size=20)
        label = Label(fr, bg="#1ABCB4", fg="#FFF", width=17, font=font)
        label.pack(side="left", fill=BOTH)

        #button
        b_font = Font(family="Segoe UI", size=20, weight="bold")
        blueframe=Frame(fr, highlightbackground="#1ABCB4", highlightthickness=3)
        add_word_button = Button(blueframe, text="+", bg="#FFF", fg="#1ABCB4",font=b_font, borderwidth=0, width=2)
        add_word_button["command"] = self._add_word_pressed
        add_word_button["state"] = DISABLED
        add_word_button.pack()
        blueframe.pack(side=RIGHT)

        fr.pack(pady=20)
        return label, add_word_button

    def _add_word_pressed(self):
        """
        called when word is added
        :return: None
        """
        word = self.__board.get_current_word()
        valid, message = self.__util.add_word(word)

        # reset board
        self.__board.reset_selection()
        # graphically reset board
        self.__wordplace["text"] = ""

        for button in self._board_buttons:
            button["fg"] = "#1ABCB4"
            button["bg"] = "#FFF"

        # add to the list
        self.add_word(word, valid)

        self.message(message)

    def clear_lists(self):
        """
        Clear all contents from correct/wrong lists
        :return: None
        """
        self.__correct["text"] = ""
        self.__wrong["text"] = ""

    def start_play(self):
        self.time_on()
        self.add_restart_button()

    def restart_game(self):
        self.__util.reset()
        self.__time[1] = Cfg.GAME_TIME
        self.start_play()

    def run(self):
        self.__root.mainloop()


if __name__ == '__main__':
    my_app = BoggleApp()
    my_app.run()
