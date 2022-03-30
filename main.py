import Words as ws
import random
import tkinter
import tkinter.ttk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
words_list = []
score = 0
rights = 0
data = pd.read_csv("CSVWORD.csv")
englishlist = data["English"].values.tolist()
arabiclist = data["Arabic"].values.tolist()
for org, trs in zip(englishlist, arabiclist):
    words_list.append(ws.Words(org, trs))

random.shuffle(words_list)
original_word = words_list[0].get_original()
translated_word = words_list[0].get_translate()


def inc_rights():
    global rights, score
    rights += 1
    score += 1


def inc_score():
    global score
    score += 1


# window + images
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
window.minsize(width=750, height=700)
var = tkinter.IntVar()
canvas = tkinter.Canvas(width=800, height=800, bg=BACKGROUND_COLOR, highlightthickness=0)
image1 = tkinter.PhotoImage(file="card_back.png")
image2 = tkinter.PhotoImage(file="card_front.png")
image_right = tkinter.PhotoImage(file="right.png")
image_wrong = tkinter.PhotoImage(file="wrong.png")
canvas.create_image(400, 500, image=image1)
canvas.create_text(400, 400, text="English:", font=("arial", 20, "bold"))
canvas.create_text(400, 500, text=original_word, font=("arial", 20, "bold"))
canvas.grid(column=1, row=0)


def flip2():
    canvas.create_image(400, 500, image=image1)
    canvas.create_text(400, 400, text="English:", font=("arial", 25, "bold"))
    canvas.create_text(400, 500, text=original_word, font=("arial", 25, "bold"))
    canvas.create_text(400, 700, text=f"Score is {rights}/{score}", font=("arial", 25, "bold"))
    window.after(3000, flip)


def flip():
    global original_word,translated_word
    canvas.create_image(400, 500, image=image2)
    canvas.create_text(400, 400, text="Arabic:", font=("arial", 25, "bold"))
    canvas.create_text(400, 500, text=translated_word, font=("arial", 25, "bold"))
    canvas.create_text(400, 700, text="Did you know this word ?", font=("arial", 25, "bold"))
    window.wait_variable(var)
    var.set(0)
    random.shuffle(words_list)
    original_word = words_list[0].get_original()
    translated_word = words_list[0].get_translate()
    flip2()


window.after(3000, flip)

button = tkinter.Button(text="", image=image_wrong, highlightthickness=0, relief='groove',
                        command=lambda: [inc_score(), var.set(1)])
button.grid(column=1, row=4)

button2 = tkinter.Button(text="", image=image_right, highlightthickness=0, relief='groove',
                         command=lambda: [inc_rights(), var.set(1)])
button2.grid(column=1, row=2)
window.mainloop()
