import pygame
from button import Button
from constants import *
from player import Player
from sprite import Sprite


# Fonts

fonts = {
    "text1": pygame.font.Font('fonts/trigram.ttf', 28),
    "score": pygame.font.Font('fonts/trigram.ttf', SCORE_TEXT_SIZE)
}


# Images

heart_icon = Sprite(pygame.image.load(
    "sprites/heart-icon.png").convert_alpha(), 20, 20, 0.09, "topleft")

enemy_image = pygame.image.load(
    "sprites/enemy.png").convert_alpha()


# Text

score_text = fonts["score"].render(
    "0", True, (50, 50, 50))

score_text_rect = score_text.get_rect(
    center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

lives_text = fonts["text1"].render(
    "0", True, (255, 255, 255))


# Game objects

player = Player(pygame.image.load(
    "sprites/canonLineArt.png").convert_alpha(), SCREEN_WIDTH/2, SCREEN_HEIGHT)

button_width = 300
button_height = 60
restart_button = Button(pygame.Rect((SCREEN_WIDTH-button_width)/2, (SCREEN_HEIGHT-button_height)/2-50, button_width, button_height),
                        (255, 255, 255), "Restart", (0, 0, 0), fonts["text1"])
quit_button = Button(pygame.Rect((SCREEN_WIDTH-button_width)/2, (SCREEN_HEIGHT-button_height)/2+50, button_width, button_height),
                     (255, 255, 255), "Quit", (0, 0, 0), fonts["text1"], pygame.quit)

buttons = [restart_button, quit_button]
