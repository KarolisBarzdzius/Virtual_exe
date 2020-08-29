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
nuli=[0]
pirm=[1]
antr=[2]
trec=[3]
ketv=[4]
penk=[5]
sest=[6]
sept=[7]
astu=[8]


game_still_going=True
winner="niekas"
current_player = "X"


def play_game():
    display_board()
    while game_still_going:


        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == "niekas":
        print("Tie.")






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
        winner = "niekas"


def check_rows():
    global game_still_going

    row_1 = nuli == pirm == antr != "-"
    row_2 = trec == ketv == penk != "-"
    row_3 = sest == sept == astu != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return nuli
    elif row_2:
        return trec
    elif row_3:
        return sest
    else:
        return "niekas"


def check_columns():
    global game_still_going

    column_1 = nuli == trec == sest != "-"
    column_2 = pirm == ketv == sept != "-"
    column_3 = antr == penk == astu != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return nuli
    elif column_2:
        return pirm
    elif column_3:
        return antr
    else:
        return "niekas"


def check_diagonals():
    global game_still_going

    diagonal_1 = nuli == ketv == astu != "-"
    diagonal_2 = antr == ketv == sest != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return nuli
    elif diagonal_2:
        return antr
    else:
        return "niekas"


def check_for_tie():
    global game_still_going

    if "-" not in (nuli,pirm,antr,trec,ketv,penk,sest,sept,astu):
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
    nuli.config(text=f"{current_player}")

def pasirinkta1():
    pirm["text"]=(f"{current_player}")

def pasirinkta2():
    antr["text"]=(f"{current_player}")

def pasirinkta3():
    trec["text"]=(f"{current_player}")

def pasirinkta4():
    ketv["text"]=(f"{current_player}")

def pasirinkta5():
    penk["text"]=(f"{current_player}")

def pasirinkta6():
    sest["text"]=(f"{current_player}")

def pasirinkta7():
    sept["text"]=(f"{current_player}")

def pasirinkta8():
    astu["text"]=(f"{current_player}")


def display_board():
    nuli=Button(langas,text="-",command=pasirinkta0).grid(row=0,column=0)
    pirm=Button(langas,text="-",command=pasirinkta1).grid(row=0,column=1)
    antr=Button(langas,text="-",command=pasirinkta2).grid(row=0,column=2)
    trec=Button(langas,text="-",command=pasirinkta3).grid(row=1,column=0)
    ketv=Button(langas,text="-",command=pasirinkta4).grid(row=1,column=1)
    penk=Button(langas,text="-",command=pasirinkta5).grid(row=1,column=2)
    sest=Button(langas,text="-",command=pasirinkta6).grid(row=2,column=0)
    sept=Button(langas,text="-",command=pasirinkta7).grid(row=2,column=1)
    astu=Button(langas,text="-",command=pasirinkta8).grid(row=2,column=2)



langas=Tk()
langas.title("Kryziukai/Nuliukai")

status=Label(langas,text="Status",bd=1,relief=SUNKEN,anchor=W).grid(row=3,columnspan=3)
startas=Button(langas,text="Pradeti",command=play_game).grid(row=3,columnspan=3)












langas.mainloop()

