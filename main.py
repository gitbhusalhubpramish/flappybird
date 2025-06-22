import pygame
import platform
import os
from game import game


# Remove the dummy video driver to allow VNC display
if platform.system() == "Linux":
    os.environ['SDL_VIDEODRIVER'] = 'x11'

pygame.init()
pygame.display.set_caption('Flappy Bird')
screen = pygame.display.set_mode((600, 400))
game = game(screen)

running = True
while running:
    jump = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
            jump = True
    
    game.run(jump)

pygame.quit()
