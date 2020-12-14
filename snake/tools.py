import pygame
#Devuelve un Objeto tipo Rect con un texto en el centro
def create_button(text, colorrgb, position, width, height):
    game_font = pygame.font.Font('assets/NerkoOne-Regular.ttf', 25) 
    btn_text = str(text)
    btn_surface = game_font.render(btn_text,True,colorrgb)
    btn_rect = btn_surface.get_rect(center = (position[0]+ (width/2),position[1]+(height/2)))
    button = pygame.Rect(position[0],position[1], width, height)
    return button, btn_surface, btn_rect
#Lee un archivo y cambia el color
import fileinput

def read_color():
    SNAKE_COLOR = "PURPLE"
    with open('config/game_config.txt') as reader:
        lines_list = reader.readlines()
        for line in lines_list:
            if "SNAKE_COLOR" in line:
                splited_line = line.split(":")
                SNAKE_COLOR = splited_line[1]
    return SNAKE_COLOR
def change_color(color):
    SNAKE_COLOR = read_color()
    fin = open("config/game_config.txt", "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace(SNAKE_COLOR, color)
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open("config/game_config.txt", "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
        