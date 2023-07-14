import tkinter as tk
from tkinter import messagebox

# Costanti
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = ""

# Variabili di gioco
current_player = PLAYER_X
game_board = [[EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]


def on_button_click(row, col):
    global current_player

    if game_board[row][col] == EMPTY:
        game_board[row][col] = current_player
        button = buttons[row][col]
        button.config(text=current_player)

        if check_winner(current_player):
            messagebox.showinfo("Vittoria", f"Giocatore {current_player} ha vinto!")
            reset_game()
        elif is_board_full():
            messagebox.showinfo("Pareggio", "Nessun vincitore. Pareggio!")
            reset_game()
        else:
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X


def check_winner(player):
    # Controllo righe
    for row in range(3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] == player:
            return True

    # Controllo colonne
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] == player:
            return True

    # Controllo diagonali
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == player:
        return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0] == player:
        return True

    return False


def is_board_full():
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == EMPTY:
                return False
    return True


def reset_game():
    global current_player, game_board
    current_player = PLAYER_X
    game_board = [[EMPTY, EMPTY, EMPTY],
                  [EMPTY, EMPTY, EMPTY],
                  [EMPTY, EMPTY, EMPTY]]

    for row in range(3):
        for col in range(3):
            button = buttons[row][col]
            button.config(text=EMPTY)


# Creazione della finestra di gioco
window = tk.Tk()
window.title("Tic Tac Toe")

# Creazione dei bottoni
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text=EMPTY, font=("Arial", 20), width=6, height=3,
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

# Avvio dell'interfaccia grafica
window.mainloop()
