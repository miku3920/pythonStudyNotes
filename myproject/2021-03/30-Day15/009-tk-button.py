import tkinter as tk

def addTax():
    str = entry.get()
    if str == "":
        str = "0"
    price = float(str)
    tax = 0.05
    calc = price+price*tax
    v.set("%.2f" % calc)

win = tk.Tk()
win.wm_title("Hello miku3920")
win.minsize(width=320, height=240)
win.resizable(width=False, height=False)

label = tk.Label(win, text="消費:")
label.place(x=80, y=50)

sv = tk.StringVar()
entry = tk.Entry(win, textvariable=sv)
entry.place(x=120, y=50)

label = tk.Label(win, text="稅後:")
label.place(x=80, y=100)

v = tk.StringVar()
v.set("0")
label = tk.Label(win, textvariable=v)
label.place(x=120, y=100)

label = tk.Button(win, text="計算", command=addTax)
label.place(x=150, y=150)

win.mainloop()
