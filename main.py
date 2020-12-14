import pygame, sys
from snake.constants import WIDTH,HEIGHT,GREEN, VELOCITY, RUSH, UP, DOWN, LEFT, RIGHT, BLACK, LIGHT_BLUE, MENU_BACKGROUND,  SNAKE_COLOR
from snake.game import Game
from pygame.math import Vector2
from snake.tools import create_button, change_color
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
clock=pygame.time.Clock()
pygame.display.set_caption('Snake')
clicked = False
clock.tick(140)
def menu():
    while True:
        screen.blit(MENU_BACKGROUND, (0,0))
        play_button, playbtn_surface, playbtn_rect = create_button('Jugar', (56,74,12), (WIDTH/2-100, HEIGHT/2 - 125), 200, 50)
        options_button, options_surface, options_rect = create_button('Opciones', (56,74,12), (WIDTH/2-100, HEIGHT/2 - 25), 200, 50)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.rect(screen, LIGHT_BLUE, play_button)
        pygame.draw.rect(screen, LIGHT_BLUE, options_button)
        screen.blit(playbtn_surface, playbtn_rect)
        screen.blit(options_surface, options_rect)
        if play_button.collidepoint((mouse_x, mouse_y)):
            if clicked:
                game_scene()
        elif options_button.collidepoint((mouse_x, mouse_y)):
            if clicked:
                options()
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
        
game = Game(screen)
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

def options():
    clicked = False
    run=True
    while run:
        screen.blit(MENU_BACKGROUND, (0,0))
        purplebtn, purplebtn_surface, purplebtn_rect = create_button('Morado', (56,74,12), (WIDTH/2-100, HEIGHT/2 - 125), 200, 50)
        pinkbtn, pinkbtn_surface, pinkbtn_rect = create_button('Rosa', (56,74,12), (WIDTH/2-100, HEIGHT/2 - 25), 200, 50)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.rect(screen, LIGHT_BLUE, purplebtn)
        pygame.draw.rect(screen, LIGHT_BLUE, pinkbtn)
        screen.blit(purplebtn_surface, purplebtn_rect)
        screen.blit(pinkbtn_surface, pinkbtn_rect)
        if purplebtn.collidepoint((mouse_x, mouse_y)):
            if clicked:
                change_color("PURPLE")
                print(SNAKE_COLOR, "changed")
        elif pinkbtn.collidepoint((mouse_x, mouse_y)):
            if clicked:
                change_color("PINK")
                print(SNAKE_COLOR, "changed")
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
        pygame.display.update()
menu()


