from tkinter import *

root = Tk()
canvas_width = 600
canvas_height = 600
frame = Frame(root)
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(frame, width=canvas_width, height=canvas_height)


# x1, y1 to x2, y2
can_widget.create_line(250, 0, 0, 500)
can_widget.create_line(250, 0, 500, 500)
can_widget.create_line(500, 500, 0, 500)

frame.pack()
can_widget.pack()

root.mainloop()