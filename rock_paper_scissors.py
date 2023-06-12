from tkinter import Tk, Label, Button
from random import choice

available_choices = ["paper", "kamien", "nozyce"]

def play(player, cpu):
    win_with = {"papier": "kamien", "kamien": "nozyce", "nozyce": "papier"}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False

def play_cmd(player):
    global text_label
    cpu = choice(available_choices)
    is_user_winner = play(player, cpu)
    if is_user_winner is None:
        text_label.config(text="Remis", fg="blue")
    elif is_user_winner:
        text_label.config(text="Wygrales!", fg="green")
    else:
        text_label.config(text="Przegrales!", fg="red")


root = Tk()
root.title("Papier, kamien, nozyce")
root.geometry("300x150")

text_label = Label(root, font=40, text="Zagrajmy w gre ( ͡° ͜ʖ ͡°)")
text_label.pack()

Button(
    root, text="📄 Papier", font=40, width=10, command=lambda: play_cmd("papier")
).pack()

Button(
    root, text="🪨 Kamien", font=40, width=10, command=lambda: play_cmd("kamien")
).pack()

Button(
    root, text="✂️ Nozyce", font=40, width=10, command=lambda: play_cmd("nozyce")
).pack()

root.mainloop()
