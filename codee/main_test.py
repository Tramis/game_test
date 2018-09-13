import pygame
from pygame.locals import *
from sys import exit

pygame.init()

winSize = [640, 480]
potInit = (0, 0)

potCar = (10, 10)

threeCar1 = pygame.image.load('img/twr1.png')
threeCar2 = pygame.image.load('img/twr2.png')
flag = 0

win = pygame.display.set_mode(winSize)
pygame.display.set_caption('今晚，我在秋名山等你')
backGround = pygame.image.load('img/bg.jpg')

isCon = True

while isCon:
    # win.blit(backGround, potInit)
    # if flag == 1000:
    #     flag = 0
    # if flag % 50 < 25:
    #     win.blit(threeCar1, potCar)
    # else:
    #     win.blit(threeCar2, potCar)
    # flag += 1

    pygame.display.update()
    print('in while')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == KEYDOWN:
        print('in for')