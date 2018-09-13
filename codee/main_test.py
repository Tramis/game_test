import pygame
from pygame.locals import *
from sys import exit

pygame.init()

winSize = [640, 480]
potInit = (0, 0)
potCar = [10, 10]
moveDict = {pygame.K_LEFT: 0, pygame.K_RIGHT: 0, pygame.K_UP: 0, pygame.K_DOWN: 0}

threeCar1 = pygame.image.load('img/twr1.png')
threeCar2 = pygame.image.load('img/twr2.png')
flagCar = [0]

strIn = 'in'
strOut = 'out'

win = pygame.display.set_mode(winSize)
pygame.display.set_caption('今晚，我在秋名山等你')
backGround = pygame.image.load('img/bg.jpg')

def showCar(flag):
    if flag[0] == 1000:
        flag[0] = 0
    if flag[0] % 50 < 25:
        win.blit(threeCar1, potCar)
    else:
        win.blit(threeCar2, potCar)
    flag[0] += 1

def moveObject(pot):
    pot[0] += (moveDict[pygame.K_RIGHT] - moveDict[pygame.K_LEFT])
    pot[0] += (moveDict[pygame.K_DOWN] - moveDict[pygame.K_UP])
    if pot[0] < 0:
        pot[0] = 0
    if pot[1] < 0:
        pot[1] = 0

def showText(text):
    font = pygame.font.Font('freesansbold.ttf', 16)
    surText = font.render(text, True, (0, 0, 0), (255, 255, 255))
    win.blit(surText, potInit)
    pygame.display.update()

isCon = True
while isCon:
    win.blit(backGround, potInit)
    showCar(flagCar)

    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()

        if i.type == pygame.KEYDOWN:
            if i.key in moveDict:
                moveDict[i.key] = 10

        if i.type == pygame.KEYUP:
            if i.key in moveDict:
                moveDict[i.key] = 0

    moveObject(potCar)