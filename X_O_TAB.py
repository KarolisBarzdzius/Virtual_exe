# Meniu
    # Naujas zaidimas(Istrinti)
    # Uzdaryti zaidima
    # Paskutinio zaidimo rezultatas
# Zaidimo Lentos atvaizdavimas
# NumPado mygtuku regavimas lentoje
# NumPado mygtuku atvaizdavimas????
# Zaidimo lentos vietos paspaudimas/regavimas
# Pranesimas apacioje kas laimejo arba kad lygiosios
# Kieno eile
from tkinter import *

langas=Tk()
langas.title("Kryziukai/Nuliukai")

board = ["-", "-", "-",
         "-", "=", "-",
         "-", "-", "-"]


game_still_going=True
winner=None
current_player = "X"






def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[4] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


def check_diagonals():
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


def check_for_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def pasirinkta0():
    global board
    print(board)


def pasirinkta1():
    board[1]=current_player


def pasirinkta2():
    board[2]=current_player


def pasirinkta3():
    board[3]=current_player


def pasirinkta4():
    board[4]=current_player


def pasirinkta5():
    board[5]=current_player


def pasirinkta6():
    board[6]=current_player


def pasirinkta7():
    board[7]=current_player


def pasirinkta8():
    board[8]=current_player


board[0]=Button(langas,text=board[0],command=pasirinkta0).grid(row=0,column=0)
board[1]=Button(langas,text=aaa,command=pasirinkta1).grid(row=0,column=1)
board[2]=Button(langas,text=board[2],command=pasirinkta2).grid(row=0,column=2)
board[3]=Button(langas,text=board[3],command=pasirinkta3).grid(row=1,column=0)
board[4]=Button(langas,text=board[4],command=pasirinkta4).grid(row=1,column=1)
board[5]=Button(langas,text=board[5],command=pasirinkta5).grid(row=1,column=2)
board[6]=Button(langas,text=board[6],command=pasirinkta6).grid(row=2,column=0)
board[7]=Button(langas,text=board[7],command=pasirinkta7).grid(row=2,column=1)
board[8]=Button(langas,text=board[8],command=pasirinkta8).grid(row=2,column=2)



def play_game():
    while game_still_going:
        check_if_game_over()
        flip_player()
    else:
        if winner == "X" or winner == "O":
            print(winner + " won.")
        elif winner == None:
            print("Tie.")


status=Label(langas,text="Status",bd=1,relief=SUNKEN,anchor=W).grid(row=3,columnspan=3)
startas=Button(langas,text="Pradeti",command=play_game).grid(row=3,columnspan=3)




langas.mainloop()

