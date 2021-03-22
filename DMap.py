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


class DMap():
    def __init__(self, n, m):
        self.__n = n
        self.__m = m
        self.surface = np.zeros((self.__n, self.__m))
        for i in range(self.__n):
            for j in range(self.__m):
                self.surface[i][j] = -1

    def get_height(self):
        return self.__n

    def get_width(self):
        return self.__m

    def markDetectedWalls(self, env, x, y):
        #   To DO
        # mark on this map the wals that you detect
        wals = env.readUDMSensors(x, y)
        i = x - 1
        if wals[UP] > 0:
            while (i >= 0) and (i >= x - wals[UP]):
                self.surface[i][y] = 0
                i = i - 1
        if i >= 0:
            self.surface[i][y] = 1

        i = x + 1
        if wals[DOWN] > 0:
            while (i < self.__n) and (i <= x + wals[DOWN]):
                self.surface[i][y] = 0
                i = i + 1
        if i < self.__n:
            self.surface[i][y] = 1

        j = y + 1
        if wals[LEFT] > 0:
            while (j < self.__m) and (j <= y + wals[LEFT]):
                self.surface[x][j] = 0
                j = j + 1
        if j < self.__m:
            self.surface[x][j] = 1

        j = y - 1
        if wals[RIGHT] > 0:
            while (j >= 0) and (j >= y - wals[RIGHT]):
                self.surface[x][j] = 0
                j = j - 1
        if j >= 0:
            self.surface[x][j] = 1

        return None

    def image(self, x, y):
        size_of_brick = 10
        imagine = pygame.Surface((size_of_brick * self.__n, size_of_brick * self.__m))
        brick = pygame.Surface((size_of_brick, size_of_brick))
        empty = pygame.Surface((size_of_brick, size_of_brick))
        empty.fill(WHITE)
        brick.fill(BLACK)
        imagine.fill(GRAYBLUE)

        for i in range(self.__n):
            for j in range(self.__m):
                if self.surface[i][j] == 1:
                    imagine.blit(brick, (i * size_of_brick, j * size_of_brick))
                elif self.surface[i][j] == 0:
                    imagine.blit(empty, (i * size_of_brick, j * size_of_brick))

        drona = pygame.image.load("drona.png")
        drona = pygame.transform.scale(drona, (size_of_brick, size_of_brick))

        imagine.blit(drona, (x * size_of_brick, y * size_of_brick))
        return imagine
