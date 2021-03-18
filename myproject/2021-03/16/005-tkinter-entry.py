import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

path = __file__
path = path[:path.rfind('\\')]


def setString():
    str = entry.get()
    if str == "":
        str = "0"
    twd = float(str)
    magnification = 1.0

    dollar = combobox.get()

    magnification = {
        '美金': 0.035112,
        '日幣': 3.818251,
        '歐元': 0.02924
    }

    if dollar in magnification:
        calc = twd * magnification[dollar]
    else:
        calc = twd

    v.set("%.4f" % calc)


win = tk.Tk()
win.wm_title("Hello miku3920")
win.minsize(width=320, height=240)
win.resizable(width=False, height=False)

# source: https://twitter.com/hosihosinosora/status/1370853127696523267
img = ImageTk.PhotoImage(Image.open(path+"\\EwY.jpg"))
label = tk.Label(win, image=img)
label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(win, text="台幣:")
label.place(x=80, y=50)

sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: setString())
entry = tk.Entry(win, textvariable=sv)
entry.place(x=120, y=50)

n = tk.StringVar()
combobox = ttk.Combobox(win, width=5, textvariable=n)
combobox['values'] = ('美金', '日幣', '歐元')
combobox.set('美金')
combobox.place(x=80, y=100)

v = tk.StringVar()
v.set("0")
label = tk.Label(win, textvariable=v)
label.place(x=150, y=100)

win.mainloop()
