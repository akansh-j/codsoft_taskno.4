import tkinter as tk
import random

# Game choices
choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

def play(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    player_label.config(text=f"Player chose: {player_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(
        text=f"Score → Player: {player_score} | Computer: {computer_score}"
    )

# Create window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x300")
root.resizable(False, False)

# Labels
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
title.pack(pady=10)

player_label = tk.Label(root, text="Player chose: ", font=("Arial", 10))
player_label.pack()

computer_label = tk.Label(root, text="Computer chose: ", font=("Arial", 10))
computer_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score → Player: 0 | Computer: 0")
score_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

# Start app
root.mainloop()
