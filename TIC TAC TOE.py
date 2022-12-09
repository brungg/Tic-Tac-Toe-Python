from tkinter import *
from tkinter import ttk, messagebox

tk = Tk()
c = Canvas()
board = ["", "", "", "", "", "", "", "", ""]
quad = -1
player = "X"
message = ""

def label_maker(quad, t):
    match quad:
        case 1: ttk.Label(c, text=t).grid(row=1, column=1, padx=(166.666/2) - 10, pady=(166.666/2) - 10)
        case 2: ttk.Label(c, text=t).grid(row=1, column=2, padx=(166.666/2) - 5, pady=(166.666/2) - 10)
        case 3: ttk.Label(c, text=t).grid(row=1, column=3, padx=(166.666/2) - 5, pady=(166.666/2) - 10)
        case 4: ttk.Label(c, text=t).grid(row=2, column=1, padx=(166.666/2) - 5, pady=(166.666/2) - 10)
        case 5: ttk.Label(c, text=t).grid(row=2, column=2, padx=(166.666/2) - 5, pady=(166.666/2) - 10)
        case 6: ttk.Label(c, text=t).grid(row=2, column=3, padx=(166.666/2) - 5, pady=(166.666/2) - 10)
        case 7: ttk.Label(c, text=t).grid(row=3, column=1, padx=(166.666/2) - 5, pady=(166.666/2) - 10)
        case 8: ttk.Label(c, text=t).grid(row=3, column=2, padx=(166.666/2) - 5, pady=(166.666/2) - 10)
        case 9: ttk.Label(c, text=t).grid(row=3, column=3, padx=(166.666/2) - 5, pady=(166.666/2) - 10)

def start():
    global tk, c, board
    tk.title("Tic Tac Toe")
    tk.geometry("500x500")

    c = Canvas(tk, width = 500, height = 500)
    c.grid(column = 0, row = 0, sticky = (N, E, W, S))
    tk.columnconfigure(0, weight = 1)
    tk.rowconfigure(0, weight = 1)
    for i in range(len(board)):
        label_maker(i, " ")

def isDone():
    global tk
    tk.destroy()
    
def cont():
    global board, quad, player
    start()
    board = ["", "", "", "", "", "", "", "", ""]
    quad = -1
    player = "X"
    main()
        
def left_click(event):
    global quad, player, board, message
    if event.x > 0 and event.x < 166.666 and event.y > 0 and event.y < 166.666 and board[0] != "X" and board[0] != "Y":
        board[0], quad = player, 1
        label_maker(quad, player)
    elif event.x > 166.666 and event.x < 166.666 * 2 and event.y > 0 and event.y < 166.666 and board[1] != "X" and board[1] != "Y":
        board[1], quad = player, 2
        label_maker(quad, player)
    elif event.x > 166.666 * 2 and event.x < 166.666 * 4 and event.y > 0 and event.y < 166.666 and board[2] != "X" and board[2] != "Y":
        board[2], quad = player, 3
        label_maker(quad, player)

    elif event.x > 0 and event.x < 166.666 and event.y > 166.666 and event.y < 166.666 * 2 and board[3] != "X" and board[3] != "Y":
        board[3], quad = player, 4
        label_maker(quad, player)
    elif event.x > 166.666 and event.x < 166.666 * 2 and event.y > 166.666 and event.y < 166.666 * 2 and board[4] != "X" and board[4] != "Y":
        board[4], quad = player, 5
        label_maker(quad, player)
    elif event.x > 166.666 * 2 and event.x < 166.666 * 4 and event.y > 166.666 and event.y < 166.666 * 2 and board[5] != "X" and board[5] != "Y":
        board[5], quad = player, 6
        label_maker(quad, player)

    elif event.x > 0 and event.x < 166.666 and event.y > 166.666 * 2 and event.y < 166.666 * 4 and board[6] != "X" and board[6] != "Y":
        board[6], quad = player, 7
        label_maker(quad, player)
    elif event.x > 166.666 and event.x < 166.666 * 2 and event.y > 166.666 * 2 and event.y < 166.666 * 4 and board[7] != "X" and board[7] != "Y":
        board[7], quad = player, 8
        label_maker(quad, player)
    elif event.x > 166.666 * 2 and event.x < 166.666 * 4 and event.y > 166.666 * 2 and event.y < 166.666 * 4 and board[8] != "X" and board[8] != "Y":
        board[8], quad = player, 9
        label_maker(quad, player)

    if not game_check(board, player):  
        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        msb = messagebox.askquestion(title="Game", message=message)
        if msb == 'yes':
            cont()
        else:
            isDone()

def game_grid():
    c.create_line(166.666, 0, 166.666, 500, fill="green", width=5)
    c.create_line(333.333, 0, 333.333, 500, fill="green", width=5)
    c.create_line(0, 166.666, 500, 166.666, fill="green", width=5)
    c.create_line(0, 333.333, 500, 333.333, fill="green", width=5)

def game_check(board, player):
    global message
    if board[0] != "" and board[0] == board[1] and board[0] == board[2]:
        message = player + "'s won the game, do you want to continue?"
        return True
    if board[3] != "" and board[3] == board[4] and board[3] == board[5]:
        message = player + "'s won the game, do you want to continue?"
        return True
    if board[6] != "" and board[6] == board[7] and board[6] == board[8]:
        message = player + "'s won the game, do you want to continue?"
        return True
        
    if board[0] != "" and board[0] == board[4] and board[0] == board[8]:
        message = player + "'s won the game, do you want to continue?"
        return True
    if board[2] != "" and board[2] == board[4] and board[2] == board[6]:
        message = player + "'s won the game, do you want to continue?"
        return True
    
    if board[0] != "" and board[0] == board[3] and board[0] == board[6]:
        message = player + "'s won the game, do you want to continue?"
        return True
    if board[1] != "" and board[1] == board[4] and board[1] == board[7]:
        message = player + "'s won the game, do you want to continue?"
        return True
    if board[2] != "" and board[2] == board[5] and board[2] == board[8]:
        message = player + "'s won the game, do you want to continue?"
        return True
    for i in board:
        if i == "":
            return False
    message = "Draw, do you want to continue?"
    return True
    
def main():
    game_grid()

    c.bind("<Button-1>", left_click)
    
    tk.mainloop()
    
if __name__ == "__main__":
    start()
    main()

