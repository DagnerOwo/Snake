import pygame
#Devuelve un Objeto tipo Rect con un texto en el centro
def create_button(text, colorrgb, position, width, height):
    game_font = pygame.font.Font('assets/NerkoOne-Regular.ttf', 25) 
    btn_text = str(text)
    btn_surface = game_font.render(btn_text,True,colorrgb)
    btn_rect = btn_surface.get_rect(center = (position[0]+ (width/2),position[1]+(height/2)))
    button = pygame.Rect(position[0],position[1], width, height)
    return button, btn_surface, btn_rect