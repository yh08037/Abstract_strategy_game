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

def eventHandle(mousePos):
    escClicked = False
    leftMouseClicked = False
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                escClicked = True
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == leftMouse:
            leftMouseClicked = True
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
    return escClicked, leftMouseClicked, mousePos

def drawobject(object, color):
    pass


#RGB 포맷으로 색을 정의합니다.
color = {'darkgray':(49, 51, 53), 'black':(0,0,0)}

leftMouse = 1
rightMouse = 3
resolution = (1280, 720)
FPS = 60

pygame.init()
font = 'myfont.ttf'
pygame.display.set_caption("chess")
clock = pygame.time.Clock()
screen = pygame.display.set_mode(resolution)

boardPositionVertex = ((340, 60), (940,60), (940,660), (340,660))
whiteObject = {'king':[()], 'queen':[()], 'bishop':[(), ()], 'rook':[(), ()],
'knight':[(), ()], 'pawn':[(),(),(),(),(),(),(),()]}
blackObject = {'king':[()], 'queen':[()], 'bishop':[(), ()], 'rook':[(), ()],
'knight':[(), ()], 'pawn':[(),(),(),(),(),(),(),()]}

mousePos = (0, 0)
while True:
    eventHandle(mousePos)
    screen.fill(color['darkgray'])

    chessboard = pygame.image.load('chessboard.png')
    screen.blit(chessboard, boardPositionVertex[0])
    pygame.draw.lines(screen, color['black'], True, boardPositionVertex, 6)


    drawobject(whiteObject, 'white')
    drawobject(blackObject, 'black')

    pygame.display.update()
    clock.tick(FPS)
