import tkinter as tk
from PIL import ImageTk, Image


def printMe():
    print("miku3920")

path = __file__
path = path[:path.rfind('\\')]

win = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path+"\\donatetw.png"))
label=tk.Label(win, image=img)
label = tk.Button(win, image=img, command=printMe)
label.pack()
win.mainloop()
