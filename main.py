from controls import *
from constans import *

if __name__ == "__main__":
    # start game
    board_draw = Board()
    #board_draw.display_field()
    board_draw.sql_request(CREATE_TABLE)

    tic_tac_root.mainloop()
