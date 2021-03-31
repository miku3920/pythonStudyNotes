# project 1
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

base = '0123456789ABCDEF'

def toBase10(string, fromBase):
    fromBase = int(fromBase)
    base10 = 0
    exponent = 0
    if fromBase > 16:
        stringList = string.split(':')
        i = len(stringList)-1
    else:
        i = len(string)-1
    while i >= 0:
        if fromBase > 16:
            number = int(stringList[i])
        else:
            number = base.index(string[i].upper())
        if number >= fromBase:
            raise Exception("格式錯誤")
        base10 += number * (fromBase ** exponent)
        exponent += 1
        i -= 1

    return base10


def toBase(base10, toBase):
    base10 = int(base10)
    toBase = int(toBase)
    toBaseString = ''
    while True:
        remainder = base10 % toBase
        if toBase > 16:
            toBaseString = str(remainder) + ':' + toBaseString
        else:
            toBaseString = base[remainder] + toBaseString
        quotient = base10 // toBase
        if quotient == 0:
            break
        base10 = quotient

    return toBaseString.strip(':')


def setBase(fromSV, fromBaseSV):

    string = fromSV.get()
    if string == "":
        string = "0"

    baseSV = fromBaseSV.get()
    if baseSV == "":
        baseSV = "10"

    try:
        decimal = toBase10(string, baseSV)
        if decimal > 9999999999999:
            v.set("數字太大!!")
            label["fg"] = "#CC0000"
            return
        decimalSV.set(decimal)

        binary = toBase(decimal, 2)
        binarySV.set(binary)
        octal = toBase(decimal, 8)
        octalSV.set(octal)
        hexS = toBase(decimal, 16)
        hexSV.set(hexS)
        c1 = toBase(decimal, c1Base.get())
        c1SV.set(c1)
        c2 = toBase(decimal, c2Base.get())
        c2SV.set(c2)

        v.set("計算成功!!")
        label["fg"] = "#00AA00"
    except:
        v.set("格式錯誤!!")
        label["fg"] = "#CC0000"


win = tk.Tk()
win.wm_title("Calc. base by miku3920")
win.minsize(width=320, height=240)
win.resizable(width=False, height=False)

# source: https://twitter.com/hosihosinosora/status/1370853127696523267
img = ImageTk.PhotoImage(Image.open("EwY.jpg"))
label = tk.Label(win, image=img)
label.place(x=0, y=0, relwidth=1, relheight=1)

binaryBase = tk.StringVar()
binaryBase.set(2)
binaryLabel = tk.Label(win, text="二進位:")
binaryLabel.place(x=80, y=20)

binarySV = tk.StringVar()
binarySV.trace("w", lambda name, index, mode,
               sv=binarySV: setBase(binarySV, binaryBase))
binaryEntry = tk.Entry(win, textvariable=binarySV)
binaryEntry.place(x=140, y=20, width=100)

octalBase = tk.StringVar()
octalBase.set(8)
octalLabel = tk.Label(win, text="八進位:")
octalLabel.place(x=80, y=50)

octalSV = tk.StringVar()
octalSV.trace("w", lambda name, index, mode,
              sv=octalSV: setBase(octalSV, octalBase))
octalEntry = tk.Entry(win, textvariable=octalSV)
octalEntry.place(x=140, y=50, width=100)

decimalBase = tk.StringVar()
decimalBase.set(10)
decimalLabel = tk.Label(win, text="十進位:")
decimalLabel.place(x=80, y=80)

decimalSV = tk.StringVar()
decimalSV.trace("w", lambda name, index, mode,
                sv=decimalSV: setBase(decimalSV, decimalBase))
decimalEntry = tk.Entry(win, textvariable=decimalSV)
decimalEntry.place(x=140, y=80, width=100)

hexBase = tk.StringVar()
hexBase.set(16)
hexLabel = tk.Label(win, text="十六進位:")
hexLabel.place(x=68, y=110)

hexSV = tk.StringVar()
hexSV.trace("w", lambda name, index, mode, sv=hexSV: setBase(hexSV, hexBase))
hexEntry = tk.Entry(win, textvariable=hexSV)
hexEntry.place(x=140, y=110, width=100)

c1Base = tk.StringVar()
c1Base.set(256)
combobox1 = ttk.Combobox(win, width=5, textvariable=c1Base)
combobox1['values'] = (2, 8, 10, 16)
combobox1.place(x=68, y=140)

c1SV = tk.StringVar()
c1SV.trace("w", lambda name, index, mode, sv=c1SV: setBase(c1SV, c1Base))
c1Entry = tk.Entry(win, textvariable=c1SV)
c1Entry.place(x=140, y=140, width=100)

c2Base = tk.StringVar()
c2Base.set(65536)
combobox2 = ttk.Combobox(win, width=5, textvariable=c2Base)
combobox2['values'] = (2, 8, 10, 16)
combobox2.place(x=68, y=170)

c2SV = tk.StringVar()
c2SV.trace("w", lambda name, index, mode, sv=c2SV: setBase(c2SV, c2Base))
c2Entry = tk.Entry(win, textvariable=c2SV)
c2Entry.place(x=140, y=170, width=100)

v = tk.StringVar()
v.set("請任意輸入")
label = tk.Label(win, textvariable=v)
label.place(x=120, y=200)

win.mainloop()
