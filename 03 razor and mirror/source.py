import sys
import pygame
from pygame.locals import *

font = 'myfont.ttf' #ba안경고딕

color_red = (255,0,0)
color_white = (255,255,255)
color_graywhite = (127,127,127)
color_black = (0,0,0)


board_position_vertex_point = ((450, 50),(820, 50),(1005, 370.43),(820, 690.86),(450, 690.86),(265, 370.43), (450, 50))
board_position_edge_point = []
board_position_all_point = []
for i in range(6):
    board_position_edge_point_element = []
    new_edge_point_X = (board_position_vertex_point[i+1][0] - board_position_vertex_point[i][0]) / 8
    new_edge_point_Y = (board_position_vertex_point[i+1][1] - board_position_vertex_point[i][1]) / 8
    for j in range(8):
        new_edge_point = (board_position_vertex_point[i][0] + new_edge_point_X * j, board_position_vertex_point[i][1] + new_edge_point_Y * j)
        board_position_edge_point_element.append(new_edge_point)
    board_position_edge_point.append(board_position_edge_point_element)

board_position_all_point.append(board_position_edge_point[0])
board_position_all_point[0].append(board_position_edge_point[1][0])
for i in range(8):
    board_position_all_point_element = []
    new_edge_point_X = (board_position_edge_point[1][i][0] - board_position_edge_point[5][7-i][0] + board_position_edge_point[0][0][1]/2)/ (i + 9)
    new_edge_point_Y = board_position_edge_point[1][i][1] + board_position_edge_point[1][2][1] - board_position_edge_point[1][1][1]
    for j in range(i + 10):
        new_edge_point = (board_position_edge_point[5][7-i][0] + new_edge_point_X * j, new_edge_point_Y)
        board_position_all_point_element.append(new_edge_point)
    board_position_all_point.append(board_position_all_point_element)
for i in range(7):
    board_position_all_point_element = []
    new_edge_point_X = (board_position_edge_point[2][i][0] - board_position_edge_point[4][7-i][0] + board_position_edge_point[0][0][1]/2 )/ (16-i)
    new_edge_point_Y = board_position_edge_point[2][i][1] + board_position_edge_point[1][2][1] - board_position_edge_point[1][1][1]
    for j in range(16 - i):
        new_edge_point = (board_position_edge_point[4][7-i][0] + new_edge_point_X * j, new_edge_point_Y)
        board_position_all_point_element.append(new_edge_point)
    board_position_all_point.append(board_position_all_point_element)
        
board_position_all_point.append(board_position_edge_point[3][:-1])
board_position_all_point[-1].append(board_position_edge_point[3][7])
board_position_all_point[-1].append(board_position_edge_point[4][0])




left_mouse = 1
right_mouse = 3

resolution = (1280, 720)
FPS = 60
clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("Mirror and Razor")
screen = pygame.display.set_mode(resolution)


current = 'menu'
while True:
    left_mouse_clicked = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == left_mouse:
            left_mouse_clicked = True
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos

    screen.fill(color_black)       

    if current == 'menu':
        if left_mouse_clicked and 610 < mouse_pos[0] < 670 and 400 < mouse_pos[1] < 440:
            current = 'game'
            continue
        if left_mouse_clicked and 610 < mouse_pos[0] < 670 and 460 < mouse_pos[1] < 500:
            pygame.quit()
            sys.exit()
        
        font_title = pygame.font.Font(font, 50)
        text_title = font_title.render('Mirror and Razor', True, color_white)
        text_title_Rect = text_title.get_rect()
        text_title_Rect.center = (640, 320)

        font_play = pygame.font.Font(font, 20)
        if (610 < mouse_pos[0] < 670 and 400 < mouse_pos[1] < 440):
            text_play = font_play.render('Play', True, color_red)
        else:
            text_play = font_play.render('Play', True, color_white)
        text_play_Rect = text_play.get_rect()
        text_play_Rect.center = (640, 420)

        font_exit = pygame.font.Font(font, 20)
        if (610 < mouse_pos[0] < 670 and 460 < mouse_pos[1] < 500):
            text_exit = font_exit.render('Exit', True, color_red)
        else:
            text_exit = font_exit.render('Exit', True, color_white)
        text_exit_Rect = text_exit.get_rect()
        text_exit_Rect.center = (640, 480)

        screen.blit(text_title, text_title_Rect)
        screen.blit(text_play, text_play_Rect)
        screen.blit(text_exit, text_exit_Rect)
        pygame.display.flip()


    elif current == 'game':
        pygame.draw.aalines(screen, color_white, False, board_position_vertex_point)

        for i in range(3):
            pygame.draw.aaline(screen, color_graywhite, board_position_edge_point[i][0], board_position_edge_point[i+3][0])
        for i in range(7):
            pygame.draw.aaline(screen, color_graywhite, board_position_edge_point[0][i+1], board_position_edge_point[2][7-i])
            pygame.draw.aaline(screen, color_graywhite, board_position_edge_point[5][i+1], board_position_edge_point[3][7-i])
            pygame.draw.aaline(screen, color_graywhite, board_position_edge_point[1][i+1], board_position_edge_point[5][7-i])
            pygame.draw.aaline(screen, color_graywhite, board_position_edge_point[2][i+1], board_position_edge_point[4][7-i])
            pygame.draw.aaline(screen, color_graywhite, board_position_edge_point[0][i+1], board_position_edge_point[4][7-i])
            pygame.draw.aaline(screen, color_graywhite, board_position_edge_point[1][i+1], board_position_edge_point[3][7-i])

        for i in board_position_all_point:
            for j in i:
                if  j[0]-5<mouse_pos[0]<j[0]+5 and j[1]-5<mouse_pos[1]<j[1]+5:
                    pygame.draw.circle(screen, color_graywhite, (round(j[0]), round(j[1])), 10, 0)
                pygame.draw.circle(screen, color_white, (round(j[0]), round(j[1])), 5, 0)

        

        



    pygame.display.flip()
    clock.tick(FPS)
