import pygame
from random import randint


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_file, vel, screen_x, screen_y, reduce_lives):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.original_image = self.image
        self.rect = self.image.get_rect()

        self.x = -self.rect.width
        self.y = randint(0, screen_y-self.rect.height)

        self.rect.x = self.x
        self.rect.y = self.y

        self.vel = vel
        self.screen_x = screen_x
        self.screen_y = screen_y

        self.reduce_lives = reduce_lives

    def update(self, enemies, dt):
        self.x += self.vel
        self.rect.x = self.x
        print('v', self.vel*dt)
        print('x', self.rect.x)
        if (self.screen_x < self.rect.x):
            enemies.remove(self)
            self.reduce_lives()
