from tkinter import *

root = Tk()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(root, text="Music", variable=CheckVar1, onvalue=1, offvalue=0, width=20, anchor=E)
C2 = Checkbutton(root, text="Video", variable=CheckVar2, onvalue=1, offvalue=0, width=20, anchor=SW)


C1.pack()
C2.pack()

mainloop()
