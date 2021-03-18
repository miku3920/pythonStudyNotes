import tkinter as tk
from PIL import ImageTk, Image

win = tk.Tk()

c1 = tk.Canvas(win, width=1000, height=200)

# coord = 10, 10, 100, 100
# arc = c1.create_arc(coord, start=0, extent=350, fill="red")

# img = ImageTk.PhotoImage(file="python.png")
# c1.create_image(300,100,image=img)

# c1.create_line(500,100,600,10, fill="red", width=3)

# c1.create_text(700,50, text="miku3920")

c1.create_rectangle(800, 50, 900, 100, fill="blue")

c1.pack()
win.mainloop()
