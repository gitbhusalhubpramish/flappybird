import pygame
import platform
import os
from char import Bird

clock = pygame.time.Clock()

# Remove the dummy video driver to allow VNC display
if platform.system() == "Linux":
    os.environ['SDL_VIDEODRIVER'] = 'x11'

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Flappy Bird')

bird = Bird()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 235))  # Sky blue background
    bird.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
