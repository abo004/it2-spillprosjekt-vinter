#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 09:12:22 2023

@author: Alvaro
"""

import pygame
import random
from player import Player
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Set up the window
screen_x = 800
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("OSU 2")

fps = 60

# Create a font object
font = pygame.font.Font(None, 36)

player = Player("sprites/Canon.png", screen_x/2, screen_y)
enemies = pygame.sprite.Group()


score = 0
number_of_enemies = 3
velocity = 3
lives = 3


def reduce_lives():
    global lives
    lives -= 1


dt = 0

clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            player.point_at(x, y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for enemy in enemies:
                if enemy.rect.collidepoint(x, y):
                    score += 1
                    enemies.remove(enemy)
                    break

    # Clear the screen
    screen.fill((0, 0, 0))

    enemies.update(enemies, dt)

    for i in range(len(enemies), number_of_enemies):
        enemies.add(Enemy("sprites/sprite0.jpg", velocity +
                    random.randint(0, velocity), screen_x, screen_y, reduce_lives))

    enemies.draw(screen)

    screen.blit(player.image, player.rect)

    # Keep track of score and lives
    lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
    screen.blit(lives_text, (20, 20))

    score_text = font.render(f"Score: {score}", True, (255, 0, 0))
    screen.blit(score_text, (20, 60))

    if lives <= 0:
        running = False

    # Update the display
    pygame.display.update()

    dt = clock.tick(fps) / 1000

# Close Pygame
pygame.quit()
