import pygame
from pygame.locals import *
import sys
import pygame.gfxdraw
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

def guideline(screen, color, boardPoint, circleSize):
    pointlist = [(boardPoint[0] - 15, boardPoint[1]+7), (boardPoint[0] - 15, boardPoint[1] + 15), (boardPoint[0] - 7, boardPoint[1] +15)]
    pygame.draw.lines(screen, color, False, pointlist)
    pointlist = [(boardPoint[0] + 15, boardPoint[1]+7), (boardPoint[0] + 15, boardPoint[1] + 15), (boardPoint[0] + 7, boardPoint[1] +15)]
    pygame.draw.lines(screen, color, False, pointlist)
    pointlist = [(boardPoint[0] + 15, boardPoint[1]-7), (boardPoint[0] + 15, boardPoint[1] - 15), (boardPoint[0] + 7, boardPoint[1] -15)]
    pygame.draw.lines(screen, color, False, pointlist)
    pointlist = [(boardPoint[0] - 15, boardPoint[1]-7), (boardPoint[0] - 15, boardPoint[1] - 15), (boardPoint[0] - 7, boardPoint[1] -15)]
    pygame.draw.lines(screen, color, False, pointlist)
    pygame.gfxdraw.aacircle(screen, boardPoint[0], boardPoint[1], 2, color)

def Check_game_finished(placed):
    for stone in placed:
        for i in range(1, 5):
            if not (stone[0] - 40 * i, stone[1] - 40 * i) in placed:
                break
        else:
            return True

        for i in range(1, 5):
            if not (stone[0], stone[1] - 40 * i) in placed:
                break
        else:
            return True

        for i in range(1, 5):
            if not (stone[0] + 40 * i, stone[1] - 40 * i) in placed:
                break
        else:
            return True

        for i in range(1, 5):
            if not (stone[0] + 40 * i, stone[1]) in placed:
                break
        else:
            return True

        for i in range(1, 5):
            if not (stone[0] + 40 * i, stone[1] + 40 * i) in placed:
                break
        else:
            return True

        for i in range(1, 5):
            if not (stone[0], stone[1] + 40 * i) in placed:
                break
        else:
            return True

        for i in range(1, 5):
            if not (stone[0] - 40 * i, stone[1] + 40 * i) in placed:
                break
        else:
            return True

        for i in range(1, 5):
            if not (stone[0] - 40 * i, stone[1]) in placed:
                break
        else:
            return True
    return False
    # 돌 하나에 대해서 주변에 돌 있는지 확인하고 방향(8방향)을 체크,
    # 그리고 두번째 돌 하나에 대해서 가지고 있는 방향을 이용하여 세번째 돌이 나열되어있는지 체크...
    # 5번 반혹 후 하나라도 있으면 True, 없으면 False값을 결정

#흑돌의 33 44 6목 이상을 막습니다.
def cannotplace(placed):
    pass


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
pygame.display.set_caption("오목")
clock = pygame.time.Clock()
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
IsBlackWin = False
IsWhiteWin = False

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

    screen.fill(colorMilkWhite)  # 바탕화면

    for i in range(15):
        #스크린, 색깔, x좌표, y좌표, (안티얼레이싱 활성화 여부)
        pygame.draw.line(screen, colorBlack, boardAll[0][i], boardAll[14][i])
        pygame.draw.line(screen, colorBlack, boardAll[i][0], boardAll[i][14])
    boardVertex = [boardAll[0][0], boardAll[0][14], boardAll[14][14], boardAll[14][0]]
    pygame.draw.aalines(screen, colorBlack, True, boardVertex)
    pygame.gfxdraw.aacircle(screen, boardAll[3][3][0], boardAll[3][3][1], 2, colorBlack)
    pygame.gfxdraw.aacircle(screen, boardAll[3][-3][0], boardAll[3][-4][1], 2, colorBlack)
    pygame.gfxdraw.aacircle(screen, boardAll[-4][3][0], boardAll[-4][3][1], 2, colorBlack)
    pygame.gfxdraw.aacircle(screen, boardAll[-4][-4][0], boardAll[-4][-4][1], 2, colorBlack)
    pygame.gfxdraw.aacircle(screen, boardAll[7][7][0], boardAll[7][7][1], 2, colorBlack)


    #i,j 값을 참고하여, x,y자리에 해당하는 곳에 희미한 선이 나온다.
    IsBreak = False
    for x in range(15):
        for y in range(15):
            if Is_mousePos_in_boardAll(mousePos, boardAll[x][y]):
                Is_it_placed = boardAll[x][y] in whitePlaced or boardAll[x][y] in blackPlaced
                if not Is_it_placed:
                    guideline(screen, colorGray, boardAll[x][y], circleSize)
                    if leftMouseClicked and Is_turn_black:
                        blackPlaced.append(boardAll[x][y])
                        IsBlackWin = Check_game_finished(blackPlaced)
                        Is_turn_black = False
                    elif leftMouseClicked and not Is_turn_black:
                        whitePlaced.append(boardAll[x][y])
                        IsWhiteWin = Check_game_finished(whitePlaced)
                        Is_turn_black = True
                IsBreak = True
                break
        if IsBreak:
            break
    if IsBlackWin:
        printText('black wins!', colorBlack, (150, 100), 40)
    elif IsWhiteWin:
        printText('white wins!', colorBlack, (150, 100), 40)

    # 좌표에 있는 알맞은 돌 나타냄
    for point in blackPlaced:
        pygame.draw.circle(screen, colorBlack, point, circleSize)
        pygame.gfxdraw.aacircle(screen, point[0], point[1], circleSize, colorWhite)
    for point in whitePlaced:
        pygame.draw.circle(screen, colorWhite, point, circleSize)
        pygame.gfxdraw.aacircle(screen, point[0], point[1], circleSize, colorGray)

    if Is_turn_black:
        printText("Black Turn!", colorBlack, (1080, 100), 40)
    elif not Is_turn_black:
        printText("White Turn!", colorBlack, (1080, 100), 40)

    pygame.display.update()
    clock.tick(FPS)
