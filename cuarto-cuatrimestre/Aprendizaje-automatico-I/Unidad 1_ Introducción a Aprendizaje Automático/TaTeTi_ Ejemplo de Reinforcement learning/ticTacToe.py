import tkinter as tk
import numpy as np
import pickle

# Definición del tamaño del tablero
BOARD_ROWS = 3
BOARD_COLS = 3

class TicTacToeGUI:
    def __init__(self, master, ai_player, human_player):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.ai_player = ai_player
        self.human_player = human_player
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS))
        self.current_symbol = 1  # Player 1 (IA) empieza
        self.buttons = {}
        self.create_board()
        self.status_label = tk.Label(self.master, text="Turno de la IA", font=("Arial", 14))
        self.status_label.grid(row=3, column=0, columnspan=3)

        # La IA hace su primer movimiento
        self.ai_move()

    def create_board(self):
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                button = tk.Button(self.master, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda row=i, col=j: self.human_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[(i, j)] = button

    def human_move(self, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = -1  # Player 2 (Humano)
            self.buttons[(row, col)].config(text="O", state="disabled")

            if self.check_winner() is not None:
                self.end_game()
            else:
                self.current_symbol = 1
                self.status_label.config(text="Turno de la IA")
                self.master.after(500, self.ai_move)  # La IA juega después de 0.5 segundos

    def ai_move(self):
        positions = self.available_positions()
        if positions:
            ai_action = self.ai_player.choose_action(positions, self.board, self.current_symbol)
            self.board[ai_action] = 1  # Player 1 (IA)
            self.buttons[ai_action].config(text="X", state="disabled")

            if self.check_winner() is not None:
                self.end_game()
            else:
                self.current_symbol = -1
                self.status_label.config(text="Tu turno")

    def available_positions(self):
        positions = []
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if self.board[i, j] == 0:
                    positions.append((i, j))
        return positions

    def check_winner(self):
        for i in range(BOARD_ROWS):
            if sum(self.board[i, :]) == 3:
                return 1
            if sum(self.board[i, :]) == -3:
                return -1

        for i in range(BOARD_COLS):
            if sum(self.board[:, i]) == 3:
                return 1
            if sum(self.board[:, i]) == -3:
                return -1

        diag_sum1 = sum([self.board[i, i] for i in range(BOARD_COLS)])
        diag_sum2 = sum([self.board[i, BOARD_COLS - i - 1] for i in range(BOARD_COLS)])
        diag_sum = max(diag_sum1, diag_sum2)
        if diag_sum == 3:
            return 1
        if diag_sum == -3:
            return -1

        if len(self.available_positions()) == 0:
            return 0

        return None

    def end_game(self):
        winner = self.check_winner()
        if winner == 1:
            self.status_label.config(text="¡La IA gana!")
        elif winner == -1:
            self.status_label.config(text="¡Ganaste!")
        else:
            self.status_label.config(text="¡Empate!")

        for button in self.buttons.values():
            button.config(state="disabled")

class Player:
    def __init__(self, name, exp_rate=0.3):
        self.name = name
        self.exp_rate = exp_rate
        self.states_value = {}

    def get_hash(self, board):
        board_hash = str(board.reshape(BOARD_COLS * BOARD_ROWS))
        return board_hash

    def choose_action(self, positions, current_board, symbol):
        if np.random.uniform(0, 1) <= self.exp_rate:
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            value_max = -999
            for position in positions:
                next_board = current_board.copy()
                next_board[position] = symbol
                next_board_hash = self.get_hash(next_board)
                value = 0 if self.states_value.get(next_board_hash) is None else self.states_value.get(next_board_hash)
                if value >= value_max:
                    value_max = value
                    action = position
        return action

    def load_policy(self, file):
        with open(file, 'rb') as f:
            self.states_value = pickle.load(f)

class HumanPlayer:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    root = tk.Tk()
    
    # cargar la política entrenada de la IA
    ai_player = Player("computer", exp_rate=0)
    ai_player.load_policy("policy_p1")

    human_player = HumanPlayer("human")

    game = TicTacToeGUI(root, ai_player, human_player)
    root.mainloop()
