import tkinter as tk

win = tk.Tk()
win.wm_title("Hello miku3920")
win.minsize(width=320, height=240)
win.resizable(width=False, height=False)

twd = 100
usd = twd*0.0357057

label = tk.Label(win, text="台幣: %12.2f" % twd)
label.place(x=120, y=80)

label = tk.Label(win, text="美金: %12.2f" % usd)
label.place(x=120, y=100)

win.mainloop()
print("end")
