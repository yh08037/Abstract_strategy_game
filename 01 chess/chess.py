import pygame
from pygame.locals import *
import sys
import pygame.gfxdraw
import math

# 텍스트를 출력하는 함수
def printText(msg, color, pos, fontsize, _font = 'myfont.ttf'):
    font = pygame.font.Font(_font, fontsize)
    text = font.render(msg, True, color)
    textRect = text.get_rect()
    textRect.center = pos
    screen.blit(text, textRect)

# 입력 관련에 대해서 조사합니다.
leftMouse = 1
rightMouse = 3
mousePos = (0, 0)
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

# 체스 말을 그립니다.
def drawobject(object, color):
    pass

# 각 기물의 모양을 불러올 좌표를 정합니다.
object = {
'blackKing' : [((0, 0), (70, 70))],
'blackQueen' : [((128, 0), (200, 70))],
'blackBishop' : [((264, 0), (330, 70))],
'blackKnight' : [((393, 0), (467, 70))],
'blackRook' : [((526, 0), (600, 70))],
'blackPawn' : [((669, 0), (719, 70))],
'whiteKing' : [((0, 112), (70, 184))],
'WhiteQueen' : ((128, 112), (200, 184)),
'whiteBishop' : ((264, 112), (330, 200)),
'whiteKnight' : ((393, 112), (467, 200)),
'whiteRook' : ((526, 112), (600, 200)),
'whitePawn' : ((669, 112), (719, 200))
}

#RGB 포맷으로 색을 정의합니다.
color = {
'darkgray' : (49, 51, 53),
'black' : (0,0,0)
}

#화면 설정
resolution = (1280, 720)
FPS = 60

pygame.init()
font = 'myfont.ttf'
pygame.display.set_caption("chess")
clock = pygame.time.Clock()
screen = pygame.display.set_mode(resolution)

boardPositionVertex = ((340, 60), (940,60), (940,660), (340,660))

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
