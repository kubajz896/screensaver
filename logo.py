import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Custom Logo')

# Load logo image
logo_image = pygame.image.load('logoS.png')
logo_rect = logo_image.get_rect('logoS.png')

# Set up logo initial position and speed
logo_rect.centerx, logo_rect.centery = screen_width // 2, screen_height // 2
logo_speed_x, logo_speed_y = 2, 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update logo position
    logo_rect.x += logo_speed_x
    logo_rect.y += logo_speed_y

    # Bounce off the walls
    if logo_rect.left < 0 or logo_rect.right > screen_width:
        logo_speed_x = -logo_speed_x
    if logo_rect.top < 0 or logo_rect.bottom > screen_height:
        logo_speed_y = -logo_speed_y

  # Fill the screen with a background color (change the color here)
    screen.fill((0, 0, 0))  # Change (0, 0, 0) to the RGB values of your desired color


    # Draw the logo image
    screen.blit(logo_image, logo_rect)

    # Update display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
