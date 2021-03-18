import tkinter as tk

win = tk.Tk()
win.wm_title("Hello miku3920")
win.minsize(width=640, height=480)
win.maxsize(width=1440, height=900)
win.resizable(width=True, height=True)

label = tk.Label(win, text="120 160")
label.place(x=120, y=160)

label = tk.Label(win, text="200 300")
label.place(x=200, y=300)

label = tk.Label(win, text="250 350", fg="red", bg="yellow")
label.place(x=250, y=350)

win.mainloop()
print("end")
