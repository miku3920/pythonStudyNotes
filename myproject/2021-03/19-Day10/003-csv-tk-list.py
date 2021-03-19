import csv
import tkinter as tk

path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+"\\"

win = tk.Tk()
lb = tk.Listbox(win)

with open(path+'消費紀錄.csv', 'r', newline='', encoding='utf-8') as fp:
    read = csv.reader(fp, delimiter=',')
    header = next(read)
    print(header)
    i = 0
    for row in read:
        lb.insert(i, row)
        i += 1

fp.close()

lb.pack()
win.mainloop()
