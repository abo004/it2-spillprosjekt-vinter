import pygame


class Explosion:
    def __init__(self, pos, start_radius):
        self.start_time = 0.5
        self.time = self.start_time
        self.x, self.y = pos
        self.start_radius = start_radius
        self.radius = start_radius

    def update(self, explosions, dt):
        if (self.time < 0):
            explosions.remove(self)
            return

        self.time -= dt
        self.radius = (self.time/self.start_time) * self.start_radius

    def draw(self, screen):
        pygame.draw.line(screen, (255, 100, 0),
                         (self.x+0, self.y-13), (self.x+0, self.y+13), 2)
        pygame.draw.line(screen, (255, 100, 0),
                         (self.x-13, self.y+0), (self.x+13, self.y-0), 2)
        pygame.draw.line(screen, (255, 255, 0),
                         (self.x-11, self.y-11), (self.x+11, self.y+11), 2)
        pygame.draw.line(screen, (255, 255, 0),
                         (self.x-11, self.y+11), (self.x+11, self.y-11), 2)

        pygame.draw.circle(screen, (255, 0, 0),
                           (self.x, self.y), self.radius, 2)
