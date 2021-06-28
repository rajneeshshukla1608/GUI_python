from tkinter import *

# I accept the challenge
# made a ready bar in the bottom i the window

root = Tk()
root.geometry("700x300")
root.title("It's Exercise")

label = Label(text="Ready", bg="grey")
label.pack(side="bottom", anchor="sw", fill=X)

root.mainloop()
