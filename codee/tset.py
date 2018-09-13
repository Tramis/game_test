import pygame
from pygame.locals import *
import sys

win = pygame.display.set_mode((400, 400))
pygame.display.set_caption('test')

flag = 0

while True:
    if flag == 1000000:
        flag = 0
        print('im here')
    flag += 1

    event = pygame.event.get()
    for i in event:
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()

        if  i.type == pygame.KEYDOWN:
            print("d")
        elif i.type == pygame.KEYUP:
            print("u")
