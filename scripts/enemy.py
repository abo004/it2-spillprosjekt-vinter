import random
from sprite import Sprite


class Enemy(Sprite):
    def __init__(self, sprite, vel, screen_x, screen_y, reduce_lives, scale):
        super().__init__(*sprite)
        self.scale_to(scale)

        self.x = -self.rect.width*(random.random()*10+1)
        self.y = random.randint(0, screen_y-self.rect.height)

        self.rect.x = self.x
        self.rect.y = self.y

        self.vel = vel
        self.screen_x = screen_x
        self.screen_y = screen_y

        self.reduce_lives = reduce_lives

    def update(self, enemies, dt):
        self.x += self.vel * dt
        self.rect.x = self.x
        if (self.screen_x < self.rect.x):
            enemies.remove(self)
            self.reduce_lives()
