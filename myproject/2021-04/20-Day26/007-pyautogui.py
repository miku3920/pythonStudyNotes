import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print(pyautogui.size())
width, height = pyautogui.size()
print(width)
print(height)

pyautogui.moveTo(100, 100, duration=0.05)
pyautogui.moveTo(200, 100, duration=0.05)
pyautogui.moveTo(200, 200, duration=0.05)
pyautogui.moveTo(100, 200, duration=0.05)

pyautogui.moveRel(100, 0, duration=0.05)
pyautogui.moveRel(0, 100, duration=0.05)
pyautogui.moveRel(-100, 0, duration=0.05)
pyautogui.moveRel(0, -100, duration=0.05)


print(pyautogui.position())
pyautogui.click(10, 5)
pyautogui.scroll(200)

pyautogui.click(960, 512)
pyautogui.typewrite('Hello world!')

pyautogui.keyDown('ctrl')
pyautogui.keyDown('a')
pyautogui.keyUp('a')
pyautogui.keyUp('ctrl')