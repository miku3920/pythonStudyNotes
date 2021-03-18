import tkinter as tk

class Stock:

    def __init__(self, name, id, price, dividend):
        self.name = name
        self.id = id
        self.price = price
        self.dividend = dividend

    def printName(self):
        print(self.name)

    def printId(self):
        print(self.id)

    def printPrice(self):
        print(self.price)

    def printDividend(self):
        print(self.dividend)


HonHai = Stock("鴻海", 2317, 87.36, 4.2)
HonHai.printName()
HonHai.printId()
HonHai.printPrice()
HonHai.printDividend()

win = tk.Tk()
win.wm_title("Hello miku3920")
win.minsize(width=320, height=240)
win.resizable(width=False, height=False)

label = tk.Label(win, text="%d %s" % (HonHai.id,HonHai.name))
label.place(x=120, y=60)

label = tk.Label(win, text="股價: %.2f" % HonHai.price)
label.place(x=120, y=80)

label = tk.Label(win, text="股利: %.2f" % HonHai.dividend)
label.place(x=120, y=100)

win.mainloop()
print("end")
