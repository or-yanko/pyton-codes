#or yanko yud gimel1 hadasa neurim
import pygame
import math
import random

class DrawableObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load('ball.jpg')
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#draw o from lines on the screen
def draw_lines_circle(screen):
    BLACK = [0, 0, 0]
    PI = 3.14159265359
    for i in range(100):
        x = math.cos(2*PI/100*i)
        y = math.sin(2*PI/100*i)
        pygame.draw.line(screen, BLACK, [350, 250], [350+150*x, 250+150*y])
#func that draw the moving ball in changed place
def draw_moving_ball(screen, x, y, xvec, yvec, width, hight):
    speed = 1
    if x + 118 > width:
        xvec = -1
    if x < speed:
        xvec = 1
    if y + 117 > hight:
        yvec = -1
    if y < speed:
        yvec = 1
    x += xvec*speed
    y += yvec*speed
    ballImg = pygame.image.load('ball.jpg')
    ballImg.set_colorkey((0, 0, 0))
    screen.blit(ballImg, (x, y))
    return x, y, xvec, yvec
#write your name in red in the middle of the screen
def write_name(screen, width, hight):
    RED = (255, 0, 0)
    pygame.font.init()
    myfont = pygame.font.SysFont('didot.ttc', 200)
    name = myfont.render("or yanko", True, RED)
    screen.blit(name, (width/2 - 280, hight/2 - 130))
#draw sprite in pos
def draw_sprite_from_array(screen, ball):
    img = ball.image
    x = ball.rect.x
    y = ball.rect.y
    img.set_colorkey((0, 0, 0))
    screen.blit(img, (x, y))



def main1():
    # constants
    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 500

    # init screen
    pygame.init()
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")

    #white screen
    WHITE = (255, 255, 255)
    color = WHITE
    screen.fill(WHITE)#fill in white
    pygame.display.flip()

    ballx = 100
    bally = 100
    ballxvec = 1
    ballyvec = 1

    #active_now and array of sprites
    active_now = ''
    sprites_arr = []

    #sounds
    sound1 = "sound1.mp3"
    beat1 = "beat1.mp3"
    pygame.mixer.init()

    finish = False

    while not finish:
        screen.fill(WHITE)  # fill in white (default)

        for event in pygame.event.get():
            #if quit
            if event.type == pygame.QUIT:
                finish = True
            #if mouse was clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click
                    #add sprite to the array
                    if active_now == 'r' or active_now == 's':
                        pygame.mixer.music.stop()
                    active_now = 'l'
                    x1, y1 = pygame.mouse.get_pos()
                    ball = DrawableObject(x1, y1)
                    sprites_arr.append(ball)
                if event.button == 3:  # right click
                    if active_now == 'r':
                        active_now = ''
                        pygame.mixer.music.stop()
                    else:
                        active_now = 'r'
                        pygame.mixer.music.load(beat1)
                        pygame.mixer.music.play()
            #if button was clicked
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    if active_now == 'r' or active_now == 's':
                        pygame.mixer.music.stop()
                    active_now = 'j'
                elif event.key == pygame.K_x:
                    finish = True
                elif event.key == pygame.K_k:
                    if active_now == 'r' or active_now == 's':
                        pygame.mixer.music.stop()
                    active_now = 'k'
                elif event.key == pygame.K_m:
                    if active_now == 'r' or active_now == 's':
                        pygame.mixer.music.stop()
                    active_now = 'm'
                elif event.key == pygame.K_n:
                    if active_now == 'r' or active_now == 's':
                        pygame.mixer.music.stop()
                    active_now = 'n'
                    color = (random.randrange(0,255,1), random.randrange(0,255,1), random.randrange(0,255,1))
                elif event.key == pygame.K_o:
                    if active_now == 'r' or active_now == 's':
                        pygame.mixer.music.stop()
                    active_now = 'o'
                elif event.key == pygame.K_s:
                    if active_now == 's':
                        active_now =''
                        pygame.mixer.music.stop()
                    else:
                        active_now = 's'
                        pygame.mixer.music.load(sound1)
                        pygame.mixer.music.play()
                elif event.key == pygame.K_SPACE:
                    if active_now == 'r' or active_now == 's':
                        pygame.mixer.music.stop()
                    sprites_arr = []
                    screen.fill(WHITE)  # fill in white (default)
                    pygame.display.flip()
                    active_now = ''

        #draw if was clicked
        if active_now != '':
            if active_now == 'j':
                draw_lines_circle(screen)
            if active_now == 'k':
                ballx, bally, ballxvec, ballyvec = draw_moving_ball(screen, ballx, bally, ballxvec, ballyvec, WINDOW_WIDTH, WINDOW_HEIGHT)
            if active_now == 'm':
                write_name(screen,WINDOW_WIDTH, WINDOW_HEIGHT)
            if active_now == 'n':
                screen.fill(color)  # fill in white
            if active_now == 'o':
                pygame.draw.line(screen, (0, 0, 0), [0,WINDOW_HEIGHT/2], [WINDOW_WIDTH, WINDOW_HEIGHT/2], 10)
            if active_now == 'l':
                for sprite in sprites_arr:
                    draw_sprite_from_array(screen, sprite)
            pygame.display.flip()


    pygame.quit()
    quit()



if __name__ == '__main__':
    main1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
