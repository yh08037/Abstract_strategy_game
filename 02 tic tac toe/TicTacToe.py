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


O_placed = []
X_placed = []
Is_turn_X = True


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
def printText(msg, color='BLACK', pos=(1100, 150)):
    textSurface = font.render(msg, True, pygame.Color(color), None)
    textRect = textSurface.get_rect()
    textRect.center = pos

    screen.blit(textSurface, textRect)


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

    # 가로세로줄 그리기
    for i in range(0, 4):
        pygame.draw.line(screen, BLACK, boardPos[0][i], boardPos[3][i], 5)
        pygame.draw.line(screen, BLACK, boardPos[i][0], boardPos[i][3], 5)      


    # 마우스 클릭 정보 저장하기
    IsBreak = False
    for x in range(3):
        for y in range(3):
            if leftMouseClicked and Is_mousePos_in_boardPos(mousePos, boardPos[x][y]):
                Is_it_Placed = boardPos[x][y] in X_placed or boardPos[x][y] in O_placed 
                if Is_turn_X and not Is_it_Placed:
                    X_placed.append(boardPos[x][y])
                    Is_turn_X = False
                elif not Is_turn_X and not Is_it_Placed:
                    O_placed.append(boardPos[x][y])
                    Is_turn_X = True
                IsBreak = True
                break
        if IsBreak:
            break


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

