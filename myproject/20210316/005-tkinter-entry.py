import tkinter as tk


def setString():
    twd = int(entry.get())
    usd = twd*0.0354204
    v.set("%.4f" % usd)


win = tk.Tk()
win.wm_title("Hello miku3920")
win.minsize(width=320, height=240)
win.resizable(width=False, height=False)

label = tk.Label(win, text="台幣:")
label.place(x=80, y=50)

entry = tk.Entry(win)
entry.place(x=120, y=50)

label = tk.Label(win, text="美金:")
label.place(x=80, y=100)

v = tk.StringVar()
v.set("0")
label = tk.Label(win, textvariable=v)
label.place(x=120, y=100)

label = tk.Button(win, text="計算", command=setString)
label.place(x=140, y=150)

win.mainloop()
