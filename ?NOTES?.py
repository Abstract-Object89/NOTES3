from tkinter import *

from PIL import ImageTk, Image


# def correct_answer (a, b, c, d, e, f, g, )
# background not changing to red
# from note_names.py import notes
# notes()
# print(notes[0])

root = Tk()
win = Tk()

root.title("Guess the notes on the Treble clef ! - - - OFFBEAT.com")

root.iconbitmap('E3.png')

# defining images
E3 = ImageTk.PhotoImage(Image.open('E3.png'))
F3 = ImageTk.PhotoImage(Image.open('F3.png'))
G3 = ImageTk.PhotoImage(Image.open('G3.png'))
A3 = ImageTk.PhotoImage(Image.open('A3.png'))
B3 = ImageTk.PhotoImage(Image.open('B3.png'))
C4 = ImageTk.PhotoImage(Image.open('C4.png'))
note_list = [E3, F3, G3, A3, B3, C4]

E3_label = Label(image=E3)
F3_label = Label(image=F3)

E3_label.grid(row=1, column=1)


#                                                  Answer entry box

entry = Entry(root, width=30, background="red", foreground="yellow", borderwidth=3)
entry.grid(row=2, column=1)
entry.get()


#                                              defining page navigation
def next():
    global E3
    global next_button
    global previous_button

    E3_label.grid_forget()


def previous():
    return


#                                             RETURNS RESPONSE To Answer
def click2play():
    #                                         Creates answer Label
    answer = Label(root, text=entry.get() + "     WELL DONE, THAT'S RIGHT !")
    #                                         Positions answer
    answer.grid(row=2, column=1)


click2play()

# if entry == "E3":
# click2play:
#                                                   Button creation
checkanswr_button = Button(root, text="Click to check answer !", padx=10, pady=10, anchor=S,
                     fg="black", background="red", borderwidth=5, command=click2play)
next_button = Button(root, text=">>", fg="yellow", background="red", command=next)
previous_button = Button(root, text="<<", fg="yellow", background="red", command=lambda: previous())

#                                                   Button positioning
previous_button.grid(row=3, column=0)
checkanswr_button.grid(row=3, column=1)
next_button.grid(row=3, column=3)



#                                                  Runs program
root.mainloop()
