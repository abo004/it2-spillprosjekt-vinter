import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, initial_scale=1, pos="center"):
        super().__init__()

        self.image = image
        self.original_image = self.image
        self.initial_scale = initial_scale

        self.scale_to(1)
        self.scaled_image = self.image

        self.rect = self.image.get_rect()

        if (pos == "center"):
            self.rect.center = (x, y)
        else:
            self.rect.topleft = (x, y)

    def scale_to(self, scale):
        self.image = pygame.transform.scale(
            self.original_image, (self.original_image.get_width()*self.initial_scale*scale, self.original_image.get_height()*self.initial_scale*scale))

    def rotate_to(self, angle):
        self.image = pygame.transform.rotate(
            self.scaled_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
