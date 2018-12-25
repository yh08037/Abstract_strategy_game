import sys
import pygame
from pygame.locals import *

font = 'myfont.ttf' #ba안경고딕

color_red = (255,0,0)
color_white = (255,255,255)
color_graywhite = (200,200,200)
color_black = (0,0,0)


board_position_point = ((450, 50),(820, 50),(1005, 370.43),(820, 690.86),(450, 690.86),(265, 370.43))
board_position_edge = []

append_x = (board_position_point[1][0] - board_position_point[0][0]) / 8
board_position_edge.append(
    



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

        screen.fill(color_black)
        screen.blit(text_title, text_title_Rect)
        screen.blit(text_play, text_play_Rect)
        screen.blit(text_exit, text_exit_Rect)
        pygame.display.flip()


    elif current == 'game':
        screen.fill(color_black)
        pygame.draw.polygon(screen, color_white, board_position_point, 2)
        
            
            
        

        
    pygame.display.flip()
    clock.tick(FPS)
