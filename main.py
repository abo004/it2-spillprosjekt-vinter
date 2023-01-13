import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Aim Game")

# Create a box class
class Box:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def collides_with_point(self, x, y):
        if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
            return True
        else:
            return False

# Create a list to store the boxes
boxes = []

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            x, y = pygame.mouse.get_pos()
            # Check if the mouse collides with any boxes
            for box in boxes:
                if box.collides_with_point(x, y):
                    boxes.remove(box)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the boxes
    for box in boxes:
        box.draw(screen)

    # Update the display
    pygame.display.update()

    # Generate a new box
    if len(boxes) < 3 and random.randint(0, 100) < 10:
        x = random.randint(0, 800 - 60)
        y = random.randint(0, 600 - 60)
        width = random.randint(10, 100)
        height = random.randint(10, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        boxes.append(Box(x, y, width, height, color))

# Close Pygame
pygame.quit()
