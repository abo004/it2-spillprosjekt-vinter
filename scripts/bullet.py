import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image_file, starting_pos, end_pos, vel):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width()//2, self.image.get_height()//2))

        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.angle = angle
        self.vel = vel

    def update(self, dt):
        self.rect.x += self.vel * dt * math.cos(self.angle)
        self.rect.y += self.vel * dt * math.sin(self.angle)

        if self.rect.x < 0 or self.rect.x > 800 or self.rect.y < 0 or self.rect.y > 600:
            self.kill()