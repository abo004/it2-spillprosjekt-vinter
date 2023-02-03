import pygame
from assets import *


def handle_input(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for button in buttons:
                if button.rect.collidepoint(x, y):
                    button.on_click()


def update(dt):
    pass


def draw(screen):
    for button in buttons:
            button.draw(screen)
