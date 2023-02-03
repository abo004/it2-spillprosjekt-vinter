import pygame
from constants import STARTING_NUMBER_OF_ENEMIES

velocity = 100
number_of_enemies = 0
score = 0
lives = 0
enemies = pygame.sprite.Group()


def reduce_lives():
    global lives
    lives -= 1


def init_game():
    global velocity
    global number_of_enemies
    global score
    global lives
    global enemies

    velocity = 100
    number_of_enemies = STARTING_NUMBER_OF_ENEMIES
    score = 0
    lives = 3
    enemies = pygame.sprite.Group()
