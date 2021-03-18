import tkinter as tk
from PIL import ImageTk, Image

path = __file__
path = path[:path.rfind('\\')]+"\\"

win = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path+"donate.png"))
label = tk.Label(win, image=img)
label.pack()
win.mainloop()
