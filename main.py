import pygame, sys
from snake.constants import WIDTH,HEIGHT,GREEN, VELOCITY, RUSH, UP, DOWN, LEFT, RIGHT, BLACK, LIGHT_BLUE, MENU_BACKGROUND
from snake.game import Game
from pygame.math import Vector2
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
clock=pygame.time.Clock()
pygame.display.set_caption('Snake')
clicked = False
clock.tick(140)
game = Game(screen)
def menu():
    while True:
        game_font = pygame.font.Font('assets/NerkoOne-Regular.ttf', 25) 
        playbtn_text = str('Jugar')
        playbtn_surface = game_font.render(playbtn_text,True,(56,74,12))
        playbtn_rect = playbtn_surface.get_rect(center = (WIDTH/2,HEIGHT/2 - 100))
        screen.blit(MENU_BACKGROUND, (0,0))
        play_button = pygame.Rect(WIDTH/2-100,HEIGHT/2 - 125, 200, 50)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if play_button.collidepoint((mouse_x, mouse_y)):
            if clicked:
                game_scene()
        pygame.draw.rect(screen, LIGHT_BLUE, play_button)
        
        screen.blit(playbtn_surface, playbtn_rect)
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
            pygame.display.update()
def game_scene():
    run=True
    SCREEN_UPDATE=pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,VELOCITY)
    while run:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == SCREEN_UPDATE:
                game.moved_done = True
                game._move()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.change_snake_direction(UP)
                if event.key == pygame.K_RIGHT:
                    game.change_snake_direction(RIGHT)
                if event.key == pygame.K_DOWN:
                    game.change_snake_direction(DOWN)
                if event.key == pygame.K_LEFT:
                    game.change_snake_direction(LEFT)
                if event.key == pygame.K_SPACE:
                    pygame.time.set_timer(SCREEN_UPDATE,RUSH)
                if event.key == pygame.K_ESCAPE:
                    run=False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pygame.time.set_timer(SCREEN_UPDATE,VELOCITY)
        screen.fill(GREEN)
        game.update()
menu()


