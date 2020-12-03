from pygame.math import Vector2
import pygame
WIDTH=600
HEIGHT=600
BLACK=(0,0,0)
GREEN=(17,200,41)
RED=(243,14,24)
SQUARE_SIZE=25
ROWS=WIDTH/SQUARE_SIZE
COLS=HEIGHT/SQUARE_SIZE
VELOCITY=150
RUSH = VELOCITY // 2
RIGHT=Vector2(1,0)
LEFT=Vector2(-1,0)
UP=Vector2(0,-1)
DOWN=Vector2(0,1)
HEAD_UP = pygame.transform.scale(pygame.image.load('assets/head_up.png'), (SQUARE_SIZE, SQUARE_SIZE))
HEAD_DOWN = pygame.transform.scale(pygame.image.load('assets/head_down.png'), (SQUARE_SIZE, SQUARE_SIZE))
HEAD_RIGHT = pygame.transform.scale(pygame.image.load('assets/head_right.png'), (SQUARE_SIZE, SQUARE_SIZE))
HEAD_LEFT = pygame.transform.scale(pygame.image.load('assets/head_left.png'), (SQUARE_SIZE, SQUARE_SIZE))
APPLE = pygame.transform.scale(pygame.image.load('assets/apple.png'), (SQUARE_SIZE, SQUARE_SIZE))