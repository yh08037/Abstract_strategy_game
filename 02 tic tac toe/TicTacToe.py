import pygame
from pygame.locals import *
import sys

#RGB 포맷으로 색 정의
BLACK = (0,   0,   0  )
WHITE = (255, 255, 255)

#게임 엔진 초기화
pygame.init()

#화면 높이와 폭 설정
size   = [1280, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.SysFont("consolas", 50)

#3X3 게임 판의 꼭짓점 좌표 리스트
boardPos = [[(340, 60), (540, 60), (740, 60), (940, 60)],
            [(340, 260), (540, 260), (740, 260), (940, 260)],
            [(340, 460), (540, 460), (740, 460), (940, 460)],
            [(340, 660), (540, 660), (740, 660), (940, 660)]]


done  = False
FPS   = 10
leftMouse = 1
rightMouse = 3
clock = pygame.time.Clock()

current = 'menu'
gameOver = False

X_placed = []
O_placed = []
Is_turn_X = True
X_win = False
O_win = False


# 마우스 위치 지정 함수
def Is_mousePos_in_boardPos(mousePos, boardPoint):
    Check_boardPointX = boardPoint[0] < mousePos[0] < boardPoint[0] + 200
    Check_boardPointY = boardPoint[1] < mousePos[1] < boardPoint[1] + 200
    if Check_boardPointX and Check_boardPointY :
        return True
    return False

# X자 모양 그리는 함수
def draw_X(boardPoint):
    x, y = boardPoint[0]+100, boardPoint[1]+100
    rect1 = [(x+80, y+70), (x+70, y+80), (x-80, y-70), (x-70, y-80)]
    rect2 = [(x+80, y-70), (x+70, y-80), (x-80, y+70), (x-70, y+80)]
    pygame.draw.polygon(screen, BLACK, rect1)
    pygame.draw.polygon(screen, BLACK, rect2)

# printText 함수
def printText(msg, color='BLACK', pos=(180, 150)):
    textSurface = font.render(msg, True, pygame.Color(color), None)
    textRect = textSurface.get_rect()
    textRect.center = pos

    screen.blit(textSurface, textRect)

# X 또는 O의 삼목 여부를 확인하는 함수
def Is_three_in_a_row(boardPos, placedPos):
    onBoard = []
    for i in range(3):
        for j in range(3):
            if boardPos[i][j] in placedPos:
                onBoard.append(True)
            else:
                onBoard.append(False)
    if onBoard[0] and onBoard[1] and onBoard[2]:
        return True
    elif onBoard[3] and onBoard[4] and onBoard[5]:
        return True
    elif onBoard[6] and onBoard[7] and onBoard[8]:
        return True
    elif onBoard[0] and onBoard[3] and onBoard[6]:
        return True
    elif onBoard[1] and onBoard[4] and onBoard[7]:
        return True
    elif onBoard[2] and onBoard[5] and onBoard[8]:
        return True
    elif onBoard[0] and onBoard[4] and onBoard[8]:
        return True
    elif onBoard[2] and onBoard[4] and onBoard[6]:
        return True
    else:
        return False

# 게임 진행과 관련된 모든 변수를 초기화하는 함수
def InitializeVariance():
    global gameOver
    global X_placed
    global O_placed
    global Is_turn_X
    global X_win
    global O_win

    gameOver = False
    X_placed = []
    O_placed = []
    Is_turn_X = True
    X_win = False
    O_win = False



while True:

    clock.tick(FPS)

    leftMouseClicked = False

    # 메인 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == leftMouse:
            leftMouseClicked = True
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos

    screen.fill(WHITE)


    # 게임 시작 전 메인 메뉴 화면
    if current == 'menu':
        printText("Tic Tac Toe", 'BLACK', (640, 200))
        printText("start", 'BLACK', (640, 400))
        printText("quit", 'BLACK', (640, 500))

        # 게임 시작 또는 나기기 버튼 클릭 여부 확인
        if leftMouseClicked:
            if 540 < mousePos[0] < 740 and 380 < mousePos[1] < 420:
                current = 'game'
            elif 540 < mousePos[0] < 740 and 480 < mousePos[1] < 520:
                pygame.quit()
                sys.exit()

    # 게임 진행 중 화면
    elif current == 'game':

        # 가로세로줄 그리기
        for i in range(0, 4):
            pygame.draw.line(screen, BLACK, boardPos[0][i], boardPos[3][i], 5)
            pygame.draw.line(screen, BLACK, boardPos[i][0], boardPos[i][3], 5)


        # 게임이 끝나지 않았을 때 마우스 클릭 정보 저장하기
        if not gameOver:
            IsBreak = False
            for x in range(3):
                for y in range(3):
                    if leftMouseClicked and Is_mousePos_in_boardPos(mousePos, boardPos[x][y]):
                        Is_it_Placed = boardPos[x][y] in X_placed or boardPos[x][y] in O_placed
                        if Is_turn_X and not Is_it_Placed:
                            X_placed.append(boardPos[x][y])
                            if Is_three_in_a_row(boardPos, X_placed):
                                X_win = True
                                gameOver = True
                            Is_turn_X = False
                        elif not Is_turn_X and not Is_it_Placed:
                            O_placed.append(boardPos[x][y])
                            if Is_three_in_a_row(boardPos, O_placed):
                                O_win = True
                                gameOver = True
                            Is_turn_X = True
                        IsBreak = True
                        break
                if IsBreak:
                    break

        elif gameOver:
            # 승패 여부 출력하기
            if X_win:
                printText("X win!", 'BLACK', (180, 400))
            elif O_win:
                printText("O win!", 'BLACK', (180, 400))


            # 다시 시작 또는 끝내기 출력
            printText("Restart", 'BLACK', (1100, 300))
            printText("Main", 'BLACK', (1100, 400))
            printText("Quit", 'BLACK', (1100, 500))


            # 다시 시작 또는 나가기 버튼 클릭 확인
            if leftMouseClicked:
                if 1000 < mousePos[0] < 1200 and 280 < mousePos[1] < 320:
                    InitializeVariance()
                elif 1000 < mousePos[0] < 1200 and 380 < mousePos[1] < 420:
                    current = 'menu'
                    InitializeVariance()
                elif 1000 < mousePos[0] < 1200 and 480 < mousePos[1] < 520:
                    pygame.quit()
                    sys.exit()



        # O, X 그리기
        for point in X_placed:
            draw_X(point)
        for point in O_placed:
            pygame.draw.circle(screen, BLACK, (point[0]+100, point[1]+100), 80, 13)


        # 차례 나타내기
        if Is_turn_X:
            printText("X turn")
        elif not Is_turn_X:
            printText("O turn")





    #그린 것을 화면에 업데이트
    #이는 모든 draw명령 뒤에 위치해야한다
    pygame.display.update()
