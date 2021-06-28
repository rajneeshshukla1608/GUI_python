from tkinter import *

window = Tk()

window.title("Responding button")
btn_end = Button(window, text="Close", command=exit, bd=5, activebackground="blue")


def tog():
    if window.cget('bg') == 'yellow':
        window.configure(bg="grey")
    else:
        window.configure(bg="yellow")


btn_tog = Button(window, text="Switch", command=tog, bd=5, activeforeground="green", state="active")

btn_end.pack(padx=150, pady=20)
btn_tog.pack(padx=150, pady=20)

# options available for the option=value pairs

# activebackground
# activeforeground
# bd
# bg
# command
# fg
# font
# height
# highlightcolor
# image
# justify
# padx
# pady
# relief
# state = active, normal, disabled
# underline
# width
# wraplength




window.mainloop()
