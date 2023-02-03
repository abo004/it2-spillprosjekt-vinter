import pygame
import random
import load_game as var
from assets import *
from enemy import Enemy
from constants import *

print(var.lives)
init_game()
print(var.lives)

def handle_input(events):
    for event in events:
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            player.point_at(x, y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for enemy in var.enemies:
                if enemy.rect.collidepoint(x, y):
                    var.score += 1
                    var.enemies.remove(enemy)
                    var.number_of_enemies = STARTING_NUMBER_OF_ENEMIES + var.score//10


def update(dt):
    global score_text
    global lives_text

    var.enemies.update(var.enemies, dt)

    # print(number_of_enemies)

    for i in range(len(var.enemies), var.number_of_enemies):
        rand_variation = random.random()+0.5
        var.enemies.add(Enemy((enemy_image, 0, 0, 0.02, "center"), var.velocity +
                              rand_variation*rand_variation*var.velocity, SCREEN_WIDTH, SCREEN_HEIGHT, var.reduce_lives, (rand_variation)))

    score_text = fonts["score"].render(
        f"{var.score}", True, (50, 50, 50))

    lives_text = fonts["text1"].render(
        f"{var.lives}", True, (255, 255, 255))


def draw(screen):
    screen.blit(score_text, score_text_rect)
    var.enemies.draw(screen)

    screen.blit(player.image, player.rect)
    screen.blit(heart_icon.image, heart_icon.rect)
    screen.blit(lives_text, (55, 20))
