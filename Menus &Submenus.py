from tkinter import *

root = Tk()
root.geometry("344x555")
root.title("Pycharm")


def com():
    print("you clicked")

# use these to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="Menu", command=com)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)


mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New", command=com)
m1.add_command(label="Save", command=com)
m1.add_separator()
m1.add_command(label="Print", command=com)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)


m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=com)
m2.add_command(label="Copy", command=com)
m2.add_separator()
m2.add_command(label="Paste", command=com)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)


m3 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Exit", command=exit)



root.mainloop()
