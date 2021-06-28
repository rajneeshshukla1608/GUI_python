from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title("Check Boxes")

frame = Frame()

var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()

book_1 = Checkbutton(frame, text="HTMl", variable=var_1, onvalue=1, offvalue=0)
book_2 = Checkbutton(frame, text="CSS", variable=var_2, onvalue=1, offvalue=0)
book_3 = Checkbutton(frame, text="JS", variable=var_3, onvalue=1, offvalue=0)


def dialog():
    str = "Your Choose: "
    if var_1.get() == 1 : str += "\nHTMl is easy"
    if var_2.get() == 1 : str += "\nCSS is easy"
    if var_3.get() == 1 : str += "\nJS is easy"
    box.showinfo("Selection", str)


btn = Button(frame, text="Click", command=dialog)

btn.pack(side=RIGHT, padx=5)
book_1.pack(side=LEFT)
book_2.pack(side=LEFT)
book_3.pack(side=LEFT)
frame.pack(padx=20, pady=20)

window.mainloop()
