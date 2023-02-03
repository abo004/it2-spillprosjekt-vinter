import pygame
from sprite import Sprite


class Player(Sprite):
    def __init__(self, image_file, x, y):
        super().__init__(image_file, x, y, 0.3, pos="center")

    def point_at(self, x, y):
        direction = pygame.math.Vector2(x, y) - self.rect.center
        angle = direction.angle_to((0, -1))
        self.rotate_to(angle)
