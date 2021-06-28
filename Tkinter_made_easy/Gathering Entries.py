from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title("Gathering Info")
# using the Entry Constructor

frame = Frame(window)
# entry = Entry(frame, show="*")
entry = Entry(frame, width=20, font=23, textvariable=1)


def dialog():
    box.showinfo("Greeting", "Welcome here " + entry.get())


btn = Button(frame, text="Enter Name", command=dialog)
btn.pack(side=RIGHT, padx=5)
entry.pack(side=LEFT)
frame.pack(padx=20, pady=20)

# options you can use with the Entries
# bd
# bg
# font
# highlightcolor
# selectbackground
# selectforground
# show
# state
# width
# textvariable


window.mainloop()
