import pygame
from snake.constants import WIDTH,HEIGHT,GREEN, VELOCITY, RUSH, UP, DOWN, LEFT, RIGHT
from snake.game import Game
from pygame.math import Vector2
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
clock=pygame.time.Clock()
pygame.display.set_caption('Snake')
def main():
    game = Game(screen)
    clock.tick(60)
    run=True
    game.draw_everything()
    SCREEN_UPDATE=pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,VELOCITY)
    while run:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == SCREEN_UPDATE:
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pygame.time.set_timer(SCREEN_UPDATE,VELOCITY)
        screen.fill(GREEN)
        game.update()
    pygame.quit()
main()


