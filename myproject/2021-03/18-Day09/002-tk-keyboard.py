from tkinter import Tk, Label

def key_pressed(event):
    w = Label(root, text="Key Pressed:"+event.char)
    w.place(x=70, y=90)

def leftKey(event):
    print("Left key pressed")

def rightKey(event):
    print("Right key pressed")

def upKey(event):
    print("Up key pressed")

def downKey(event):
    print("Down key pressed")

root = Tk()
root.bind("<Key>", key_pressed)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)
root.mainloop()
