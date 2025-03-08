import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("PowerPong")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with a color (e.g., black)
    window.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()