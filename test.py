import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))

# Load the sprites
sprites = []
for i in range(5):
    sprites.append(pygame.image.load(f"xwing{i}.jpg"))

# Create a list to store the positions of the sprites
positions = []
for i in range(5):
    positions.append([0, 0])

# Create a list to store the velocities of the sprites
velocities = []
for i in range(5):
    velocities.append([1, 1])

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update the positions of the sprites
    for i in range(5):
        # move the sprite 10 times slower
        positions[i][0] += velocities[i][0]/10
        positions[i][1] += velocities[i][1]/10

        # check if sprite is out of the screen
        if positions[i][0] > 800 or positions[i][0] < 0 or positions[i][1] > 600 or positions[i][1] < 0:
            sprites[i] = None
            positions[i] = None
            velocities[i] = None

    # Draw the sprites on the screen
    for i in range(5):
        if sprites[i]:
            screen.blit(sprites[i], positions[i])

    # Update the screen
    pygame.display.flip()

# Clean up
pygame.quit()
