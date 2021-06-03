# project 6
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import gym
import cv2
from gym import spaces
from keras import layers
from keras.models import Sequential
from keras.optimizers import Adam
import keras.backend as K
from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


class Model():

    def __init__(self, starting_len, grid_size, grid_shape):
        self.grid_size = grid_size
        self.grid_shape = grid_shape
        self.starting_len = starting_len
        self.history = {'step': [], 'score': []}

    def reset(self):
        self.timeDelay = 300
        self.len = self.starting_len
        self.headX, self.headY = self.getRandomXY()
        self.snakeX, self.snakeY = [self.headX], [self.headY]
        self.resetStep()
        self.resetDirection()
        self.addHead()

    def resetDirection(self):
        if self.headX > self.grid_size // 2:
            self.xDirection = -1
        else:
            self.xDirection = 1
        self.yDirection = 0

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

    def resetStep(self):
        self.step = 0

    def addStep(self):
        self.step += 1

    def getScore(self):
        return self.len - self.starting_len

    def getReward(self):
        reward = self.getScore() * (0.95 ** self.step + 1)
        return reward

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

    def updatelen(self):
        self.len += 1

    def updateTimeDelay(self):
        self.timeDelay *= 0.95

    def updateScorePoint(self, x, y):
        self.scoreX = x
        self.scoreY = y

    def getRandomXY(self):
        return random.randint(1, self.grid_size), random.randint(1, self.grid_size)

    def getSnake(self):
        return np.array([self.snakeY[::-1], self.snakeX[::-1]], dtype='float32').transpose()

    def getScorePoint(self):
        return np.array([self.scoreY, self.scoreX], dtype='float32').reshape((1, 2))

    # def getPos(self):
    #     result = np.zeros(self.grid_shape, dtype='float32')
    #     snake, scorePoint = self.getSnake(), self.getScorePoint()
    #     result[:1, :] = scorePoint
    #     result[1:1 + snake.shape[0], :] = snake
    #     return result

    def addHistory(self):
        self.history['step'].append(self.step)
        self.history['score'].append(self.getScore())


class View():
    def __init__(self, model):
        self.model = model
        self.background = np.array([210, 210, 210])
        self.wall = np.array([128, 128, 128])
        self.point = np.array([141, 141, 243])
        self.head = np.array([141, 243, 141])
        self.body = np.array([243, 141, 141])
        self.img = np.full((500, 500, 3), 255, dtype=np.uint8)
        self.scale = 500 / (self.model.grid_size + 2)
        self.gap = self.scale * 0.05

    def getImg(self):
        g = self.gap
        s = self.scale

        img = self.img.copy()
        img[:, :] = self.background
        img[int(0 * s + g):-int(0 * s + g), int(0 * s + g):int(1 * s - g)] = self.wall
        img[int(0 * s + g):-int(0 * s + g), -int(1 * s - g):-int(0 * s + g)] = self.wall
        img[int(0 * s + g):int(1 * s - g), int(0 * s + g):-int(0 * s + g)] = self.wall
        img[-int(1 * s - g):-int(0 * s + g), int(0 * s + g):-int(0 * s + g)] = self.wall

        scorePoint = self.model.getScorePoint()
        y, x = int(scorePoint[0][0]), int(scorePoint[0][1])
        img[int(y * s + g):int((y + 1) * s - g), int(x * s + g):int((x + 1) * s - g)] = self.point

        snake = self.model.getSnake()
        for key, point in enumerate(snake):
            y, x = int(point[0]), int(point[1])
            if key == 0:
                img[int(y * s + g):int((y + 1) * s - g), int(x * s + g):int((x + 1) * s - g)] = self.head
            else:
                img[int(y * s + g):int((y + 1) * s - g), int(x * s + g):int((x + 1) * s - g)] = self.body
        return img

    def getObs(self):
        obs = np.zeros(self.model.grid_shape, dtype='float32')
        obs[:, :1, 0] = 1
        obs[:, -1:, 0] = 1
        obs[:1, :, 0] = 1
        obs[-1:, :, 0] = 1

        scorePoint = self.model.getScorePoint()
        y, x = int(scorePoint[0][0]), int(scorePoint[0][1])
        obs[y, x, 1] = 1

        snake = self.model.getSnake()
        for key, point in enumerate(snake):
            y, x = int(point[0]), int(point[1])
            if key == 0:
                obs[y, x, 2] = 1
            else:
                obs[y, x, 3] = 1
        return obs

    def render(self, mode):
        if mode == 'console':
            print('console: ', end='')
            print(self.getObs()[:, :, 3])
        else:
            cv2.imshow('Snake by miku3920', self.getImg())
            cv2.waitKey(self.model.getTimeDelay())


class Controller():

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def leftKey(self):
        if not self.isLeftRight():
            self.model.setLeft()
            self.model.addStep()

    def rightKey(self):
        if not self.isLeftRight():
            self.model.setRight()
            self.model.addStep()

    def upKey(self):
        if not self.isUpDown():
            self.model.setUp()
            self.model.addStep()

    def downKey(self):
        if not self.isUpDown():
            self.model.setDown()
            self.model.addStep()

    def reset(self):
        self.model.reset()
        self.updateScorePoint()

    def updateSnake(self):
        self.updateHead()
        self.updateTail()

        reward = -0.001
        done = self.isDie()
        info = {}
        if done:
            reward = -1.0
            self.model.addHistory()
        if self.shouldAddScore():
            self.model.updatelen()
            self.model.updateTimeDelay()
            self.updateScorePoint()
            reward = self.model.getReward()

        pos = self.view.getObs()

        return pos, reward, done, info

    def updateHead(self):
        self.model.addHead()

    def updateTail(self):
        if len(self.model.snakeX) > self.model.len:
            self.model.delTail()

    def updateScorePoint(self):
        while True:
            x, y = self.model.getRandomXY()
            self.model.updateScorePoint(x, y)
            if self.isScorePointNotOnSnake():
                break

    def isLeftRight(self):
        x = self.model.snakeX[-1] - self.model.snakeX[-2]
        return x == -1 or x == 1

    def isUpDown(self):
        y = self.model.snakeY[-1] - self.model.snakeY[-2]
        return y == -1 or y == 1

    def isScorePointNotOnSnake(self):
        for i in range(len(self.model.snakeX)):
            if self.model.scoreX == self.model.snakeX[i] and self.model.scoreY == self.model.snakeY[i]:
                return False
        return True

    def isDie(self):
        if self.model.headX < 1:
            return True
        if self.model.headX > self.model.grid_size:
            return True
        if self.model.headY < 1:
            return True
        if self.model.headY > self.model.grid_size:
            return True
        for i in range(len(self.model.snakeX) - 1):
            if self.model.headX == self.model.snakeX[i] and self.model.headY == self.model.snakeY[i]:
                return True
        return False

    def shouldAddScore(self):
        return self.model.headX == self.model.scoreX and self.model.headY == self.model.scoreY


class Snake(gym.Env):
    metadata = {'render.modes': ['console']}

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, grid_size=10, starting_len=4):
        super(Snake, self).__init__()

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(
            low=0, high=1,
            shape=(grid_size + 2, grid_size + 2, 4), dtype=np.float32
        )

        self.model = Model(starting_len, grid_size, self.observation_space.shape)
        self.view = View(self.model)
        self.controller = Controller(self.view, self.model)

    def reset(self):
        self.controller.reset()
        return self.view.getObs()

    def step(self, action):
        if action == self.UP:
            self.controller.upKey()
        elif action == self.DOWN:
            self.controller.downKey()
        elif action == self.LEFT:
            self.controller.leftKey()
        elif action == self.RIGHT:
            self.controller.rightKey()

        return self.controller.updateSnake()

    def render(self, mode='console'):
        self.view.render(mode)

    def draw(self):
        plt.plot(self.model.history['score'])
        plt.plot(np.log10(np.array(self.model.history['step'])))
        plt.title('Snake by miku3920')
        plt.legend(['score', 'step (10^x)'], loc='upper left')
        plt.show()

    def close(self):
        pass


def swish(x):
    return x * K.sigmoid(x)


env = Snake(5, 6)

obs = env.reset()
obs, reward, done, info = env.step(0)
env.render(mode='cv2')
cv2.waitKey(0)
cv2.destroyAllWindows()
nb_actions = env.action_space.n

model = Sequential()
model.add(layers.Input(shape=(1,) + env.observation_space.shape))
model.add(layers.Flatten())
for i in range(3):
    model.add(layers.Dense(1024, swish))
model.add(layers.Dense(nb_actions))
print(model.summary())

dqn = DQNAgent(
    model=model,
    nb_actions=nb_actions,
    memory=SequentialMemory(limit=50000, window_length=1),
    target_model_update=1e-2,
    policy=BoltzmannQPolicy()
)
dqn.compile(Adam(1e-5), metrics=['mse', 'mae', 'logcosh'])

dqn.fit(env, nb_steps=10000000, visualize=False, verbose=2)

dqn.save_weights(f'dqn_snake_weights.h5f', overwrite=True)

env.draw()
env.render(mode='cv2')
cv2.waitKey(0)
cv2.destroyAllWindows()

dqn.test(env, nb_episodes=5, visualize=True)

cv2.waitKey(0)
cv2.destroyAllWindows()
