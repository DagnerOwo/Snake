from .snake import Snake
import pygame
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
    def update(self):
        self.food.draw_food(self.screen)
        self.snake.draw_snake(self.screen)
        pygame.display.update()
    def change_snake_direction(self, direction):
        self.snake.direction = direction