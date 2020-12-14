from pygame.math import Vector2
import pygame
WIDTH=600
HEIGHT=600
BLACK=(0,0,0)
GREEN=(17,200,41)
LIGHT_BLUE=(16,216,221)
SQUARE_SIZE=25
ROWS=WIDTH/SQUARE_SIZE
COLS=HEIGHT/SQUARE_SIZE
VELOCITY=150
RUSH = VELOCITY // 2
RIGHT=Vector2(1,0)
LEFT=Vector2(-1,0)
UP=Vector2(0,-1)
DOWN=Vector2(0,1)
SNAKE_COLOR = "PINK"
APPLE = pygame.transform.scale(pygame.image.load('assets/apple.png'), (int(SQUARE_SIZE// 1.5), int(SQUARE_SIZE//1.5)))

MENU_BACKGROUND = pygame.transform.scale(pygame.image.load('assets/snake_background_menu.jpg'), (WIDTH, HEIGHT))