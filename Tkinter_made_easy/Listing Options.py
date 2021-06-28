from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title("Listing Options")

frame = Frame()
listbox = Listbox(frame, height=10, width=20, selectmode=SINGLE)

listbox.insert(1, "HTML")
listbox.insert(2, "CSS")
listbox.insert(3, "javascript")


def dialog():
    box.showinfo("Courses", "You chose " + listbox.get(listbox.curselection()))


btn = Button(frame, text="Choose", command=dialog)

btn.pack(side=RIGHT, padx=5)
listbox.pack(side=LEFT)
frame.pack(pady=30, padx=30)

# option in listbox widget with their options=value

# bd
# bg
# fg
# font
# height
# selectbackground
# selectmode
# width
# yscrollcommand


window.mainloop()
