import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

path = __file__
path = path[:path.rfind('\\')]


def calcBase(value, fromBase, toBase):
    value % 2


def setBase(fromBase):
    Map = {
        2: binarySV,
        8: octalSV,
        10: decimalSV,
        16: hexSV
    }

    MapPrefix = {
        2: '0b',
        8: '0o',
        10: '',
        16: '0x'
    }

    if fromBase in Map:
        fromSV = Map[fromBase]
        prefix = MapPrefix[fromBase]
    else:
        return False

    str = fromSV.get()
    if str == "":
        str = "0"

    try:
        decimal = int(prefix + str.upper(), fromBase)
        decimalSV.set(decimal)
        binary = bin(decimal)
        binarySV.set(binary[2:])
        octal = oct(decimal)
        octalSV.set(octal[2:])
        hexS = hex(decimal)
        hexSV.set(hexS[2:])
        v.set("計算成功!!")
        label["fg"] = "#00AA00"
    except:
        v.set("格式錯誤!!")
        label["fg"] = "#CC0000"


win = tk.Tk()
win.wm_title("base conversion")
win.minsize(width=320, height=240)
win.resizable(width=False, height=False)

# source: https://twitter.com/hosihosinosora/status/1370853127696523267
img = ImageTk.PhotoImage(Image.open(path+"\\EwY.jpg"))
label = tk.Label(win, image=img)
label.place(x=0, y=0, relwidth=1, relheight=1)

binaryLabel = tk.Label(win, text="二進位:")
binaryLabel.place(x=80, y=20)

binarySV = tk.StringVar()
binarySV.trace("w", lambda name, index, mode, sv=binarySV: setBase(2))
binaryEntry = tk.Entry(win, textvariable=binarySV)
binaryEntry.place(x=140, y=20, width=100)

octalLabel = tk.Label(win, text="八進位:")
octalLabel.place(x=80, y=50)

octalSV = tk.StringVar()
octalSV.trace("w", lambda name, index, mode, sv=octalSV: setBase(8))
octalEntry = tk.Entry(win, textvariable=octalSV)
octalEntry.place(x=140, y=50, width=100)

decimalLabel = tk.Label(win, text="十進位:")
decimalLabel.place(x=80, y=80)

decimalSV = tk.StringVar()
decimalSV.trace("w", lambda name, index, mode, sv=decimalSV: setBase(10))
decimalEntry = tk.Entry(win, textvariable=decimalSV)
decimalEntry.place(x=140, y=80, width=100)

hexLabel = tk.Label(win, text="十六進位:")
hexLabel.place(x=68, y=110)

hexSV = tk.StringVar()
hexSV.trace("w", lambda name, index, mode, sv=hexSV: setBase(16))
hexEntry = tk.Entry(win, textvariable=hexSV)
hexEntry.place(x=140, y=110, width=100)

v = tk.StringVar()
v.set("請任意輸入")
label = tk.Label(win, textvariable=v)
label.place(x=120, y=160)

win.mainloop()
