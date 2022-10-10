#  MUSICAL GUESS GAME
#
#  
#
#
#  ################

from tkinter import *


from PIL import ImageTk, Image

# from note_names.py import notes
# notes()
# print(notes[0])

root = Tk()
win = Tk()

root.title("Guess the notes on the Treble clef ! - - - OFFBEAT.com")

root.iconbitmap('Desktop/NOTES/iconico/E3.ico')

# E3 = ImageTk.PhotoImage(Image.open("image"))

# def correct_answer (a, b, c, d, e, f, g, )

# background not changing to red


e = Entry(root, width=30, background="red", foreground="yellow", borderwidth=3)

e.pack()
e.get()
e.insert(0, "Answer here: ")


def click2play():
    answer1 = Label(root, text=e.get() + ". . . is not the right answer 🤭 Try again !")
    answer1.pack()


play_button = Button(root, text="Click to check answer !", padx=10, pady=10, anchor=S,
                     fg="black", background="red", borderwidth=5, command=click2play)

play_button.pack()

root.mainloop()
