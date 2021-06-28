from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title("Label Example")


# def dialog():
#     var = box.askyesno("Message Box", "Proceed?")
#     if var == 1:
#         box.showinfo("yes Box", "proceeding")
#     else:
#         box.showwarning("No box", "Cancelling")


def dialog():
    box.showerror("error", "you stucked")


# def dialog():
#     var = box.askquestion("question", "are you a donkey")
#     if var == 1:
#         box.showerror("fhvd", "you can be good guy")
#     else:
#         box.showinfo("nonoooo", "really")


btn = Button(window, text="Click", command=dialog)
btn.pack(padx=150, pady=50)

# methods used in the box

# showinfo()
# showwarning()
# showerror()
# askquestion()
# askokcancel()
# askyesno()
# askretrycancel()

window.mainloop()
