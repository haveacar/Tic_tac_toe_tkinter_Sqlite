import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import sqlite3
from constans import *


class Board:

    tic_tac_root = Tk()

    # Display set up
    tic_tac_root.title("Tic Tac Toe")
    tic_tac_root.geometry("800x700+10+100")
    tic_tac_root.config(bg='#80FF80')
    tic_tac_root.resizable(False, False)

    # frames
    game_play_frame = Frame()
    game_play_frame.grid(column=0, row=2, sticky="w")

    top_frame = Frame(bg='#80FF80')
    top_frame.grid(column=0, row=0, columnspan=2, sticky="w")

    stat_frame = Frame(bg='#80FF80')
    stat_frame.grid(column=1, row=1, sticky="s")

    # top buttons and label
    name_l = Label(top_frame, text="Tic Tac Toe", font=('Comic Sans MS', 25, 'bold'), bg='#80FF80', fg='#363535')
    name_l.grid(column=0, row=0)
    name_n = Label(top_frame, text="©Daniel Govnir", font=('Comic Sans MS', 20), bg='#80FF80', fg='white')
    name_n.grid(column=4, row=0)

    def __init__(self):


        # win counting statistic
        self.winner_counting = {
            "name": "PLAYER",
            "user": 0,
            "computer": 0
        }



        self.new_game = Button(Board.top_frame, text="New Game", command=self.push_new,
                               font=('Comic Sans MS', 20))
        self.new_game.grid(row=0, column=1, padx=10)
        self.load_btn = Button(Board.top_frame, text="Load Game", command=self.push_load,
                               font=('Comic Sans MS', 20))
        self.load_btn.grid(row=0, column=2, padx=10)
        self.save_btn = Button(Board.top_frame, text="Save Game", command=self.push_save,
                               font=('Comic Sans MS', 20))
        self.save_btn.grid(row=0, column=3, padx=10)

        # win combinations
        self.win_comp = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

        # buttons
        self.btn_1 = Button(Board.game_play_frame, text=" ", command=lambda: self.push_bt(self.btn_1, "X", 0),
                            font=('Comic Sans MS', 35, 'bold',), disabledforeground="white")
        self.btn_2 = Button(Board.game_play_frame, text=" ", command=lambda: self.push_bt(self.btn_2, "X", 1),
                            font=('Comic Sans MS', 35, 'bold'), disabledforeground="white")
        self.btn_3 = Button(Board.game_play_frame, text=" ", command=lambda: self.push_bt(self.btn_3, "X", 2),
                            font=('Comic Sans MS', 35, 'bold',), disabledforeground="white")
        self.btn_4 = Button(Board.game_play_frame, text=" ", command=lambda: self.push_bt(self.btn_4, "X", 3),
                            font=('Comic Sans MS', 35, 'bold',), disabledforeground="white")
        self.btn_5 = Button(Board.game_play_frame, text=" ", command=lambda: self.push_bt(self.btn_5, "X", 4),
                            font=('Comic Sans MS', 35, 'bold',), disabledforeground="white")
        self.btn_6 = Button(Board.game_play_frame, text=" ", command=lambda: self.push_bt(self.btn_6, "X", 5),
                            font=('Comic Sans MS', 35, 'bold',), disabledforeground="white")
        self.btn_7 = Button(Board.game_play_frame, text=" ", command=lambda: self.push_bt(self.btn_7, "X", 6),
                            font=('Comic Sans MS', 35, 'bold',), disabledforeground="white")
        self.btn_8 = Button(Board.game_play_frame, text=" ", command=lambda: self.push_bt(self.btn_8, "X", 7),
                            font=('Comic Sans MS', 35, 'bold',), disabledforeground="white")
        self.btn_9 = Button(Board.game_play_frame, text=" ", command=lambda: self.push_bt(self.btn_9, "X", 8),
                            font=('Comic Sans MS', 35, 'bold',), disabledforeground="white")

        # list of buttons
        self.buttons_list = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7,
                             self.btn_8, self.btn_9]

        # labels
        self.label3 = Label(Board.stat_frame, text=f"{self.winner_counting.get('name')} 0",
                            font=('Comic Sans MS', 15, 'bold'), bg='#80FF80', fg='#363535')

        self.label4 = Label(Board.stat_frame, text="COMPUTER O", font=('Comic Sans MS', 15, 'bold'), bg='#80FF80',
                            fg='#363535')

        # new game
        self.name_input = Entry(Board.top_frame, relief=FLAT)
        self.label_input = Label(Board.top_frame, text="Your Name", font=('Comic Sans MS', 15, 'bold'), bg='#80FF80',
                                 fg='#363535')
        self.btn_new = Button(Board.top_frame, text="Enter", command=self.push_new_name, padx=4, pady=4,
                              font=('Comic Sans MS', 15))

        # computer choice list
        self.computer_turn_list = [x for x in range(9)]
        # game turn list
        self.game_turn_list = [None for x in range(9)]

        # load menu
        self.combobox = ttk.Combobox(Board.top_frame, values="none")
        self.btn_load_list = Button(Board.top_frame, text="Select", command=self.push_select_load, padx=4, pady=4,
                                    font=('Comic Sans MS', 15))

    def display_field(self):
        """
        func display play field
        """
        self.btn_1.grid(column=2, row=1, ipadx=70, ipady=70, sticky='snew')
        self.btn_2.grid(column=3, row=1, ipadx=70, ipady=70, sticky='snew')
        self.btn_3.grid(column=4, row=1, ipadx=70, ipady=70, sticky='snew')
        self.btn_4.grid(column=2, row=2, ipadx=70, ipady=70, sticky='snew')
        self.btn_5.grid(column=3, row=2, ipadx=70, ipady=70, sticky='snew')
        self.btn_6.grid(column=4, row=2, ipadx=70, ipady=70, sticky='snew')
        self.btn_7.grid(column=2, row=3, ipadx=70, ipady=70, sticky='snew')
        self.btn_8.grid(column=3, row=3, ipadx=70, ipady=70, sticky='snew')
        self.btn_9.grid(column=4, row=3, ipadx=70, ipady=70, sticky='snew')

        self.label3.grid(row=5, sticky='w')
        self.label4.grid(row=6, sticky='w')

    def push_bt(self, btn, turn, index):
        """
        Push button func
        :param btn: self.btn
        :param turn: str
        :param index: int
        """
        btn.config(text=turn)
        btn.config(state=DISABLED)
        self.computer_turn_list.remove(index)
        self.game_turn_list[index] = turn
        self.turn()

    def computer_push(self):
        """
        computer random push
        """
        if len(self.computer_turn_list) == 0:
            self.restore()
            # display no winner
            tkinter.messagebox.showinfo("Tic Tac Toe", "Standoff\nGame Over!")

        computer_choice = random.choice(self.computer_turn_list)
        self.buttons_list[computer_choice].config(text="O")
        self.buttons_list[computer_choice].config(state=DISABLED)
        self.computer_turn_list.remove(computer_choice)

        self.game_turn_list[computer_choice] = "O"

    def check_win(self):
        """
        check winner func
        :return: winner = True
        """

        for i in self.win_comp:
            # if winner User
            if self.game_turn_list[i[0]] == self.game_turn_list[i[1]] == self.game_turn_list[i[2]] == "X":
                # user statistic
                count = self.winner_counting.get("user")
                self.winner_counting["user"] = count + 1

                self.label3.config(text=f"{self.winner_counting.get('name')} X  {self.winner_counting.get('user')}")
                # display win message user
                tkinter.messagebox.showinfo("Tic Tac Toe", "Congratulation\nYou Win!")

                return True

            # if winner computer
            if self.game_turn_list[i[0]] == self.game_turn_list[i[1]] == self.game_turn_list[i[2]] == "O":
                count = self.winner_counting.get("computer")
                self.winner_counting["computer"] = count + 1
                self.label4.config(text=f"Computer O    {self.winner_counting.get('computer')}")
                # display win message computer
                tkinter.messagebox.showinfo("Tic Tac Toe", "Computer Win\nGame Over!")

                return True

    def restore(self):
        """
        restore buttons and list func
        """

        # computer choice list
        self.computer_turn_list = [x for x in range(9)]
        # game turn list
        self.game_turn_list = [None for x in range(9)]

        # restore buttons text
        for next_btn in self.buttons_list:
            next_btn['text'] = ' '
            next_btn.config(state="normal")

    def turn(self):
        """
        turn func
        """
        self.computer_push()
        if self.check_win():
            self.restore()

    def sql_request(self, n_cursor, query_result=False):
        """
        sql request func
        :param n_cursor: string sql request
        """

        try:
            with sqlite3.connect(DB_URL) as sqlite_connection:  # Connect to database
                # Create cursor object
                cursor = sqlite_connection.cursor()
                # Execute SQL query
                cursor.execute(n_cursor)
                # Fetch result
                if query_result:
                    res = cursor.fetchall()
                else:
                    res = None
                pass
                return res
        except sqlite3.Error as err:
            print(">>>>SQL error occurred", err)
        else:
            print("***Complete***")

    def push_new(self):
        """
        func display new game menu
        """
        self.label_input.grid(row=1, column=0, ipadx=5)
        self.name_input.grid(row=1, column=1, ipadx=5)
        self.btn_new.grid(row=2, column=1, ipadx=2)

    def push_new_name(self):
        """
        func print new game menu
        """
        result = self.name_input.get()  # input result
        self.winner_counting["name"] = result
        self.label3.config(text=f'{result} X')
        self.display_field()  # display game field

        # delete buttons
        self.new_game.config(state=DISABLED)
        self.label_input.destroy()
        self.name_input.destroy()
        self.btn_new.destroy()

    def push_load(self):
        #sql answer
        sql_answer = self.sql_request(SELECT_NAMES, query_result=True)

        # display combobox
        self.combobox.config(values=sql_answer)
        self.combobox.grid(column=2, row=2)
        self.btn_load_list.grid(column=2, row=3)



    def push_select_load(self):
        """
        from database load func
        :return:
        """

        # selection get
        selection = self.combobox.get()
        # sql request
        request = f'''SELECT * from "game stats"
                    where name  = '$name$';'''
        request = request.replace('$name$', selection)

        # sql answer
        res = self.sql_request(request, query_result=True)
        # replace user from data base
        self.winner_counting['name'] = res[0][0]
        self.winner_counting['user'] = res[0][1]
        self.winner_counting['computer'] = res[0][2]
        self.label3.config(text=f'{self.winner_counting.get("name")} X {self.winner_counting.get("user")}')
        self.label4.config(text=f"Computer O  {self.winner_counting.get('computer')}")

        # remove combobox
        self.combobox.grid_remove()
        self.combobox.grid_remove()
        self.btn_load_list.grid_remove()

        self.display_field()  # display game field



    def push_save(self):
        """
        func update database
        :return:
        """

        INSERT_SQL = f"""INSERT OR REPLACE INTO "game stats" ("name","user","computer") VALUES ("$name$",{self.winner_counting.get("user")}, {self.winner_counting.get("computer")});"""
        INSERT_SQL = INSERT_SQL.replace('$name$', f'{self.winner_counting.get("name")}')
        self.sql_request(INSERT_SQL)
        tkinter.messagebox.showinfo("Tic Tac Toe", "Saved")

        pass
