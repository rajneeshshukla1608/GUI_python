from tkinter import *


def getvalue():
    print(f" The username is {uservalue.get()}")
    print(f" THE password is {passvalue.get()}")


root = Tk()
root.geometry("655x333")

username = Label(root, text="Username")

password = Label(root, text="Password")

username.grid()
password.grid(row=1)

# variable class in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvalue).grid()

root.mainloop()
