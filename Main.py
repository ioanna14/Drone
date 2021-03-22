# import the pygame module, so you can use it
import time
from random import randint

import pygame

from DMap import DMap
from Drone import Drone
from Environment import Environment

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


# define a main function
def main():
    # we create the environment
    n = 50
    m = 10
    fill = 0.3
    e = Environment(n, m, fill)
    e.randomMap()
    # print(str(e))

    # we create the map
    the_map = DMap(n, m)

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("drone exploration")

    # we position the drone somewhere in the area
    x = randint(0, n - 1)
    y = randint(0, m - 1)
    while e.is_occupied(x, y):
        x = randint(0, n - 1)
        y = randint(0, m - 1)

    # create drone
    d = Drone(x, y)

    # create a surface on screen that has the size of 1000 x 500
    screen = pygame.display.set_mode((10*2*n, 10*m))
    screen.fill(WHITE)
    screen.blit(e.image(), (0, 0))

    # define a variable to control the main loop
    running = True

    the_map.markDetectedWalls(e, d.x, d.y)

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                pygame.quit()
                return
            # if event.type == KEYDOWN:
            # use this function instead of move
            # d.move(m)

        time.sleep(0.1)
        running = d.moveDSF(the_map)
        the_map.markDetectedWalls(e, d.x, d.y)
        screen.blit(the_map.image(d.x, d.y), (n*10, 0))
        pygame.display.flip()

    pygame.quit()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
