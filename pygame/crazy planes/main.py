# or yanko and michael sharon crazy planes

import pygame
import random
import time

#vars
directions = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0)]

#funcs
def is_square_empty(planes_arr, x, y):
    for plane in planes_arr:
        if plane.x == x and plane.y == y:
            return False
    return True

#class CrazyPlane
class CrazyPlane:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        #if in range set image
        if 0 <= direction <= 7:
            if direction == 0:
                self.image = pygame.image.load("crazy_plane-0.png")
            if direction == 1:
                self.image = pygame.image.load("crazy_plane-1.png")
            if direction == 2:
                self.image = pygame.image.load("crazy_plane-2.png")
            if direction == 3:
                self.image = pygame.image.load("crazy_plane-3.png")
            if direction == 4:
                self.image = pygame.image.load("crazy_plane-4.png")
            if direction == 5:
                self.image = pygame.image.load("crazy_plane-5.png")
            if direction == 6:
                self.image = pygame.image.load("crazy_plane-6.png")
            if direction == 7:
                self.image = pygame.image.load("crazy_plane-7.png")

    def update(self, planes_arr):
        rand = random.randint(0, 7)
        xUpdate = self.x + 65 * directions[rand][0]
        yUpdate = self.y + 65 * directions[rand][1]

        while xUpdate > 585 or xUpdate < 0 or yUpdate > 585 or yUpdate < 0 or is_square_empty(planes_arr, xUpdate, yUpdate) == False:
            rand = random.randint(0, 7)
            xUpdate = self.x + 65 * directions[rand][0]
            yUpdate = self.y + 65 * directions[rand][1]
            #print("---------", xUpdate, " ", yUpdate)

        #change pos
        self.x = xUpdate
        self.y = yUpdate

        #change image
        if rand == 0:
            self.image = pygame.image.load("crazy_plane-0.png")
        elif rand == 1:
            self.image = pygame.image.load("crazy_plane-1.png")
        elif rand == 2:
            self.image = pygame.image.load("crazy_plane-2.png")
        elif rand == 3:
            self.image = pygame.image.load("crazy_plane-3.png")
        elif rand == 4:
            self.image = pygame.image.load("crazy_plane-4.png")
        elif rand == 5:
            self.image = pygame.image.load("crazy_plane-5.png")
        elif rand == 6:
            self.image = pygame.image.load("crazy_plane-6.png")
        elif rand == 7:
            self.image = pygame.image.load("crazy_plane-7.png")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))



def main():
    # constants
    WINDOW_WIDTH = 650
    WINDOW_HEIGHT = 650

    # init screen
    pygame.init()
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")

    # colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    screen.fill(WHITE)  # fill in white
    pygame.display.flip()

    plane1 = CrazyPlane(0, 0, 4)
    plane2 = CrazyPlane(585, 0, 6)
    plane3 = CrazyPlane(585, 585, 0)
    plane4 = CrazyPlane(0, 585, 2)
    planes_list = [plane1, plane2, plane3, plane4]

    finish = False

    while not finish:
        screen.fill(WHITE)  # fill in white (default)
        for event in pygame.event.get():
            # if quit
            if event.type == pygame.QUIT:
                finish = True
             # if button was clicked
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    finish = True
        for plane in planes_list:
            plane.draw(screen)
            plane.update(planes_list)
        pygame.display.flip()
        pygame.time.delay(1000)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()

