from tkinter import *

root = Tk()

my_label1 = Label(root, text="Off Beat . . . ")
my_label2 = Label(root, text="The music of the street . . .")
my_label3 = Label(root, text="      . . .")
my_label4 = Label(root, text="Hustle & Bustle . . .")

my_label1.grid(row=0, column=1)
my_label2.grid(row=0, column=0)
my_label3.grid(row=1, column=1)
my_label4.grid(row=2, column=2)

mainloop()
