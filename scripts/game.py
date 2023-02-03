if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


import pygame
import random
from assets import *
from enemy import Enemy
from constants import *
from math import sin
from xplodelib import Explosion
from easing_functions import QuadEaseInOut, QuadEaseOut


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

boom_sound = pygame.mixer.Sound("sounds/dramatic-boom.mp3")
explosions = []
STARTING_BRIGHTNESS = 50
BRIGHTNESS_TIME = 500
time_of_last_kill = -1000


def handle_input(events):
    global enemies
    global number_of_enemies
    global score_text_rect
    global score_text
    global score
    global time_of_last_kill

    for event in events:
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            player.point_at(x, y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for enemy in enemies:
                if enemy.rect.collidepoint(x, y):
                    score += 1

                    time_of_last_kill = pygame.time.get_ticks()
                    explosions.append(Explosion((x, y), 20))
                    enemies.remove(enemy)
                    number_of_enemies = STARTING_NUMBER_OF_ENEMIES + score//10
                    boom_sound.play()

                    break


def update(dt, time):
    global score_text
    global lives_text
    global enemies
    global lives
    global score_text_rect

    enemies.update(enemies, dt)
    for explosion in explosions:
        explosion.update(explosions, dt)

    for i in range(len(enemies), number_of_enemies):
        rand_variation = random.random()+0.5
        enemies.add(Enemy((enemy_image, 0, 0, 0.2, "center"), velocity +
                          rand_variation*rand_variation*velocity, SCREEN_WIDTH, SCREEN_HEIGHT, reduce_lives, (rand_variation)))

    brigthness = (time_of_last_kill + BRIGHTNESS_TIME - pygame.time.get_ticks())/BRIGHTNESS_TIME*50+STARTING_BRIGHTNESS if time_of_last_kill + \
        BRIGHTNESS_TIME > pygame.time.get_ticks() else STARTING_BRIGHTNESS

    score_text = pygame.font.Font('fonts/trigram.ttf', SCORE_TEXT_SIZE + int(50*(sin(time/1000)))).render(
        f"{score}", True, (brigthness, brigthness, brigthness))

    score_text_rect = score_text.get_rect(
        center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    lives_text = fonts["text1"].render(
        f"{lives}", True, (255, 255, 255))


def draw(screen):
    screen.blit(score_text, score_text_rect)

    for explosion in explosions:
        explosion.draw(screen)
    enemies.draw(screen)

    screen.blit(player.image, player.rect)
    screen.blit(heart_icon.image, heart_icon.rect)
    screen.blit(lives_text, (55, 14))
