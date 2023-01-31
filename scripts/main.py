#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 09:12:22 2023

@author: Alvaro && Henrik
"""

import pygame
import random
from player import Player
from enemy import Enemy
from button import Button
from bullet import Bullet
from sprite import Sprite

# Initialize Pygame
pygame.init()

# Set up the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("OSU 2")

FPS = 60

player = Player(pygame.image.load(
    "sprites/gunner.png").convert_alpha(), SCREEN_WIDTH/2, SCREEN_HEIGHT)

fonts = {
    "text1": pygame.font.Font(None, 36),
    "score": pygame.font.Font(None, 240)
}


def reduce_lives():
    global lives
    lives -= 1


def init_game():
    global velocity
    global starting_number_of_enemies
    global number_of_enemies
    global score
    global lives
    global enemies
    global levels

    velocity = 100
    starting_number_of_enemies = 3
    number_of_enemies = starting_number_of_enemies
    score = 0
    lives = 3
    enemies = pygame.sprite.Group()


dt = 0

clock = pygame.time.Clock()
running = True

button_width = 200
button_height = 40
restart_button = Button(pygame.Rect((SCREEN_WIDTH-button_width)/2, (SCREEN_HEIGHT-button_height)/2-50, button_width, button_height),
                        (255, 255, 255), "Restart", (0, 0, 0), fonts["text1"], init_game)
quit_button = Button(pygame.Rect((SCREEN_WIDTH-button_width)/2, (SCREEN_HEIGHT-button_height)/2+50, button_width, button_height),
                     (255, 255, 255), "Quit", (0, 0, 0), fonts["text1"], pygame.quit)

buttons = [restart_button, quit_button]

heart_icon = Sprite(pygame.image.load(
    "sprites/heart-icon.png").convert_alpha(), 20, 20, 0.09, "topleft")

enemy_image = pygame.image.load(
    "sprites/enemy1.png").convert_alpha()

init_game()


while running:
    screen.fill((0, 0, 0))

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if lives > 0:
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                player.point_at(x, y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for enemy in enemies:
                    if enemy.rect.collidepoint(x, y):
                        score += 1
                        enemies.remove(enemy)
                        number_of_enemies = starting_number_of_enemies + score//10

        enemies.update(enemies, dt)

        for i in range(len(enemies), number_of_enemies):
            rand_variation = random.random()+0.5
            enemies.add(Enemy((enemy_image, 0, 0, 0.02, "center"), velocity +
                              rand_variation*rand_variation*velocity, SCREEN_WIDTH, SCREEN_HEIGHT, reduce_lives, (rand_variation)))

        score_text = fonts["score"].render(
            f"{score}", True, (50, 50, 50))
        score_text_rect = score_text.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(score_text, score_text_rect)

        enemies.draw(screen)

        screen.blit(player.image, player.rect)

        lives_text = fonts["text1"].render(
            f"{lives}", True, (255, 255, 255))
        screen.blit(heart_icon.image, heart_icon.rect)
        screen.blit(lives_text, (55, 20))

    else:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button in buttons:
                    if button.rect.collidepoint(x, y):
                        button.on_click()

        for button in buttons:
            button.draw(screen)

    pygame.display.update()

    dt = clock.tick(FPS) / 1000

# Close Pygame
pygame.quit()
