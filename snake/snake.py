import pygame
from .constants import SQUARE_SIZE,BLACK, HEAD_RIGHT, HEAD_LEFT, HEAD_UP, HEAD_DOWN, UP, DOWN, RIGHT, LEFT
from pygame.math import Vector2
class Snake:
    def __init__(self):
        self.body = [Vector2(3,4),Vector2(4,4),Vector2(5,4)]
        self.direction = Vector2(1,0)
        #NUEVOS CAMBIOS
    def draw_snake(self, screen):
        self.update_head()
        for index, block in enumerate(self.body):
            block_rect=pygame.Rect(block.x*SQUARE_SIZE,block.y*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
            if index == 0:
                screen.blit(self.head, block_rect)
            else:
                pygame.draw.rect(screen,BLACK,block_rect)
    def move_snake(self):
        #Copiamos el cuerpo entero menos la última posicion
        body_c = self.body[:-1]
        body_c.insert(0, body_c[0]+self.direction)
        self.body = body_c[:]
    def enlarge(self):
        body_c = self.body[:]
        body_c.insert(0, body_c[0]+self.direction)
        self.body = body_c[:]
    def update_head(self):
        if self.direction == UP: self.head = HEAD_UP
        elif self.direction == RIGHT: self.head = HEAD_RIGHT
        elif self.direction == DOWN: self.head = HEAD_DOWN
        elif self.direction == LEFT: self.head = HEAD_LEFT
        """
        head_relation_vector = self.body[1] - self.body[0]
        if head_relation_vector == Vector2(1,0): self.head = HEAD_LEFT
        elif head_relation_vector == Vector2(-1,0): self.head = HEAD_RIGHT
        elif head_relation_vector == Vector2(0,1): self.head = HEAD_UP
        elif head_relation_vector == Vector2(0,-1): self.head = HEAD_DOWN
        """