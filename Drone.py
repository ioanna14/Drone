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


class Drone():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = []
        self.path = []

    def move(self, detectedMap):
        pressed_keys = pygame.key.get_pressed()
        if self.x > 0:
            if pressed_keys[K_UP] and detectedMap.surface[self.x - 1][self.y] == 0:
                self.x = self.x - 1
        if self.x < detectedMap.get_height() - 1:
            if pressed_keys[K_DOWN] and detectedMap.surface[self.x + 1][self.y] == 0:
                self.x = self.x + 1

        if self.y > 0:
            if pressed_keys[K_LEFT] and detectedMap.surface[self.x][self.y - 1] == 0:
                self.y = self.y - 1
        if self.y < detectedMap.get_width() - 1:
            if pressed_keys[K_RIGHT] and detectedMap.surface[self.x][self.y + 1] == 0:
                self.y = self.y + 1

    def moveDSF(self, detectedMap):
        # up
        if self.x > 0:
            if detectedMap.surface[self.x - 1][self.y] == 0 and (self.x - 1, self.y) not in self.visited:
                self.visited.append((self.x - 1, self.y))
                self.path.append((self.x - 1, self.y))
                self.x = self.x - 1
                return True
        # right
        if self.y < detectedMap.get_width() - 1:
            if detectedMap.surface[self.x][self.y + 1] == 0 and (self.x, self.y + 1) not in self.visited:
                self.visited.append((self.x, self.y + 1))
                self.path.append((self.x, self.y + 1))
                self.y = self.y + 1
                return True
        # down
        if self.x < detectedMap.get_height() - 1:
            if detectedMap.surface[self.x + 1][self.y] == 0 and (self.x + 1, self.y) not in self.visited:
                self.visited.append((self.x + 1, self.y))
                self.path.append((self.x + 1, self.y))
                self.x = self.x + 1
                return True
        # left
        if self.y > 0:
            if detectedMap.surface[self.x][self.y - 1] == 0 and (self.x, self.y - 1) not in self.visited:
                self.visited.append((self.x, self.y - 1))
                self.path.append((self.x, self.y - 1))
                self.y = self.y - 1
                return True
        if len(self.path) != 0:
            (x, y) = self.path.pop(len(self.path) - 1)
            self.x = x
            self.y = y
            return True

        return False
