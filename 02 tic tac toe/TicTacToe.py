import pygame

#RGB 포맷으로 색 정의 
BLACK = (0,   0,   0  )
WHITE = (255, 255, 255)

#게임 엔진 초기화
pygame.init()

#화면 높이와 폭 설정
size   = [1280, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

#3X3 게임 판의 꼭짓점 좌표 리스트
boardPosition = [[(340, 60), (540, 60), (740, 60), (940, 60)],
                 [(340, 260), (540, 260), (740, 260), (940, 260)],
                 [(340, 460), (540, 460), (740, 460), (940, 460)],
                 [(340, 660), (540, 660), (740, 660), (940, 660)]]


done  = False
FPS   = 10
clock = pygame.time.Clock()


while not done:

    clock.tick(FPS)

    #메인 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill(WHITE)

    #가로세로줄 그리기
    for i in range(0, 4):
        pygame.draw.line(screen, BLACK, boardPosition[0][i], boardPosition[3][i], 5)
        pygame.draw.line(screen, BLACK, boardPosition[i][0], boardPosition[i][3], 5)      


    #그린 것을 화면에 업데이트
    #이는 모든 draw명령 뒤에 위치해야한다
    pygame.display.update()

pygame.quit()
