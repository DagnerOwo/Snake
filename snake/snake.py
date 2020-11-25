import pygame
from .constants import SQUARE_SIZE,BLACK
from pygame.math import Vector2
class Snake:
    def __init__(self):
        self.body = [Vector2(3,4),Vector2(4,4),Vector2(5,4)]
        self.direction = Vector2(1,0)
    def draw_snake(self, screen):
        for block in self.body:
            block_rect=pygame.Rect(block.x*SQUARE_SIZE,block.y*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
            pygame.draw.rect(screen,BLACK,block_rect)
    def move_snake(self):
        #Copiamos el cuerpo entero menos la última posicion
        body_c = self.body[:-1]
        body_c.insert(0, body_c[0]+self.direction)
        self.body = body_c[:]
        