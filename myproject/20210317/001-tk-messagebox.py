import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.wm_title("miku3920")
win.minsize(width=320, height=240)
win.resizable(width=False, height=False)

messagebox.showinfo("showinfo", "Information")
messagebox.showwarning("showwarning", "Warning")
messagebox.showerror("showerror", "Error")
x0 = messagebox.askquestion("askquestion", "Are you sure?")
print(x0)
x1 = messagebox.askokcancel("askokcancel", "Want to continue?")
print(x1)
x2 = messagebox.askyesno("askyesno", "Find the value?")
print(x2)
x3 = messagebox.askretrycancel("askretrycancel", "Try again?")
print(x3)

win.mainloop()
