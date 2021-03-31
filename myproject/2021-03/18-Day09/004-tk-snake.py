# project 2
import tkinter as tk
import random
import math
import time


class Model():

    def __init__(self):
        self.maxlen = 4
        self.start = False
        self.shift = False
        self.snakeX = []
        self.snakeY = []

    def initGame(self):
        self.timeDelay = 300
        self.maxlen = 4
        self.snakeX = []
        self.snakeY = []
        self.headX = random.randint(1, 59)
        self.headY = random.randint(1, 59)
        if self.headX > 30:
            self.xDirection = -1
        else:
            self.xDirection = 1
        self.yDirection = 0
        self.snakeX.append(self.headX)
        self.snakeY.append(self.headY)
        self.start = True

    def endGame(self):
        self.start = False

    def setLeft(self):
        self.xDirection = -1
        self.yDirection = 0

    def setRight(self):
        self.xDirection = 1
        self.yDirection = 0

    def setUp(self):
        self.xDirection = 0
        self.yDirection = -1

    def setDown(self):
        self.xDirection = 0
        self.yDirection = 1

    def getTimeDelay(self):
        return math.floor(self.timeDelay)

    def addHead(self):
        self.headX += self.xDirection
        self.headY += self.yDirection
        self.snakeX.append(self.headX)
        self.snakeY.append(self.headY)

    def delTail(self):
        self.tailX = self.snakeX.pop(0)
        self.tailY = self.snakeY.pop(0)

    def updateMaxlen(self):
        self.maxlen += 1

    def updateTimeDelay(self):
        self.timeDelay *= 0.95

    def updateScorePoint(self, x, y):
        self.scoreX = x
        self.scoreY = y


class View():
    def __init__(self, win, model):
        self.model = model
        self.c1 = tk.Canvas(win, width=600, height=700)
        self.remakeBackground()
        self.drawStart()
        self.drawScore()
        self.c1.pack()

    def initGame(self):
        self.remakeBackground()
        self.drawScore()
        self.drawPoint(self.model.scoreX, self.model.scoreY)
        self.c1.pack()

    def endGame(self):
        self.c1.delete("all")
        self.remakeBackground()
        self.drawStart()
        self.drawScore()
        self.c1.pack()

    def drawHead(self):
        x = self.model.headX
        y = self.model.headY
        self.drawPoint(x, y)
        self.c1.pack()

    def drawTail(self):
        x = self.model.tailX
        y = self.model.tailY
        self.delPoint(x, y)
        self.c1.pack()

    def drawScorePoint(self):
        x = self.model.scoreX
        y = self.model.scoreY
        self.drawPoint(x, y)
        self.drawScore()
        self.c1.pack()

    def remakeBackground(self):
        self.c1.create_rectangle(0, 0, 600, 700, fill="#ffffff", outline="")
        self.c1.create_rectangle(4, 4, 595, 595, fill="#dddddd")

    def drawStart(self):
        self.c1.create_text(300, 300, text="按任意鍵開始", font=('Helvetica', 24))

    def drawScore(self):
        self.c1.create_rectangle(0, 600, 600, 700, fill="#ffffff", outline="")
        self.c1.create_text(300, 650, text="score: " +
                            str(self.model.maxlen-4), font=('Helvetica', 20))

    def drawPoint(self, x, y):
        self.c1.create_rectangle(
            x*10-4, y*10-4, x*10+4, y*10+4, fill="#444444", outline="")

    def delPoint(self, x, y):
        self.c1.create_rectangle(
            x*10-4, y*10-4, x*10+4, y*10+4, fill="#dddddd", outline="")


class Controller():

    def __init__(self, win, model, view):
        self.win = win
        self.model = model
        self.view = view

    def leftKey(self):
        if self.isStart() and not self.isLeftRight():
            self.model.setLeft()

    def rightKey(self):
        if self.isStart() and not self.isLeftRight():
            self.model.setRight()

    def upKey(self):
        if self.isStart() and not self.isUpDown():
            self.model.setUp()

    def downKey(self):
        if self.isStart() and not self.isUpDown():
            self.model.setDown()

    def startGame(self):
        if self.isNotStart():
            self.model.initGame()
            while True:
                x = random.randint(1, 59)
                y = random.randint(1, 59)
                self.model.updateScorePoint(x, y)
                if self.isScorePointNotOnSnake():
                    break
            self.view.initGame()
            self.updateSnake()

    def endGame(self):
        self.model.endGame()
        self.view.endGame()

    def updateSnake(self):
        if self.isStart():
            self.updateTail()
            self.updateHead()

            if self.isDie():
                self.endGame()
            if self.shouldAddScore():
                self.updateScorePoint()

            self.win.after(self.model.getTimeDelay(), self.updateSnake)

    def updateHead(self):
        self.model.addHead()
        self.view.drawHead()

    def updateTail(self):
        if len(self.model.snakeX) >= self.model.maxlen:
            self.model.delTail()
            self.view.drawTail()

    def updateScorePoint(self):
        self.model.updateMaxlen()
        self.model.updateTimeDelay()
        while True:
            x = random.randint(1, 59)
            y = random.randint(1, 59)
            self.model.updateScorePoint(x, y)
            if self.isScorePointNotOnSnake():
                break

        self.view.drawScorePoint()

    def isStart(self):
        return self.model.start

    def isNotStart(self):
        return not self.model.start

    def isLeftRight(self):
        x = self.model.snakeX[-1]-self.model.snakeX[-2]
        return x == -1 or x == 1

    def isUpDown(self):
        y = self.model.snakeY[-1]-self.model.snakeY[-2]
        return y == -1 or y == 1

    def isScorePointNotOnSnake(self):
        for i in range(len(self.model.snakeX)):
            if self.model.scoreX == self.model.snakeX[i] and self.model.scoreY == self.model.snakeY[i]:
                return False
        return True

    def isDie(self):
        if self.model.headX < 1:
            return True
        if self.model.headX > 59:
            return True
        if self.model.headY < 1:
            return True
        if self.model.headY > 59:
            return True
        for i in range(len(self.model.snakeX)-1):
            if self.model.headX == self.model.snakeX[i] and self.model.headY == self.model.snakeY[i]:
                return True
        return False

    def shouldAddScore(self):
        return self.model.headX == self.model.scoreX and self.model.headY == self.model.scoreY


class Snake():

    def __init__(self):
        win = tk.Tk()
        win.wm_title("Greedy snake by miku3920")
        win.minsize(width=600, height=700)
        win.resizable(width=False, height=False)

        model = Model()
        view = View(win, model)
        controller = Controller(win, model, view)

        win.bind("<Key>", lambda evt: controller.startGame())
        win.bind('<Left>', lambda evt: controller.leftKey())
        win.bind('<Right>', lambda evt: controller.rightKey())
        win.bind('<Up>', lambda evt: controller.upKey())
        win.bind('<Down>', lambda evt: controller.downKey())

        win.mainloop()


Snake()
