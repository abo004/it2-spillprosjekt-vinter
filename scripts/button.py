import pygame


class Button:
    def __init__(self, rect, bg_color, text, text_color, font, action=None):
        self.rect = rect
        self.bg_color = bg_color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.action = action
        self.clicked = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def on_click(self):
        if self.action:
            self.action()
