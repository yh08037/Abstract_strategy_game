import pygame
from pygame.locals import *
import sys
import math

def Is_mousePos_in_boardAll(mousePos, boardPoint):
    Check_boardPointX = boardPoint[0] - 20  < mousePos[0] < boardPoint[0] + 20
    Check_boardPointY = boardPoint[1] - 20  < mousePos[1] < boardPoint[1] + 20
    if Check_boardPointX and Check_boardPointY :
        return True 
    return False

pygame.init()

'''
font = 'myfont.ttf'
'''

#RGB 포맷으로 색을 정의합니다.
colorRed            = (255,   0,   0)
colorBrightRed      = (222,  30,  30)
colorOrange         = (255,  83,  51)
colorDarkGray       = ( 49,  51,  53)
colorLightGray      = (160, 160, 160)
colorBlue           = (  0,   0, 255)
colorBrightBlue     = (  0, 176, 255)
colorWhite          = (255, 255, 255)
colorGray           = (127, 127, 127)
colorBlack          = (  0,   0,   0)

leftMouse = 1
rightMouse = 3

resolution = (1280, 720)
FPS = 60
clock = pygame.time.Clock()


pygame.init()
pygame.display.set_caption("오목")
screen = pygame.display.set_mode(resolution)

boardAll = []
for i in range(15):
    boardAllElement = []
    for j in range(15):
        boardAllElement.append((340 + i * 40, 60 + j * 40))
    boardAll.append(boardAllElement)

    
    

while True:
    leftMouseClicked = False  #초기 세팅
    escClicked = False
    for event in pygame.event.get():  # 키보드, 마우스 입력값 확인
        if event.type == KEYDOWN:  # 누르는 행위
            if event.key == K_ESCAPE:  # ESC
                escClicked = True
    if event.type == QUIT:  # X버튼 누르면 생기는 일
        pygame.quit()
        sys.exit()
    if event.type == MOUSEBUTTONDOWN and event.button == leftMouse:  # 주클릭
        leftMouseClicked = True
    if event.type == pygame.MOUSEMOTION:  # 마우스 움직이면 그 좌표를 반환
        mousePos = event.pos  # mousePos = (x좌표, y좌표)
            
    screen.fill(colorDarkGray)
    
    for i in range(15):
        pygame.draw.aaline(screen, colorLightGray, boardAll[0][i], boardAll[14][i])
        pygame.draw.aaline(screen, colorLightGray, boardAll[i][0], boardAll[i][14])
    pygame.draw.aalines(screen, colorWhite, False, [boardAll[0][0], boardAll[0][14], boardAll[14][14], boardAll[14][0]])
    
    
    #i,j 값을 참고하여, x,y자리에 해당하는 곳에 희미한 선이 나온다.
    IsBreak = False
    for x in range(15):
        for y in range(15):
            if Is_mousePos_in_boardAll(mousePos, boardAll[x][y]):
                pygame.draw.circle(screen, colorLightGray, boardAll[x][y], 10)                
        IsBreak = True
        break
    if IsBreak:
        break
    
    pygame.display.update()
    clock.tick(FPS)
    
    
    
    
    
    
    
    
    
    
    
    
