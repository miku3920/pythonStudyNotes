import tkinter as tk


def printMe():
    print("miku3920")


def printHello():
    print("Hello")

win = tk.Tk()
win.wm_title("Hello miku3920")
win.minsize(width=320, height=240)
win.resizable(width=False, height=False)

label = tk.Button(win, text="好耶", command=printMe)
label.place(x=140, y=60)

label = tk.Button(win, text="你好", command=printHello)
label.place(x=140, y=100)

win.mainloop()
