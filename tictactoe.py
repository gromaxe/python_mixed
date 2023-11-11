import tkinter as tk
from tkinter import messagebox


def generate_button_click(btn_number, buttons, game_state, counter, check_game_status, update_ui):
    def button_click():
        if game_state[btn_number] != -1:
            return
        game_state[btn_number] = counter[0] % 2
        update_ui(buttons, game_state)
        winner = check_game_status(game_state)
        if winner is not None:
            messagebox.showinfo("Game Over", f"Player {'X' if winner == 1 else 'O'} wins!")
            reset_game(buttons, game_state, counter)
        elif -1 not in game_state:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game(buttons, game_state, counter)
        counter[0] += 1

    return button_click


def create_buttons(root, game_state, counter, check_game_status, update_ui):
    buttons = []
    for i in range(9):
        btn = tk.Button(root, font=('normal', 40, 'bold'), command=generate_button_click(i, buttons, game_state, counter, check_game_status, update_ui))
        btn.place(relx=(i % 3) / 3, rely=(i // 3) / 3, relwidth=1 / 3, relheight=1 / 3)
        buttons.append(btn)
    return buttons


def check_game_status(game_state):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in winning_combinations:
        if game_state[a] == game_state[b] == game_state[c] != -1:
            return game_state[a]
    return None


def update_ui(buttons, game_state):
    for btn, state in zip(buttons, game_state):
        btn.config(text='X' if state == 1 else 'O' if state == 0 else '')


def reset_game(buttons, game_state, counter):
    for i in range(9):
        game_state[i] = -1
        buttons[i].config(text='')
    counter[0] = 0


def main():
    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Set minimum window size
    min_width, min_height = 300, 300
    root.minsize(min_width, min_height)

    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (min_width // 2)
    y = (root.winfo_screenheight() // 2) - (min_height // 2)
    root.geometry(f'+{x}+{y}')

    game_state = [-1] * 9  # -1 for empty, 0 for O, 1 for X
    counter = [0]  # Move counter

    buttons = create_buttons(root, game_state, counter, check_game_status, update_ui)

    root.mainloop()


if __name__ == "__main__":
    main()
