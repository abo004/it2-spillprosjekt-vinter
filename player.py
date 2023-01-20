import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def rotate_to_angle(self, angle):
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def point_at(self, x, y):
        direction = pygame.math.Vector2(x, y) - self.rect.center
        angle = direction.angle_to((0, -1))
        self.rotate_to_angle(angle)
