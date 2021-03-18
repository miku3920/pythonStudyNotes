import tkinter as tk
import random
import math
import time

# god class example
class Snake():

    def __init__(self):
        self.win = tk.Tk()
        self.win.wm_title("Greedy snake by miku3920")
        self.win.minsize(width=600, height=700)
        self.win.resizable(width=False, height=False)
        self.c1 = tk.Canvas(self.win, width=600, height=700)
        self.c1.create_rectangle(0, 0, 600, 700, fill="#ffffff", outline="")
        self.c1.create_rectangle(4, 4, 595, 595, fill="#dddddd")
        self.c1.create_text(300, 300, text="按任意鍵開始", font=('Helvetica', 24))
        self.c1.create_text(300, 650, text="score: 0", font=('Helvetica', 20))
        self.c1.pack()
        self.start = False
        self.shift = False
        self.win.bind("<Key>", lambda evt: self.Game())
        self.win.bind('<Left>', lambda evt: self.leftKey())
        self.win.bind('<Right>', lambda evt: self.rightKey())
        self.win.bind('<Up>', lambda evt: self.upKey())
        self.win.bind('<Down>', lambda evt: self.downKey())
        self.win.mainloop()

    def Game(self):
        if self.isNotStart():
            self.timeDelay = 300
            self.maxlen = 5
            self.scoreX = random.randint(1, 59)
            self.scoreY = random.randint(1, 59)
            self.x = random.randint(1, 59)
            self.y = random.randint(1, 59)
            if self.x > 30:
                self.xDirection = -1
            else:
                self.xDirection = 1
            self.yDirection = 0
            self.snakeX = []
            self.snakeY = []
            self.snakeX.append(self.x)
            self.snakeY.append(self.y)
            self.c1.create_rectangle(4, 4, 595, 595, fill="#dddddd")
            self.c1.create_rectangle(0, 600, 600, 700, fill="#ffffff", outline="")
            self.c1.create_text(300, 650, text="score: 0", font=('Helvetica', 20))
            self.c1.pack()
            self.start = True
            self.drawPoint(self.scoreX, self.scoreY)
            self.updateSnake()

    def leftKey(self):
        if self.isStart() and not self.isLeftRight():
            self.xDirection = -1
            self.yDirection = 0

    def rightKey(self):
        if self.isStart() and not self.isLeftRight():
            self.xDirection = 1
            self.yDirection = 0

    def upKey(self):
        if self.isStart() and not self.isUpDown():
            self.xDirection = 0
            self.yDirection = -1

    def downKey(self):
        if self.isStart() and not self.isUpDown():
            self.xDirection = 0
            self.yDirection = 1

    def updateHead(self):
        self.x += self.xDirection
        self.y += self.yDirection
        self.snakeX.append(self.x)
        self.snakeY.append(self.y)
        self.drawPoint(self.x, self.y)

    def updateTail(self):
        if len(self.snakeX) >= self.maxlen:
            x = self.snakeX.pop(0)
            y = self.snakeY.pop(0)
            self.delPoint(x, y)

    def updateSnake(self):
        if self.isStart():
            self.updateHead()
            self.updateTail()

            if self.isDie():
                self.endGame()
            if self.shouldAddScore():
                self.updateScorePoint()

            self.win.after(math.floor(self.timeDelay), self.updateSnake)

    def updateScorePoint(self):
        self.maxlen += 1
        self.timeDelay *= 0.95
        while True:
            self.scoreX = random.randint(1, 59)
            self.scoreY = random.randint(1, 59)
            if self.isScorePointNotOnSnake():
                break
        self.drawPoint(self.scoreX, self.scoreY)
        self.c1.create_rectangle(0, 600, 600, 700, fill="#ffffff", outline="")
        self.c1.create_text(300, 650, text="score: "+str(self.maxlen-5), font=('Helvetica', 20))
        self.c1.pack()

    def drawPoint(self, x, y):
        self.c1.create_rectangle(
            x*10-4, y*10-4, x*10+4, y*10+4, fill="#444444", outline="")
        self.c1.pack()

    def delPoint(self, x, y):
        self.c1.create_rectangle(
            x*10-4, y*10-4, x*10+4, y*10+4, fill="#dddddd", outline="")
        self.c1.pack()

    def isStart(self):
        return self.start

    def isNotStart(self):
        return not self.start

    def isLeftRight(self):
        x=self.snakeX[-1]-self.snakeX[-2]
        return x == -1 or x==1

    def isUpDown(self):
        y=self.snakeY[-1]-self.snakeY[-2]
        return y == -1 or y==1

    def isScorePointNotOnSnake(self):
        for i in range(len(self.snakeX)):
            if self.scoreX==self.snakeX[i] and self.scoreY==self.snakeY[i]:
                return False
        return True

    def isDie(self):
        if self.x < 0:
            return True
        if self.x > 59:
            return True
        if self.y < 0:
            return True
        if self.y > 59:
            return True
        for i in range(len(self.snakeX)-1):
            if self.x==self.snakeX[i] and self.y==self.snakeY[i]:
                return True
        return False

    def shouldAddScore(self):
        return self.x == self.scoreX and self.y == self.scoreY

    def endGame(self):
        self.start = False
        self.c1.delete("all")
        self.c1.create_rectangle(0, 0, 600, 700, fill="#ffffff", outline="")
        self.c1.create_rectangle(4, 4, 595, 595, fill="#dddddd")
        self.c1.create_text(300, 300, text="按任意鍵開始", font=('Helvetica', 24))
        self.c1.create_text(300, 650, text="score: "+str(self.maxlen-5), font=('Helvetica', 20))
        self.c1.pack()


Snake()
