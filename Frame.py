from tkinter import *

root = Tk()

root.geometry("655x333")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l = Label(f1, text="Project Tkinter - Pycharm")
l.pack(pady=142)

l = Label(f2, text="Welcome to this world", font="Helvetica 16 bold", fg="red")
l.pack()


root.mainloop()
