from tkinter import *

window = Tk()
window.title("Label Example")
label = Label(window, text="hello world!")
label.pack(padx=200, pady=200)

window.mainloop()