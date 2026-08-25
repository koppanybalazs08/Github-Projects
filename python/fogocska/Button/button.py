import pygame
from typing import Callable

class button():
    def __init__(self, color1:tuple, color2:tuple, screen, x:int, y:int, width:int, height:int, text_input:str, text_font:str, text_color:tuple, hover:bool):
        self.screen = screen
        self.color1 = color1
        self.color2 = color2

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x, self.y)

        self.text_input = text_input
        self.text_font = text_font
        self.text_color = text_color
        self.text = self.text_font.render(self.text_input, True, self.text_color)
        self.text_rect = self.text.get_rect(center = (self.x, self.y))

        self.hover = hover

    #gomb frissítése a képernyőn
    def update(self):
        self.screen.blit(self.text, self.text_rect)

    #gomb hátterének frissítése a képernyőn
    def update_bg(self, m_pos):
        pygame.draw.rect(self.screen, self.color1, self.rect)
        if self.hover:
            if m_pos[0] in range(self.rect.left, self.rect.right) and m_pos[1] in range(self.rect.top, self.rect.bottom):
                    pygame.draw.rect(self.screen, self.color2, self.rect)

    #input ellenőrzés
    def check_input(self, f:Callable, m_pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if m_pos[0] in range(self.rect.left, self.rect.right) and m_pos[1] in range(self.rect.top, self.rect.bottom):
                f()