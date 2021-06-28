from tkinter import *

root = Tk()
root.geometry("444x233")
root.title("My First GUI")

# important label options
# text = adds the text
# bd = background
# fg = foreground
# font = sets the font  -> below font methods
# 1.font=("comicsansns", 19, "bold")
# 2.font= "comicsansns 19 bold"
# padx = x padding
# pady = y padding
# relief = border styling  = SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text='''Van Rossum was born and 
raised in the Netherlands, where \n he received a master's
degree in mathematics and computer\n science from the
University of Amsterdam in 1982.''', fg="violet", bg="blue",
                    padx="90", pady="50", font="comicsansns 19 bold", borderwidth=3,
                    relief=SUNKEN)

# Important pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor="sw", fill=X)
# title_label.pack(side=LEFT, fill=Y, padx=45, pady=45)
title_label.pack(side=LEFT, fill=Y)

root.mainloop()
