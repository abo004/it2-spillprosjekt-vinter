if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


import pygame
import random
from assets import *
from enemy import Enemy
from constants import *


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


restart_button.action = init_game
init_game()


def handle_input(events):
    global enemies
    global number_of_enemies
    global score

    for event in events:
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            player.point_at(x, y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for enemy in enemies:
                if enemy.rect.collidepoint(x, y):
                    score += 1
                    enemies.remove(enemy)
                    number_of_enemies = STARTING_NUMBER_OF_ENEMIES + score//10


def update(dt):
    global score_text
    global lives_text
    global enemies
    global lives

    enemies.update(enemies, dt)

    # print(number_of_enemies)

    for i in range(len(enemies), number_of_enemies):
        rand_variation = random.random()+0.5
        enemies.add(Enemy((enemy_image, 0, 0, 0.02, "center"), velocity +
                          rand_variation*rand_variation*velocity, SCREEN_WIDTH, SCREEN_HEIGHT, reduce_lives, (rand_variation)))

    score_text = fonts["score"].render(
        f"{score}", True, (50, 50, 50))

    lives_text = fonts["text1"].render(
        f"{lives}", True, (255, 255, 255))


def draw(screen):
    screen.blit(score_text, score_text_rect)
    enemies.draw(screen)

    screen.blit(player.image, player.rect)
    screen.blit(heart_icon.image, heart_icon.rect)
    screen.blit(lives_text, (55, 20))
