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

#printText 함수
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
colorGray = (127, 127, 127)
colorBlack = (0, 0, 0)

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
        boardAllElement.append((340 + i * 40, 80 + j * 40))
    boardAll.append(boardAllElement)
    
whitePlaced = []
blackPlaced = []
circleSize = 17
Is_turn_black = True
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
            
    screen.fill(colorDarkGray)  # 바탕화면
    
    for i in range(15):
        #스크린, 색깔, x좌표, y좌표, (안티얼레이싱 활성화 여부)
        pygame.draw.aaline(screen, colorLightGray, boardAll[0][i], boardAll[14][i])
        pygame.draw.aaline(screen, colorLightGray, boardAll[i][0], boardAll[i][14])
    boardVertex = [boardAll[0][0], boardAll[0][14], boardAll[14][14], boardAll[14][0]]
    pygame.draw.aalines(screen, colorWhite, False, boardVertex)
    
    #i,j 값을 참고하여, x,y자리에 해당하는 곳에 희미한 선이 나온다.
    IsBreak = False
    for x in range(15):
        for y in range(15):
            if Is_mousePos_in_boardAll(mousePos, boardAll[x][y]):
                pygame.draw.circle(screen, colorLightGray, boardAll[x][y], circleSize)
                if leftMouseClicked:
                    Is_it_placed = boardAll[x][y] in whitePlaced or boardAll[x][y] in blackPlaced
                    if Is_turn_black and not Is_it_placed:
                        blackPlaced.append(boardAll[x][y])
                        Is_turn_black = False
                    elif not Is_turn_black and not Is_it_placed:
                        whitePlaced.append(boardAll[x][y])
                        Is_turn_black = True                             
                IsBreak = True
                break
        if IsBreak:
            break
    
    # 좌표에 있는 알맞은 돌 나타냄
    for point in blackPlaced:
        pygame.draw.circle(screen, colorBlack, point, circleSize)
    for point in whitePlaced:
        pygame.draw.circle(screen, colorWhite, point, circleSize)
    
    if Is_turn_black:
        printText("Black Turn!", colorWhite, (1080, 100), 40)       
    elif not Is_turn_black:
        printText("White Turn!", colorWhite, (1080, 100), 40)

    '''
    Is_game_finished = 판별식(blackPlaced) (whitePlaced)
       출력문은 5개가 맞추어져있다!, 아직이다...
    '''
    pygame.display.update()
    clock.tick(FPS)
    
    
    
    
    
    
    




