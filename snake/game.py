from .snake import Snake
import pygame
from .constants import LEFT, RIGHT, DOWN, UP, SQUARE_SIZE, ROWS, COLS
from .food import Food
from pygame.math import Vector2
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.moved_done = False
        self.snake = Snake()
        self.food = Food()
    def draw_everything(self):
        self.snake.draw_snake(self.screen)
        self.food.draw_food(self.screen)
    def _move(self):
        self.snake.move_snake()
        self.eat_food()
        self.check_collitions()
        print(self.snake.body[0])
    def update(self):
        self.food.draw_food(self.screen)
        self.snake.draw_snake(self.screen)
        self.draw_score()

        pygame.display.update()
    def change_snake_direction(self, direction):
        #Can not move opposite direction
        if self.moved_done == True:
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
        self.moved_done = False
    #enlarge snake, and score
    def eat_food(self):
        if self.snake.body[0] == self.food.pos:
            self.snake.enlarge()
            self.food.generate_food()
            self.score += 1
            print(self.score, 'SCORE')
    #Collitions to his body and walls
    def check_collitions(self):
        if self.snake.body[0].x<0 or self.snake.body[0].x>=COLS:
            self.score = 0
            self.snake=Snake()
        if self.snake.body[0].y<0 or self.snake.body[0].y>=ROWS:
            self.snake=Snake()
            self.score = 0
        # Body collition
        if self.snake.body[0] in self.snake.body[1:]:
            self.snake = Snake()
            self.score = 0
    def draw_score(self):
        game_font = pygame.font.Font('assets/NerkoOne-Regular.ttf', 25) 
        score_text = str(self.score)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(SQUARE_SIZE * COLS - 20)
        score_y = int(SQUARE_SIZE * ROWS - 20)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        self.screen.blit(score_surface,score_rect)
