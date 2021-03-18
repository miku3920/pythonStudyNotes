import tkinter as tk
import time

now = ''

def update_clock():
    now = time.strftime("%H:%M:%S")
    label.configure(text=now)
    root.after(1000, update_clock)

root = tk.Tk()
label = tk.Label(text="", font=('Helvetica', 48), fg='red')
label.pack()
update_clock()
root.mainloop()
