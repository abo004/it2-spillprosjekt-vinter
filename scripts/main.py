#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 09:12:22 2023

@author: Alvaro && Henrik
"""

import pygame

if __name__ == "__main__":
    from load_window import *
    from constants import *
    import end_screen
    import game

    pygame.mixer.music.load("sounds/gamingmusiccoollol.mp3")
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        screen.fill((0, 0, 0))

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if game.lives > 0:
            game.handle_input(events)
            game.update(dt, pygame.time.get_ticks())
            game.draw(screen)

        else:
            end_screen.handle_input(events)
            end_screen.draw(screen)

        pygame.display.update()

        dt = clock.tick(FPS) / 1000

    pygame.mixer.stop()
    pygame.quit()
