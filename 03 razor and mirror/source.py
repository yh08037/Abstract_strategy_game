import sys
import pygame
import pygame.gfxdraw
from pygame.locals import *
import math

font = 'myfont.ttf'


def angle(num):
    return math.tan(math.pi / 180 * num)


def razor_delta(direction):
    return [20 * math.cos(math.pi / 180 * direction * 60), 20 * math.sin(math.pi / 180 * direction * 60)]


def mirror_delta(direction):
    return [20 * math.cos(math.pi / 180 * direction * 30), 20 * math.sin(math.pi / 180 * direction * 30)]


colorRed = (255, 0, 0)
colorBrightRed = (222, 23, 56)
colorOrange = (220, 118, 51)
colorDarkGray = (49, 51, 53)
colorBlue = (0, 0, 255)
colorBrightBlue = ( 52, 152, 219)
colorWhite = (255, 255, 255)
colorGray = (127, 127, 127)
colorBlack = (0, 0, 0)

leftMouse = 1
rightMouse = 3

resolution = (1280, 720)
FPS = 60
clock = pygame.time.Clock()

boardPositionVertex = ((450, 50), (820, 50), (1005, 370.43), (820, 690.86), (450, 690.86), (265, 370.43), (450, 50))
boardPositionEdge = []
boardPositionAll = []
for i in range(6):
    boardPositionEdgeElement = []
    startPoint_X = boardPositionVertex[i][0]
    endPoint_X = boardPositionVertex[i + 1][0]
    startPoint_Y = boardPositionVertex[i][1]
    endPoint_Y = boardPositionVertex[i + 1][1]
    gap_X = (endPoint_X - startPoint_X) / 8
    gap_Y = (endPoint_Y - startPoint_Y) / 8
    for j in range(8):
        newEdgePoint = (startPoint_X + gap_X * j, startPoint_Y + gap_Y * j)
        boardPositionEdgeElement.append(newEdgePoint)
    boardPositionEdge.append(boardPositionEdgeElement)

boardPositionAll.append(boardPositionEdge[0])
boardPositionAll[0].append(boardPositionEdge[1][0])
correction_X = boardPositionEdge[0][0][1] / 2 - 2
correction_Y = boardPositionEdge[1][2][1] - boardPositionEdge[1][1][1]
for i in range(8):
    boardPositionAllElement = []
    startPoint_X = boardPositionEdge[5][7 - i][0]
    endPoint_X = boardPositionEdge[1][i][0]
    Point_Y = boardPositionEdge[5][7 - i][1]
    gap_X = (endPoint_X - startPoint_X + correction_X) / (i + 9)
    for j in range(i + 10):
        newEdgePoint = (startPoint_X + gap_X * j, Point_Y)
        boardPositionAllElement.append(newEdgePoint)
    boardPositionAll.append(boardPositionAllElement)
for i in range(7):
    boardPositionAllElement = []
    startPoint_X = boardPositionEdge[4][7 - i][0]
    endPoint_X = boardPositionEdge[2][i][0]
    gap_X = (endPoint_X - startPoint_X + correction_X) / (16 - i)
    Point_Y = boardPositionEdge[2][i][1]
    for j in range(16 - i):
        newEdgePoint = (startPoint_X + gap_X * j, Point_Y + correction_Y)
        boardPositionAllElement.append(newEdgePoint)
    boardPositionAll.append(boardPositionAllElement)
boardPositionAll.append(boardPositionEdge[3][:-1])
boardPositionAll[-1].append(boardPositionEdge[3][7])
boardPositionAll[-1].append(boardPositionEdge[4][0])

pygame.init()
pygame.display.set_caption("Mirror and Razor")
screen = pygame.display.set_mode(resolution)

razor = []
mirror = []

current = 'menu'
currentGame = 'razor'
currentGameSetting = 'position'

mousePos = (0, 0)
direction = 0
while True:
    leftMouseClicked = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == leftMouse:
            leftMouseClicked = True
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos

    screen.fill(colorDarkGray)

    if current == 'menu':
        if leftMouseClicked and 610 < mousePos[0] < 670 and 400 < mousePos[1] < 440:
            current = 'game'
            continue
        if leftMouseClicked and 610 < mousePos[0] < 670 and 460 < mousePos[1] < 500:
            pygame.quit()
            sys.exit()

        fontTitle = pygame.font.Font(font, 50)
        textTitle = fontTitle.render('Mirror and Razor', True, colorWhite)
        textTitleRect = textTitle.get_rect()
        textTitleRect.center = (640, 320)
        screen.blit(textTitle, textTitleRect)

        fontPlay = pygame.font.Font(font, 20)
        if 610 < mousePos[0] < 670 and 400 < mousePos[1] < 440:
            textPlay = fontPlay.render('Play', True, colorRed)
        else:
            textPlay = fontPlay.render('Play', True, colorWhite)
        textPlayRect = textPlay.get_rect()
        textPlayRect.center = (640, 420)
        screen.blit(textPlay, textPlayRect)

        fontExit = pygame.font.Font(font, 20)
        if 610 < mousePos[0] < 670 and 460 < mousePos[1] < 500:
            textExit = fontExit.render('Exit', True, colorRed)
        else:
            textExit = fontExit.render('Exit', True, colorWhite)
        textExitRect = textExit.get_rect()
        textExitRect.center = (640, 480)
        screen.blit(textExit, textExitRect)

    elif current == 'game':
        pygame.draw.aalines(screen, colorWhite, False, boardPositionVertex)
        pygame.gfxdraw.aapolygon(screen, boardPositionVertex, colorWhite)

        for i in range(3):
            pygame.draw.aaline(screen, colorGray, boardPositionEdge[i][0],
                               boardPositionEdge[i + 3][0])
        for i in range(7):
            pygame.draw.aaline(screen, colorGray, boardPositionEdge[0][i + 1], boardPositionEdge[2][7 - i])
            pygame.draw.aaline(screen, colorGray, boardPositionEdge[5][i + 1], boardPositionEdge[3][7 - i])
            pygame.draw.aaline(screen, colorGray, boardPositionEdge[1][i + 1], boardPositionEdge[5][7 - i])
            pygame.draw.aaline(screen, colorGray, boardPositionEdge[2][i + 1], boardPositionEdge[4][7 - i])
            pygame.draw.aaline(screen, colorGray, boardPositionEdge[0][i + 1], boardPositionEdge[4][7 - i])
            pygame.draw.aaline(screen, colorGray, boardPositionEdge[1][i + 1], boardPositionEdge[3][7 - i])

        if currentGameSetting == 'direction':
            if currentGame == 'mirror':
                pygame.draw.aaline(screen, colorWhite,
                                   list(map(lambda x, y: x - y, mirror[-1][0:2], mirror_delta(direction))),
                                   list(map(lambda x, y: x + y, mirror[-1][0:2], mirror_delta(direction))))
            else:
                pygame.draw.aaline(screen, colorWhite, razor[-1][0:2],
                                   list(map(lambda x, y: x + y, razor[-1][0:2], razor_delta(direction))))

        for i in boardPositionAll:
            for j in i:
                if currentGameSetting == 'position':
                    if j[0] - 5 < mousePos[0] < j[0] + 5 and j[1] - 5 < mousePos[1] < j[1] + 5:
                        if list(j) not in list(map(lambda x: x[0:2], mirror))\
                                and list(j) not in list(map(lambda x: x[0:2], razor)):
                            pygame.gfxdraw.aacircle(screen, round(j[0]), round(j[1]), 10, colorGray)

                pygame.gfxdraw.aacircle(screen, round(j[0]), round(j[1]), 2, colorWhite)
        for i in razor:
            pygame.gfxdraw.aacircle(screen, round(i[0]), round(i[1]), 12, colorOrange)
            if len(i) >= 3:
                pygame.draw.aaline(screen, colorRed, i[0:2], list(map(lambda x, y: x + y, i[0:2], razor_delta(i[2]))))
            if len(i) == 4:
                pygame.draw.aaline(screen, colorRed, i[0:2], list(map(lambda x, y: x + y, i[0:2], razor_delta(i[3]))))
        for i in mirror:
            if len(i) == 3:
                pygame.draw.aaline(screen, colorBrightBlue, list(map(lambda x, y: x - y, i[0:2], mirror_delta(i[2]))),
                                   list(map(lambda x, y: x + y, i[0:2], mirror_delta(i[2]))))

        fontOrder = pygame.font.Font(font, 30)
        if currentGame == 'razor':
            textOrder = fontOrder.render('Razor turns', True, colorWhite)
        else:
            textOrder = fontOrder.render('Mirror turns', True, colorWhite)
        textOrderRect = textOrder.get_rect()
        textOrderRect.center = (1100, 100)
        screen.blit(textOrder, textOrderRect)

        fontOrderExplanation = pygame.font.Font(font, 25)
        if currentGameSetting == 'position':
            textOrderExplanation = fontOrderExplanation.render('Choose a position.', True, colorWhite)
        else:
            textOrderExplanation = fontOrderExplanation.render('Choose a direction', True, colorWhite)
        textOrderExplanationRect = textOrderExplanation.get_rect()
        textOrderExplanationRect.center = (1110, 140)
        screen.blit(textOrderExplanation, textOrderExplanationRect)

        if currentGame == 'razor':
            if currentGameSetting == 'position':
                for i in boardPositionAll:
                    for j in i:
                        if j[0] - 5 < mousePos[0] < j[0] + 5 and j[1] - 5 < mousePos[1] < j[1] + 5:
                            if list(j) not in list(map(lambda x : x[0:2], razor)) and\
                                list(j) not in list(map(lambda x : x[0:2], mirror)) and leftMouseClicked:
                                razor.append(list(j))
                                currentGameSetting = 'direction'
            else:
                delta_X = mousePos[0] - razor[-1][0]
                delta_Y = mousePos[1] - razor[-1][1]
                if delta_X != 0:
                    inclination = delta_Y / delta_X
                else:
                    inclination = 100

                if angle(-30) < inclination < angle(30):
                    if delta_X >= 0:
                        direction = 0
                    else:
                        direction = 3
                elif angle(30) < inclination:
                    if delta_X >= 0:
                        direction = 1
                    else:
                        direction = 4
                elif angle(-30) > inclination:
                    if delta_X >= 0:
                        direction = 5
                    else:
                        direction = 2

                if leftMouseClicked:

                    if razor[-1][-1] == direction:
                        continue
                    razor[-1].append(direction)
                    if len(razor[-1]) == 4:
                        currentGame = 'mirror'
                        currentGameSetting = 'position'

        elif currentGame == 'mirror':
            if currentGameSetting == 'position':
                for i in boardPositionAll:
                    for j in i:
                        if j[0] - 5 < mousePos[0] < j[0] + 5 and j[1] - 5 < mousePos[1] < j[1] + 5:
                            if list(j) not in list(map(lambda x : x[0:2], razor)) and\
                                list(j) not in list(map(lambda x : x[0:2], mirror)) and leftMouseClicked:
                                mirror.append(list(j))
                                currentGameSetting = 'direction'
            else:
                delta_X = mousePos[0] - mirror[-1][0]
                delta_Y = mousePos[1] - mirror[-1][1]
                if delta_X != 0:
                    inclination = delta_Y / delta_X
                else:
                    inclination = 100

                if angle(-15) <= inclination < angle(15):
                    direction = 0
                elif angle(15) <= inclination < angle(45):
                    direction = 1
                elif angle(45) <= inclination < angle(75):
                    direction = 2
                elif angle(75) <= inclination or angle(-75) >= inclination:
                    direction = 3
                elif angle(-75) <= inclination < angle(-45):
                    direction = 4
                else:
                    direction = 5

                if leftMouseClicked:
                    mirror[-1].append(direction)
                    currentGame = 'razor'
                    currentGameSetting = 'position'

    pygame.display.flip()
    clock.tick(FPS)
