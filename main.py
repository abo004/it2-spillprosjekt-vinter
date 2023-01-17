#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 09:12:22 2023

@author: Alvaro
"""

import pygame
import random
import player

# Initialize Pygame
pygame.init()

# Set up the window
screen_x = 800
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("OSU 2")

# Create a box class


class Box:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))

    def collides_with_point(self, x, y):
        if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
            return True
        else:
            return False


# Create a list to store the boxes
boxes = []

# Create a font object
font = pygame.font.Font(None, 36)

player = player.Player("sprites/Canon.png", screen_x/2, screen_y)

lives = 3
score = 0

clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            x, y = pygame.mouse.get_pos()
            # Check if the mouse collides with any boxes
            for box in boxes:
                if box.collides_with_point(x, y):
                    boxes.remove(box)
                    score += 1

        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            player.point_at(x, y)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        for box in boxes:
            box.x += 1
    if keys[pygame.K_d]:
        for box in boxes:
            box.x -= 1

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the boxes
    for box in boxes:
        box.draw(screen)

    screen.blit(player.image, player.rect)

    # Generate a new box
    if len(boxes) < 3 and random.randint(0, 100) < 10:
        x = random.randint(0, screen_x - 60)
        y = random.randint(0, screen_y - 60)
        width = random.randint(10, 100)
        height = random.randint(10, 100)
        color = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        boxes.append(Box(x, y, width, height, color))

    # Keep track of score and lives
    lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
    screen.blit(lives_text, (20, 20))

    score_text = font.render(f"Score: {score}", True, (255, 0, 0))
    screen.blit(score_text, (20, 60))

    # Update the display
    pygame.display.update()

    clock.tick(60)

# Close Pygame
pygame.quit()
