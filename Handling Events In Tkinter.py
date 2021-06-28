from tkinter import *


def me(event):
    print("YOur clicked")


root = Tk()
root.title("Events in TKinter")
root.geometry("644x344")

widget = Button(root, text='Click me please')
widget.pack()

widget.bind('<Button-1>', me)
widget.bind('<Double-1>', quit)

root.mainloop()
