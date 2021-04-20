from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import Desktop
from time import sleep

app = Application(backend="uia").start("notepad.exe")
sleep(3)
windows = Desktop(backend="uia").windows()
x= [w for w in windows if '記事本' in w.window_text()][0]
print(x.window_text())
f=app.Notepad
# pywinauto.controls.hwndwrapper.HwndWrapper
f.send_keystrokes('some text{ENTER 2}some more textt{BACKSPACE}')
