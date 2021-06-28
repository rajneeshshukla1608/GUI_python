from tkinter import *

me_root = Tk()

me_root.geometry("955x944")
photo = PhotoImage(file="joey.png")

joey_label = Label(image=photo)
joey_label.pack()


me_root.mainloop()
