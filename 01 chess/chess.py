import pygame
from pygame.locals import *
import sys
import pygame.gfxdraw
import math

def printText(msg, color, pos, fontsize, _font = 'myfont.ttf'):
    font = pygame.font.Font(_font, fontsize)
    text = font.render(msg, True, color)
    textRect = text.get_rect()
    textRect.center = pos
    screen.blit(text, textRect)

pygame.init()
font = 'myfont.ttf'

#RGB 포맷으로 색을 정의합니다.
colorRed = (255, 0, 0)
colorBrightRed = (222, 30, 30)
colorOrange = (255, 83, 51)
colorDarkGray = (49, 51, 53)
colorLightGray = (160, 160, 160)
colorBlue = (0, 0, 255)
colorBrightBlue = (0, 176, 255)
colorWhite = (255, 255, 255)
colorMilkWhite = (223, 220, 205)
colorGray = (127, 127, 127)
colorBlack = (0, 0, 0)

leftMouse = 1
rightMouse = 3
resolution = (1280, 720)
FPS = 60


pygame.init()
pygame.display.set_caption("chess")
clock = pygame.time.Clock()
screen = pygame.display.set_mode(resolution)
