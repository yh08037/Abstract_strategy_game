import sys
import pygame
import pygame.gfxdraw
from pygame.locals import *
import math

def angle(num):
    return math.tan(math.pi / 180 * num)


def razor_delta(direction, tale=0):
    if tale == 0:
        return [20 * math.cos(math.pi / 180 * direction * 60), 20 * math.sin(math.pi / 180 * direction * 60)]
    else:
        return [-6 * math.cos(math.pi / 180 * (direction * 60 + tale * 30)), -6 * math.sin(math.pi / 180 * (direction * 60 + tale * 30))]


def mirror_delta(direction):
    return [20 * math.cos(math.pi / 180 * direction * 30), 20 * math.sin(math.pi / 180 * direction * 30)]


def razor_direction(board, x, y, direction):
    if x < 8:
        if direction == 0:
            if len(board[x]) == y + 1:
                return board
            if board[x][y+1][0] == '-':
                board = razor_direction(board, x, y+1, direction)
            elif board[x][y+1][0] == 'M':
                if board[x][y+1][1] == 3:
                    return board
                else:
                    direction = board[x][y+1][1]
                    board = razor_direction(board, x, y+1, direction)
            elif board[x][y+1][0] == 'R':
                if 3 in board[x][y+1][1:3]:
                    return board
                else:
                    board[x][y+1].append('B')
                    board = razor_direction(board, x, y + 1, direction)

        elif direction == 1:
            if len(board[x]) == y + 1 or len(board) == x + 1:
                return board
            if board[x+1][y+1][0] == '-':
                board = razor_direction(board, x+1, y+1, direction)
            elif board[x+1][y+1][0] == 'M':
                if board[x+1][y+1][1] == 5:
                    return board
                else:
                    direction = (board[x+1][y+1][1] + 5) % 6
                    board = razor_direction(board, x+1, y+1, direction)
            elif board[x+1][y+1][0] == 'R':
                if 4 in board[x+1][y+1][1:3]:
                    return board
                else:
                    board[x+1][y+1].append('B')
                    board = razor_direction(board, x+1, y + 1, direction)

        elif direction == 2:
            if len(board) == x + 1:
                return board
            if board[x+1][y][0] == '-':
                board = razor_direction(board, x+1, y, direction)
            elif board[x+1][y][0] == 'M':
                if board[x+1][y][1] == 1:
                    return board
                else:
                    direction = (board[x+1][y][1] + 4) % 6
                    board = razor_direction(board, x+1, y, direction)
            elif board[x+1][y][0] == 'R':
                if 5 in board[x+1][y][1:3]:
                    return board
                else:
                    board[x+1][y].append('B')
                    board = razor_direction(board, x+1, y, direction)

        elif direction == 3:
            if y == 0:
                return board
            if board[x][y-1][0] == '-':
                board = razor_direction(board, x, y-1, direction)
            elif board[x][y-1][0] == 'M':
                if board[x][y-1][1] == 3:
                    return board
                else:
                    direction = (board[x][y-1][1] + 3) % 6
                    board = razor_direction(board, x, y - 1, direction)
            elif board[x][y - 1][0] == 'R':
                if 0 in board[x][y - 1][1:3]:
                    return board
                else:
                    board[x][y - 1].append('B')
                    board = razor_direction(board, x, y - 1, direction)

        elif direction == 4:
            if x == 0 or y == 0:
                return board
            if board[x-1][y-1][0] == '-':
                board = razor_direction(board, x-1, y-1, direction)
            elif board[x-1][y-1][0] == 'M':
                if board[x-1][y-1][1] == 5:
                    return board
                else:
                    direction = (board[x-1][y-1][1] + 2) % 6
                    board = razor_direction(board, x-1, y - 1, direction)
            elif board[x-1][y-1][0] == 'R':
                if 1 in board[x-1][y-1][1:3]:
                    return board
                else:
                    board[x-1][y - 1].append('B')
                    board = razor_direction(board, x-1, y - 1, direction)

        elif direction == 5:
            if x == 0 or len(board[x-1]) == y:
                return board
            if board[x-1][y][0] == '-':
                board = razor_direction(board, x-1, y, direction)
            elif board[x-1][y][0] == 'M':
                if board[x-1][y][1] == 1:
                    return board
                else:
                    direction = (board[x-1][y][1] + 1) % 6
                    board = razor_direction(board, x-1, y, direction)
            elif board[x-1][y][0] == 'R':
                if 2 in board[x-1][y][1:3]:
                    return board
                else:
                    board[x-1][y].append('B')
                    board = razor_direction(board, x-1, y, direction)

    elif x == 8:
        if direction == 0:
            if len(board[x]) == y + 1:
                return board
            if board[x][y + 1][0] == '-':
                board = razor_direction(board, x, y + 1, direction)
            elif board[x][y + 1][0] == 'M':
                if board[x][y + 1][1] == 3:
                    return board
                else:
                    direction = board[x][y + 1][1]
                    board = razor_direction(board, x, y + 1, direction)
            elif board[x][y + 1][0] == 'R':
                if 3 in board[x][y + 1][1:3]:
                    return board
                else:
                    board[x][y + 1].append('B')
                    board = razor_direction(board, x, y + 1, direction)

        elif direction == 1:
            if len(board) == x + 1 or len(board[x+1]) == y:
                return board
            if board[x + 1][y][0] == '-':
                board = razor_direction(board, x + 1, y, direction)
            elif board[x + 1][y][0] == 'M':
                if board[x + 1][y][1] == 5:
                    return board
                else:
                    direction = (board[x + 1][y][1] + 5) % 6
                    board = razor_direction(board, x + 1, y, direction)
            elif board[x + 1][y][0] == 'R':
                if 4 in board[x + 1][y][1:3]:
                    return board
                else:
                    board[x + 1][y].append('B')
                    board = razor_direction(board, x + 1, y, direction)

        elif direction == 2:
            if len(board) == x + 1 or y == 0:
                return board
            if board[x + 1][y - 1][0] == '-':
                board = razor_direction(board, x + 1, y - 1, direction)
            elif board[x + 1][y - 1][0] == 'M':
                if board[x + 1][y - 1][1] == 1:
                    return board
                else:
                    direction = (board[x + 1][y - 1][1] + 4) % 6
                    board = razor_direction(board, x + 1, y - 1, direction)
            elif board[x + 1][y - 1][0] == 'R':
                if 5 in board[x + 1][y - 1][1:3]:
                    return board
                else:
                    board[x + 1][y - 1].append('B')
                    board = razor_direction(board, x + 1, y - 1, direction)

        elif direction == 3:
            if y == 0:
                return board
            if board[x][y - 1][0] == '-':
                board = razor_direction(board, x, y - 1, direction)
            elif board[x][y - 1][0] == 'M':
                if board[x][y - 1][1] == 3:
                    return board
                else:
                    direction = (board[x][y - 1][1] + 3) % 6
                    board = razor_direction(board, x, y - 1, direction)
            elif board[x][y - 1][0] == 'R':
                if 0 in board[x][y - 1][1:3]:
                    return board
                else:
                    board[x][y - 1].append('B')
                    board = razor_direction(board, x, y - 1, direction)

        elif direction == 4:
            if x == 0 or y == 0:
                return board
            if board[x - 1][y-1][0] == '-':
                board = razor_direction(board, x - 1, y-1, direction)
            elif board[x - 1][y-1][0] == 'M':
                if board[x - 1][y-1][1] == 5:
                    return board
                else:
                    direction = (board[x - 1][y-1][1] + 2) % 6
                    board = razor_direction(board, x - 1, y-1, direction)
            elif board[x - 1][y-1][0] == 'R':
                if 1 in board[x-1][y-1][1:3]:
                    return board
                else:
                    board[x - 1][y-1].append('B')
                    board = razor_direction(board, x - 1, y-1, direction)

        elif direction == 5:
            if x == 0 or len(board[x-1]) == y:
                return board
            if board[x - 1][y][0] == '-':
                board = razor_direction(board, x - 1, y, direction)
            elif board[x - 1][y][0] == 'M':
                if board[x - 1][y][1] == 1:
                    return board
                else:
                    direction = (board[x - 1][y][1] + 1) % 6
                    board = razor_direction(board, x - 1, y, direction)
            elif board[x - 1][y][0] == 'R':
                if 2 in board[x-1][y][1:3]:
                    return board
                else:
                    board[x - 1][y].append('B')
                    board = razor_direction(board, x - 1, y, direction)

    elif x > 8:
        if direction == 0:
            if len(board[x]) == y + 1:
                return board
            if board[x][y + 1][0] == '-':
                board = razor_direction(board, x, y + 1, direction)
            elif board[x][y + 1][0] == 'M':
                if board[x][y + 1][1] == 3:
                    return board
                else:
                    direction = board[x][y + 1][1]
                    board = razor_direction(board, x, y + 1, direction)
            elif board[x][y + 1][0] == 'R':
                if 3 in board[x][y + 1][1:3]:
                    return board
                else:
                    board[x][y + 1].append('B')
                    board = razor_direction(board, x, y + 1, direction)

        elif direction == 1:
            if len(board) == x + 1 or len(board[x+1]) == y:
                return board
            if board[x + 1][y][0] == '-':
                board = razor_direction(board, x + 1, y, direction)
            elif board[x + 1][y][0] == 'M':
                if board[x + 1][y][1] == 5:
                    return board
                else:
                    direction = (board[x + 1][y][1] + 5) % 6
                    board = razor_direction(board, x + 1, y, direction)
            elif board[x + 1][y][0] == 'R':
                if 4 in board[x + 1][y][1:3]:
                    return board
                else:
                    board[x + 1][y].append('B')
                    board = razor_direction(board, x + 1, y, direction)

        elif direction == 2:
            if len(board) == x + 1 or y == 0:
                return board
            if board[x + 1][y - 1][0] == '-':
                board = razor_direction(board, x + 1, y -1, direction)
            elif board[x + 1][y-1][0] == 'M':
                if board[x + 1][y-1][1] == 1:
                    return board
                else:
                    direction = (board[x + 1][y-1][1] + 4) % 6
                    board = razor_direction(board, x + 1, y-1, direction)
            elif board[x + 1][y-1][0] == 'R':
                if 5 in board[x + 1][y-1][1:3]:
                    return board
                else:
                    board[x + 1][y-1].append('B')
                    board = razor_direction(board, x+1, y - 1, direction)

        elif direction == 3:
            if y == 0:
                return board
            if board[x][y - 1][0] == '-':
                board = razor_direction(board, x, y - 1, direction)
            elif board[x][y - 1][0] == 'M':
                if board[x][y - 1][1] == 3:
                    return board
                else:
                    direction = (board[x][y - 1][1] + 3) % 6
                    board = razor_direction(board, x, y - 1, direction)
            elif board[x][y - 1][0] == 'R':
                if 0 in board[x][y - 1][1:3]:
                    return board
                else:
                    board[x][y - 1].append('B')
                    board = razor_direction(board, x, y - 1, direction)

        elif direction == 4:
            if x == 0:
                return board
            if board[x - 1][y][0] == '-':
                board = razor_direction(board, x - 1, y, direction)
            elif board[x - 1][y][0] == 'M':
                if board[x - 1][y][1] == 5:
                    return board
                else:
                    direction = (board[x - 1][y][1] + 2) % 6
                    board = razor_direction(board, x - 1, y, direction)
            elif board[x - 1][y][0] == 'R':
                if 1 in board[x-1][y][1:3]:
                    return board
                else:
                    board[x - 1][y].append('B')
                    board = razor_direction(board, x-1, y, direction)

        elif direction == 5:
            if x == 0 or len(board[x]) == y + 1:
                return board
            if board[x - 1][y+1][0] == '-':
                board = razor_direction(board, x - 1, y+1, direction)
            elif board[x - 1][y+1][0] == 'M':
                if board[x - 1][y+1][1] == 1:
                    return board
                else:
                    direction = (board[x - 1][y+1][1] + 1) % 6
                    board = razor_direction(board, x - 1, y+1, direction)
            elif board[x - 1][y+1][0] == 'R':
                if 2 in board[x-1][y+1][1:3]:
                    return board
                else:
                    board[x - 1][y+1].append('B')
                    board = razor_direction(board, x - 1, y + 1, direction)

    return board


def Is_it_burnt(razor, mirror, boardPositionAll):
    board = []
    for i in range(9):
        board_element = []
        for j in range(i + 9):
            for k in range(len(razor)):
                if razor[k][0] == boardPositionAll[i][j][0] and razor[k][1] == boardPositionAll[i][j][1]:
                    board_element.append(['R', razor[k][2], razor[k][3]])
                    break
            else:
                for k in range(len(mirror)):
                    if mirror[k][0] == boardPositionAll[i][j][0] and mirror[k][1] == boardPositionAll[i][j][1]:
                        board_element.append(['M', mirror[k][2]])
                        break
                else:
                    board_element.append(['-'])
        board.append(board_element)

    for i in range(9, 17):
        board_element = []
        for j in range(25 - i):
            for k in range(len(razor)):
                if razor[k][0] == boardPositionAll[i][j][0] and razor[k][1] == boardPositionAll[i][j][1]:
                    board_element.append(['R', razor[k][2], razor[k][3]])
                    break
            else:
                for k in range(len(mirror)):
                    if mirror[k][0] == boardPositionAll[i][j][0] and mirror[k][1] == boardPositionAll[i][j][1]:
                        board_element.append(['M', mirror[k][2]])
                        break
                else:
                    board_element.append(['-'])
        board.append(board_element)
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y][0] == 'R':
                for k in range(1, 3):
                    board = razor_direction(board, x, y, board[x][y][k])

    for i in range(len(razor)):
        razor[i] = razor[i][0:4]

    burntRazorElement = []
    for i in range(9):
        for j in range(i + 9):
            for k in range(len(razor)):
                if razor[k][0] == boardPositionAll[i][j][0] and razor[k][1] == boardPositionAll[i][j][1]:
                    if len(board[i][j]) >= 4:
                        burntRazorElement.append([i, j])
    for i in range(9, 17):
        for j in range(25 - i):
            for k in range(len(razor)):
                if razor[k][0] == boardPositionAll[i][j][0] and razor[k][1] == boardPositionAll[i][j][1]:
                    if len(board[i][j]) == 4:
                        burntRazorElement.append([i, j])
    burntRazor.append(burntRazorElement)

    for i in range(9):
        for j in range(i + 9):
            for k in range(len(razor)):
                if razor[k][0] == boardPositionAll[i][j][0] and razor[k][1] == boardPositionAll[i][j][1]:
                    for l in range(len(burntRazor)):
                        if [i, j] in burntRazor[l]:
                            razor[k].append(1)
                            break
    for i in range(9, 17):
        for j in range(25 - i):
            for k in range(len(razor)):
                if razor[k][0] == boardPositionAll[i][j][0] and razor[k][1] == boardPositionAll[i][j][1]:
                    for l in range(len(burntRazor)):
                        if [i, j] in burntRazor[l]:
                            razor[k].append(1)
                            break

    burnt = 0
    for i in razor:
        if len(i) == 5:
           burnt += 1
    notBurnt = len(razor) - burnt
    print(razor, burntRazor)
    return razor, burnt, notBurnt, burntRazor


font = 'myfont.ttf'

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

boardPositionVertex = ((450, 50), (820, 50), (1005, 370.43), (820, 690.86), (450, 690.86), (265, 370.43), (450, 50))
boardPositionEdge = []
boardPositionAll = []
for i in range(6):
    boardPositionEdgeElement = []
    startPoint_X = boardPositionVertex[i][0]
    endPoint_X = boardPositionVertex[i + 1][0]
    gap_X = (endPoint_X - startPoint_X) / 8
    startPoint_Y = boardPositionVertex[i][1]
    endPoint_Y = boardPositionVertex[i + 1][1]
    gap_Y = (endPoint_Y - startPoint_Y) / 8
    for j in range(8):
        newEdgePoint = (round(startPoint_X + gap_X * j, 1), round(startPoint_Y + gap_Y * j, 1))
        boardPositionEdgeElement.append(newEdgePoint)
    boardPositionEdge.append(boardPositionEdgeElement)

boardPositionAll.append(boardPositionEdge[0])
boardPositionAll[0].append(boardPositionEdge[1][0])
for i in range(8):
    boardPositionAllElement = []
    startPoint_X = boardPositionEdge[5][7 - i][0]
    endPoint_X = boardPositionEdge[1][i][0]
    gap_X = (endPoint_X - startPoint_X) / (i + 8.5)
    Point_Y = boardPositionEdge[5][7 - i][1]
    for j in range(i + 10):
        newEdgePoint = (round(startPoint_X + gap_X * j, 1), round(Point_Y, 1))
        boardPositionAllElement.append(newEdgePoint)
    boardPositionAll.append(boardPositionAllElement)
for i in range(7):
    boardPositionAllElement = []
    startPoint_X = boardPositionEdge[4][7 - i][0]
    endPoint_X = boardPositionEdge[2][i][0]
    gap_X = (endPoint_X - startPoint_X) / (15.5 - i)
    Point_Y = boardPositionEdge[2][i][1] + boardPositionEdge[2][3][1] - boardPositionEdge[2][2][1]
    for j in range(16 - i):
        newEdgePoint = (round(startPoint_X + gap_X * j, 1), round(Point_Y, 1))
        boardPositionAllElement.append(newEdgePoint)
    boardPositionAll.append(boardPositionAllElement)
boardPositionAll.append(boardPositionEdge[3][:-1])
boardPositionAll[-1].append(boardPositionEdge[3][7])
boardPositionAll[-1].append(boardPositionEdge[4][0])
boardPositionAll[-1].reverse()

pygame.init()
pygame.display.set_caption("Mirror and Razor")
screen = pygame.display.set_mode(resolution)

razor = []
mirror = []
burntRazor = []

current = 'menu'
currentGame = 'razor'
currentGameSetting = 'position'

mousePos = (0, 0)
direction = 0
burnt = 0
notBurnt = 0

turn = 1

while True:
    leftMouseClicked = False
    escClicked = False
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

    screen.fill(colorDarkGray)

    if escClicked:
        if current == 'game':
            if len(razor) == 0:
                continue
            if currentGame == 'mirror' and currentGameSetting == 'position':
                del razor[-1]
                currentGame = 'razor'
            elif currentGame == 'mirror' and currentGameSetting == 'direction':
                del mirror[-1]
                currentGameSetting = 'position'
            elif currentGame == 'razor' and currentGameSetting == 'position':
                del mirror[-1]
                currentGame = 'mirror'
            elif currentGame == 'razor' and currentGameSetting == 'direction':
                del razor[-1]
                currentGameSetting = 'position'
            del burntRazor[-1], burntRazor[-1]

            razor, burnt, notBurnt, burntRazor = Is_it_burnt(razor, mirror, boardPositionAll)



    if current == 'menu':

        if leftMouseClicked and 610 < mousePos[0] < 670 and 400 < mousePos[1] < 440:
            current = 'game'
            continue

        if leftMouseClicked and 610 < mousePos[0] < 670 and 460 < mousePos[1] < 500:
            openFile = input("Enter to open file. ") + '.txt'
            openData = open(openFile, 'r')
            while True:
                mirrorData = openData.readline().rstrip('\n')
                if mirrorData == '-':
                    break
                mirror.append(list(map(lambda data: float(data.strip("'' ")), list(map(str, mirrorData.strip("[]").split(','))))))
            while True:
                razorData = openData.readline().rstrip('\n')
                if razorData == '-':
                    break
                razor.append(list(map(lambda data: float(data.strip("'' ")), list(map(str, razorData.strip("[]").split(','))))))
            while True:
                burntRazorData = openData.readline().rstrip('\n')
                if burntRazorData == '':
                    break
                burntRazor.append(list(map(lambda data: float(data.strip("'' ")), list(map(str, burntRazorData.strip("[]").split(','))))))
            openData.close()
            razor, burnt, notBurnt, burntRazor = Is_it_burnt(razor, mirror, boardPositionAll)
            current = 'game'
            if len(mirror) == len(razor):
                currentGame = 'razor'
                if len(razor) > 0:
                    if len(razor[-1]) <= 3:
                        currentGameSetting = 'direction'
            else:
                currentGame = 'mirror'
                if len(mirror) > 0:
                    if len(mirror[-1]) <= 2:
                        currentGameSetting = 'direction'
            print('opened')
            continue

        if leftMouseClicked and 610 < mousePos[0] < 670 and 520 < mousePos[1] < 560:
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

        fontOpen = pygame.font.Font(font, 20)
        if 610 < mousePos[0] < 670 and 460 < mousePos[1] < 500:
            textOpen = fontOpen.render('Open', True, colorRed)
        else:
            textOpen = fontOpen.render('Open', True, colorWhite)
        textOpenRect = textOpen.get_rect()
        textOpenRect.center = (640, 480)
        screen.blit(textOpen, textOpenRect)

        fontExit = pygame.font.Font(font, 20)
        if 610 < mousePos[0] < 670 and 520 < mousePos[1] < 560:
            textExit = fontExit.render('Exit', True, colorRed)
        else:
            textExit = fontExit.render('Exit', True, colorWhite)
        textExitRect = textExit.get_rect()
        textExitRect.center = (640, 540)
        screen.blit(textExit, textExitRect)
        pygame.display.flip()

    elif current == 'game':
        pygame.draw.aalines(screen, colorWhite, False, boardPositionVertex)
        pygame.gfxdraw.aapolygon(screen, boardPositionVertex, colorWhite)

        for i in range(3):
            pygame.draw.aaline(screen, colorLightGray, boardPositionEdge[i][0],
                               boardPositionEdge[i + 3][0])
        for i in range(7):
            pygame.draw.aaline(screen, colorLightGray, boardPositionEdge[0][i + 1], boardPositionEdge[2][7 - i])
            pygame.draw.aaline(screen, colorLightGray, boardPositionEdge[5][i + 1], boardPositionEdge[3][7 - i])
            pygame.draw.aaline(screen, colorLightGray, boardPositionEdge[1][i + 1], boardPositionEdge[5][7 - i])
            pygame.draw.aaline(screen, colorLightGray, boardPositionEdge[2][i + 1], boardPositionEdge[4][7 - i])
            pygame.draw.aaline(screen, colorLightGray, boardPositionEdge[0][i + 1], boardPositionEdge[4][7 - i])
            pygame.draw.aaline(screen, colorLightGray, boardPositionEdge[1][i + 1], boardPositionEdge[3][7 - i])

        if currentGameSetting == 'direction':
            if currentGame == 'mirror':
                pygame.draw.aaline(screen, colorWhite,
                                   list(map(lambda x, y: x - y, mirror[-1][0:2], mirror_delta(direction))),
                                   list(map(lambda x, y: x + y, mirror[-1][0:2], mirror_delta(direction))))
            elif currentGame == 'razor':
                for i in range(6):
                    if tuple(razor[-1][0:2]) in boardPositionEdge[i]:
                        if direction == (i+4) % 6 or direction == (i+5) % 6:
                            break
                        if tuple(razor[-1][0:2]) == boardPositionEdge[i][0]:
                            if direction == (i+3) % 6:
                                break
                else:
                    pygame.draw.aaline(screen, colorWhite, razor[-1][0:2], list(map(lambda x, y: x + y, razor[-1][0:2], razor_delta(direction))))


        for i in boardPositionAll:
            for j in i:
                if currentGameSetting == 'position':
                    if j[0] - 10 < mousePos[0] < j[0] + 10 and j[1] - 10 < mousePos[1] < j[1] + 10:
                        if list(j) not in list(map(lambda x: x[0:2], mirror)) \
                                and list(j) not in list(map(lambda x: x[0:2], razor)):
                            pygame.gfxdraw.aacircle(screen, round(j[0]), round(j[1]), 10, colorGray)

                pygame.gfxdraw.aacircle(screen, round(j[0]), round(j[1]), 2, colorWhite)
        for i in razor:
            if len(i) == 5:
                pygame.draw.circle(screen, colorOrange, (round(i[0]), round(i[1])), 11)

            else:
                pygame.gfxdraw.aacircle(screen, round(i[0]), round(i[1]), 11, colorOrange)
            if len(i) >= 3:
                arrow = list(map(lambda x, y: x + y, i[0:2], razor_delta(i[2])))
                arrowTale1 = list(map(lambda x, y: x+y, arrow, razor_delta(i[2], 1)))
                arrowTale2 = list(map(lambda x, y: x+y, arrow, razor_delta(i[2], -1)))
                pygame.draw.aaline(screen, colorOrange, i[0:2], arrow)
                pygame.draw.aaline(screen, colorOrange, arrow, arrowTale1)
                pygame.draw.aaline(screen, colorOrange, arrow, arrowTale2)
            if len(i) >= 4:
                arrow = list(map(lambda x, y: x + y, i[0:2], razor_delta(i[3])))
                arrowTale1 = list(map(lambda x, y: x+y, arrow, razor_delta(i[3], 1)))
                arrowTale2 = list(map(lambda x, y: x+y, arrow, razor_delta(i[3], -1)))
                pygame.draw.aaline(screen, colorOrange, i[0:2], arrow)
                pygame.draw.aaline(screen, colorOrange, arrow, arrowTale1)
                pygame.draw.aaline(screen, colorOrange, arrow, arrowTale2)
        for i in mirror:
            if len(i) == 3:
                pygame.draw.aaline(screen, colorBrightBlue, list(map(lambda x, y: x - y, i[0:2], mirror_delta(i[2]))),
                                   list(map(lambda x, y: x + y, i[0:2], mirror_delta(i[2]))))

        fontOrder = pygame.font.Font(font, 30)
        if currentGame == 'razor':
            textOrder = fontOrder.render('Razor turns', True, colorWhite)
        elif currentGame == 'mirror':
            textOrder = fontOrder.render('Mirror turns', True, colorWhite)
        textOrderRect = textOrder.get_rect()
        textOrderRect.center = (1100, 100)
        screen.blit(textOrder, textOrderRect)

        fontOrderExplanation = pygame.font.Font(font, 25)
        if currentGameSetting == 'position':
            textOrderExplanation = fontOrderExplanation.render('Choose a position.', True, colorWhite)
        elif currentGameSetting == 'direction':
            textOrderExplanation = fontOrderExplanation.render('Choose a direction', True, colorWhite)
        textOrderExplanationRect = textOrderExplanation.get_rect()
        textOrderExplanationRect.center = (1100, 140)
        screen.blit(textOrderExplanation, textOrderExplanationRect)

        fontIsBurntExplanation = pygame.font.Font(font, 16)
        textBurntExplanation = fontIsBurntExplanation.render('Burnt : ' + str(burnt), True, colorWhite)
        textBurntExplanationRect = textBurntExplanation.get_rect()
        textBurntExplanationRect.center = (1100, 170)
        screen.blit(textBurntExplanation, textBurntExplanationRect)
        textNotBurntExplanation = fontIsBurntExplanation.render('Not Burnt : ' + str(notBurnt), True, colorWhite)
        textNotBurntExplanationRect = textNotBurntExplanation.get_rect()
        textNotBurntExplanationRect.center = (1100, 190)
        screen.blit(textNotBurntExplanation, textNotBurntExplanationRect)

        if burnt == 20:
            fontMirrorWin = pygame.font.Font(font, 50)
            textMirrorWin = fontMirrorWin.render('Mirror Wins!', True, colorWhite)
            textMirrorWinRect = textMirrorWin.get_rect()
            textMirrorWinRect.center = (640, 320)
            screen.blit(textMirrorWin, textMirrorWinRect)
        elif notBurnt == 20:
            fontRazorWin = pygame.font.Font(font, 50)
            textRazorWin = fontRazorWin.render('Razor Wins!', True, colorWhite)
            textRazorWinRect = textRazorWin.get_rect()
            textRazorWinRect.center = (640, 320)
            screen.blit(textRazorWin, textRazorWinRect)


        if currentGame == 'razor':
            if currentGameSetting == 'position':
                for i in boardPositionAll:
                    for j in i:
                        if j[0] - 10 < mousePos[0] < j[0] + 10 and j[1] - 10 < mousePos[1] < j[1] + 10:
                            if list(j) not in list(map(lambda x: x[0:2], razor)) and \
                                    list(j) not in list(map(lambda x: x[0:2], mirror)) and leftMouseClicked:
                                razor.append(list(j))
                                currentGameSetting = 'direction'
            elif currentGameSetting == 'direction':
                delta_X = mousePos[0] - razor[-1][0]
                delta_Y = mousePos[1] - razor[-1][1]
                if delta_X != 0:
                    inclination = delta_Y / delta_X
                else:
                    inclination = 100

                if angle(-30) < inclination < angle(30):
                    if delta_X >= 0:
                        direction = 0
                    elif delta_X < 0:
                        direction = 3
                elif angle(30) < inclination:
                    if delta_X >= 0:
                        direction = 1
                    elif delta_X < 0:
                        direction = 4
                elif angle(-30) > inclination:
                    if delta_X >= 0:
                        direction = 5
                    elif delta_X < 0:
                        direction = 2

                if leftMouseClicked:
                    if razor[-1][-1] == direction:
                        continue
                    for i in range(6):
                        if tuple(razor[-1][0:2]) in boardPositionEdge[i]:
                            if direction == (i+4) % 6 or direction == (i+5) % 6:
                                break
                            if tuple(razor[-1][0:2]) == boardPositionEdge[i][0]:
                                if direction == (i+3) % 6:
                                    break
                    else:
                        razor[-1].append(direction)
                        if len(razor[-1]) == 4:
                            currentGame = 'mirror'
                            currentGameSetting = 'position'
                            razor, burnt, notBurnt, burntRazor = Is_it_burnt(razor, mirror, boardPositionAll)

        elif currentGame == 'mirror':
            if currentGameSetting == 'position':
                for i in boardPositionAll:
                    for j in i:
                        if j[0] - 10 < mousePos[0] < j[0] + 10 and j[1] - 10 < mousePos[1] < j[1] + 10:
                            if list(j) not in list(map(lambda x: x[0:2], razor)) and \
                                    list(j) not in list(map(lambda x: x[0:2], mirror)) and leftMouseClicked:
                                mirror.append(list(j))
                                currentGameSetting = 'direction'
            elif currentGameSetting == 'direction':
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
                elif angle(-45) <= inclination < angle(-15):
                    direction = 5

                if leftMouseClicked:
                    mirror[-1].append(direction)
                    currentGame = 'razor'
                    currentGameSetting = 'position'
                    razor, burnt, notBurnt, burntRazor = Is_it_burnt(razor, mirror, boardPositionAll)

        fontSave = pygame.font.Font(font, 20)
        if 1080 < mousePos[0] < 1120 and 580 < mousePos[1] < 620:
            textSave = fontSave.render('Save', True, colorRed)
        else:
            textSave = fontSave.render('Save', True, colorWhite)
        textSaveRect = textSave.get_rect()
        textSaveRect.center = (1100, 600)
        screen.blit(textSave, textSaveRect)

        pygame.display.flip()

        if 1080 < mousePos[0] < 1120 and 580 < mousePos[1] < 620 and leftMouseClicked:
            saveFile = input("Name to save : ") + '.txt'
            saveData = open(saveFile, 'w')
            for i in range(len(mirror)):
                saveData.write(str(mirror[i]) + '\n')
            saveData.write('-\n')
            for i in range(len(razor)):
                saveData.write(str(razor[i]) + '\n')
            saveData.write('-\n')
            for i in range(len(burntRazor)):
                saveData.write(str(burntRazor[i]) + '\n')
            saveData.close()
            print('Saved')

    clock.tick(FPS)
