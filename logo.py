import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bouncing Logo')

# Load logo image
logo = pygame.image.load('logoS.png')  # Replace with the path to your logo image
logo_rect = logo.get_rect()

# Set initial position and speed
x, y = 100, 100
speed_x, speed_y = 5, 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update logo position
    x += speed_x
    y += speed_y

    # Bounce off the walls
    if x <= 0 or x + logo_rect.width >= width:
        speed_x = -speed_x
    if y <= 0 or y + logo_rect.height >= height:
        speed_y = -speed_y

    # Draw background and logo
    screen.fill((0, 0, 0))
    screen.blit(logo, (x, y))

    # Update display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(30)
