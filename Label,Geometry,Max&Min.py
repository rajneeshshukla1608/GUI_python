from tkinter import *

me_root = Tk()

# width x height  -> argument
me_root.geometry("500x434")


# this concept is used because some times we want som minimum size and not to go below this theta is why we use it

# width , height   -> argument
me_root.minsize(200, 100)

# width , height
me_root.maxsize(1200, 1000)

me = Label(text="I am a good boy god GUIr")
me.pack()
 
me_root.mainloop()
