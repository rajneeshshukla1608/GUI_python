from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title("Radio buttons")

frame = Frame()
book = StringVar()

radio_1 = Radiobutton(frame, text="HTMl", variable=book, value="HTML with me")
radio_2 = Radiobutton(frame, text="CSS", variable=book, value="CSS with me")
radio_3 = Radiobutton(frame, text="Js", variable=book, value="Js with me")

radio_1.select()

def dialog():
    box.showinfo("Selection", "Your Choice" + book.get())


btn = Button(frame, text="Click", command=dialog)


btn.pack(side=RIGHT, padx=5)
radio_1.pack(side=LEFT)
radio_2.pack(side=LEFT)
radio_3.pack(side=LEFT)
frame.pack(padx=30, pady=30)


window.mainloop()
