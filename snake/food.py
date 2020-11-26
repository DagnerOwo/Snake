import pygame,random
from .constants import COLS,ROWS,SQUARE_SIZE,RED
from pygame.math import Vector2
class Food:
    def __init__(self):
        self.generate_food()
    def draw_food(self,screen):
        food_rect=pygame.Rect(self.pos.x*SQUARE_SIZE,self.pos.y*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
        pygame.draw.rect(screen,RED,food_rect)
    #generate food in a random position
    def generate_food(self):
        self.pos_x=random.randint(0,COLS-1)
        self.pos_y=random.randint(0,ROWS-1)
        self.pos=Vector2(self.pos_x,self.pos_y)
        print(self.pos, 'COMIDAAAAAAAAAAAAAAAAA')