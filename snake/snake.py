import pygame
from .constants import SQUARE_SIZE, BLACK, UP
from pygame.math import Vector2
from .tools import read_color

class Snake:
    def __init__(self):
        self.body = [Vector2(20, 20), Vector2(20, 21), Vector2(20, 22)]
        self.direction = UP
        self.crunch_sound = pygame.mixer.Sound("assets/sounds/crunch.wav")
        self.definir_color()
        # NUEVOS CAMBIOS

    def draw_snake(self, screen):
        self.update_head()
        self.update_tail()
        for index, block in enumerate(self.body):
            block_rect = pygame.Rect(
                block.x*SQUARE_SIZE, block.y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1]-block
                next_block = self.body[index - 1]-block
                if previous_block.x == next_block.x:
                    screen.blit(self.BODY_VERTICAL, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.BODY_HORIZONTAL, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.BODY_TL, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.BODY_BL, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.BODY_TR, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.BODY_BR, block_rect)

    def move_snake(self):
        # Copiamos el cuerpo entero menos la última posicion
        body_c = self.body[:-1]
        body_c.insert(0, body_c[0]+self.direction)
        self.body = body_c[:]

    def enlarge(self):
        #self.body.append(self.body[-1]+self.direction)
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        #play Sound
    def play_crunch_sound(self): self.crunch_sound.play()

    def update_head(self):
        """
        if self.direction == UP:
            self.head = HEAD_UP
        elif self.direction == RIGHT:
            self.head = HEAD_RIGHT
        elif self.direction == DOWN:
            self.head = HEAD_DOWN
        elif self.direction == LEFT:
            self.head = HEAD_LEFT
        """
        head_relation_vector = self.body[1] - self.body[0]
        if head_relation_vector == Vector2(1, 0):
            self.head = self.HEAD_LEFT
        elif head_relation_vector == Vector2(-1, 0):
            self.head = self.HEAD_RIGHT
        elif head_relation_vector == Vector2(0, 1):
            self.head = self.HEAD_UP
        elif head_relation_vector == Vector2(0, -1):
            self.head = self.HEAD_DOWN

    def update_tail(self):
        tail_relation_vector = self.body[-2] - self.body[-1]
        if tail_relation_vector == Vector2(1, 0):
            self.tail = self.TAIL_LEFT
        elif tail_relation_vector == Vector2(-1, 0):
            self.tail = self.TAIL_RIGHT
        elif tail_relation_vector == Vector2(0, 1):
            self.tail = self.TAIL_UP
        elif tail_relation_vector == Vector2(0, -1):
            self.tail = self.TAIL_DOWN
    def definir_color(self):
        #Lee el archivo config y busca la opcion SNAKE_COLOR
        SNAKE_COLOR = read_color()
        
        if SNAKE_COLOR == "PURPLE":
            self.HEAD_UP = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/head_up.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.HEAD_DOWN = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/head_down.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.HEAD_RIGHT = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/head_right.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.HEAD_LEFT = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/head_left.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_UP = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/tail_up.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_DOWN = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/tail_down.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_RIGHT = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/tail_right.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_LEFT = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/tail_left.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_BL = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_bl.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_BR = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_br.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_HORIZONTAL = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_horizontal.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_TL = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_tl.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_TR = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_tr.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_VERTICAL = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_vertical.png'), (SQUARE_SIZE, SQUARE_SIZE))
            print(SNAKE_COLOR)
        elif SNAKE_COLOR == "PINK":
            self.HEAD_UP = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_head_up.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.HEAD_DOWN = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_head_down.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.HEAD_RIGHT = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_head_right.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.HEAD_LEFT = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_head_left.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_UP = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_tail_up.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_DOWN = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_tail_down.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_RIGHT = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_tail_right.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_LEFT = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_tail_left.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_BL = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_body_bl.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_BR = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_body_br.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_HORIZONTAL = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_body_horizontal.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_TL = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_body_tl.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_TR = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_body_tr.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_VERTICAL = pygame.transform.scale(pygame.image.load('assets/snake_images/pink/pink_body_vertical.png'), (SQUARE_SIZE, SQUARE_SIZE))
            print(SNAKE_COLOR)
        else:
            self.HEAD_UP = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/head_up.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.HEAD_DOWN = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/head_down.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.HEAD_RIGHT = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/head_right.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.HEAD_LEFT = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/head_left.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_UP = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/tail_up.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_DOWN = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/tail_down.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_RIGHT = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/tail_right.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.TAIL_LEFT = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/tail_left.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_BL = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_bl.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_BR = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_br.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_HORIZONTAL = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_horizontal.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_TL = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_tl.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_TR = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_tr.png'), (SQUARE_SIZE, SQUARE_SIZE))
            self.BODY_VERTICAL = pygame.transform.scale(pygame.image.load('assets/snake_images/purple/body_vertical.png'), (SQUARE_SIZE, SQUARE_SIZE))
        print(SNAKE_COLOR + "SOY SNAKE")