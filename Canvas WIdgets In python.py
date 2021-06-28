from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)

can_widget.pack()

# the line goes from the point x1, y1 to  x2, y2
# can_widget.create_line(0, 100, 800, 100, fill="red")
# can_widget.create_line(0, 200, 800, 200, fill="red")
# can_widget.create_line(0, 300, 800, 300, fill="red")

can_widget.create_line(200, 100, 200, 400, fill="red")
can_widget.create_line(300, 200, 300, 400, fill="red")
can_widget.create_line(400, 300, 400, 400, fill="red")


# To create a rectangle specify parameters in this order - coordinates of top left and bottom right
#can_widget.create_rectangle(3, 5, 700, 300, fill="blue")

#can_widget.create_text(200, 200, text="Python")


#can_widget.create_oval(344, 233, 244, 355)



root.mainloop()
