from tkinter import *
import pandas as pd
import random

new_data = {}
word = {}

try:
    data = pd.read_csv("french_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv("french_words.csv")
    new_data = original_data.to_dict(orient="records")

else:
    new_data = data.to_dict(orient="records")


def new_words():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(new_data)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=word["French"], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=word["English"], fill='white')
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    new_data.remove(word)
    df = pd.DataFrame(new_data)
    df.to_csv("words_to_learn.csv", index=False)

    new_words()


window = Tk()

window.config(padx=50, pady=50, bg="#B1DDC6")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(window, width=800, height=526, bg="#B1DDC6", highlightthickness=0)

card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = PhotoImage(file="wrong.png")
wrong = Button(image=wrong_button, highlightthickness=0, command=new_words)
wrong.grid(row=2, column=0)

right_button = PhotoImage(file="right.png")
right = Button(image=right_button, highlightthickness=0, command=is_known)
right.grid(row=2, column=1)

new_words()

window.mainloop()
