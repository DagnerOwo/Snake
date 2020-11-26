from .snake import Snake
import pygame
from .constants import LEFT, RIGHT, DOWN, UP
from .food import Food
from pygame.math import Vector2
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake = Snake()
        self.food = Food()
    def draw_everything(self):
        self.snake.draw_snake(self.screen)
        self.food.draw_food(self.screen)
    def _move(self):
        self.snake.move_snake()
        self.eat_food()
        print(self.snake.body[0])
    def update(self):
        self.food.draw_food(self.screen)
        self.snake.draw_snake(self.screen)
        
        pygame.display.update()
    def change_snake_direction(self, direction):
        #Can not move opposite direction
        if direction == UP and self.snake.direction == DOWN:
            direction = DOWN
            self.snake.direction = direction
        elif direction == DOWN and self.snake.direction == UP:
            direction = UP
            self.snake.direction = direction
        elif direction == RIGHT and self.snake.direction == LEFT:
            direction = LEFT
            self.snake.direction = direction
        elif direction == LEFT and self.snake.direction == RIGHT:
            direction = RIGHT
            self.snake.direction = direction
        else:
            self.snake.direction = direction
    #enlarge snake, and score
    def eat_food(self):
        if self.snake.body[0] == self.food.pos:
            self.food.generate_food()
            self.snake.enlarge()
    #Collitions to his body and walls
    def check_collitions(self):
        pass
    