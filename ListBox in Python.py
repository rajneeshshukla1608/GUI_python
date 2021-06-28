from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("Listbox")


def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1

i=0
lbx = Listbox(root)
lbx.pack()
lbx.insert(1, "First")

Button(root, text="Add item", command=add).pack()


root.mainloop()
