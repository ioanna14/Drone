# import the pygame module, so you can use it
import pickle, pygame, sys
import time

from pygame.locals import *
from random import random, randint
import numpy as np

# Creating some colors
BLUE = (0, 0, 255)
GRAYBLUE = (50, 120, 120)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# define directions
UP = 0
DOWN = 2
LEFT = 1
RIGHT = 3

# define indexes variations
v = [[-1, 0], [1, 0], [0, 1], [0, -1]]


class Environment:
    def __init__(self, n, m, fill):
        self.__n = n
        self.__m = m
        self.__fill_gradient = fill
        self.__surface = np.zeros((self.__n, self.__m))

    def is_occupied(self, x, y):
        return self.__surface[x][y] == 1

    def randomMap(self):
        for i in range(self.__n):
            for j in range(self.__m):
                if random() <= self.__fill_gradient:
                    self.__surface[i][j] = 1

    def __str__(self):
        string = ""
        for i in range(self.__n):
            for j in range(self.__m):
                string = string + str(int(self.__surface[i][j]))
            string = string + "\n"
        return string

    def readUDMSensors(self, x, y):
        readings = [0, 0, 0, 0]
        # UP
        xf = x - 1
        while (xf >= 0) and (self.__surface[xf][y] == 0):
            xf = xf - 1
            readings[UP] = readings[UP] + 1
        # DOWN
        xf = x + 1
        while (xf < self.__n) and (self.__surface[xf][y] == 0):
            xf = xf + 1
            readings[DOWN] = readings[DOWN] + 1
        # LEFT
        yf = y + 1
        while (yf < self.__m) and (self.__surface[x][yf] == 0):
            yf = yf + 1
            readings[LEFT] = readings[LEFT] + 1
        # RIGHT
        yf = y - 1
        while (yf >= 0) and (self.__surface[x][yf] == 0):
            yf = yf - 1
            readings[RIGHT] = readings[RIGHT] + 1

        return readings

    def saveEnvironment(self, numFile):
        with open(numFile, 'wb') as f:
            pickle.dump(self, f)
            f.close()

    def loadEnvironment(self, numFile):
        with open(numFile, "rb") as f:
            dummy = pickle.load(f)
            self.__n = dummy.__n
            self.__m = dummy.__m
            self.__surface = dummy.__surface
            f.close()

    def image(self, colour=BLUE, background=WHITE):
        size_of_brick = 10
        imagine = pygame.Surface((size_of_brick * self.__n, size_of_brick * self.__m))
        brick = pygame.Surface((size_of_brick, size_of_brick))
        brick.fill(BLUE)
        imagine.fill(WHITE)
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__surface[i][j] == 1:
                    imagine.blit(brick, (i * size_of_brick, j * size_of_brick))

        return imagine