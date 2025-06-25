import pygame
import platform
import os
from game import game


# Remove the dummy video driver to allow VNC display
if platform.system() == "Linux":
    os.environ['SDL_VIDEODRIVER'] = 'x11'

pygame.init()
pygame.display.set_caption('Flappy Bird')
screen = pygame.display.set_mode((600, 600))
game = game(screen)

running = True
start = False
while running:
    jump = False
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
            start=True
            jump = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            btn_x, btn_y = 230, 350
            btn_w, btn_h = game.restart.get_width(), game.restart.get_height()

            if game.game_over and btn_x <= mousex <= btn_x + btn_w and btn_y <= mousey <= btn_y + btn_h:
                game.restartgame()
    if start:
        if not game.game_over:
            game.run(jump)
        else:
            game.gameover()
    else:
        game.screen.fill((135, 206, 235))  # Sky blue background
        game.bird.update()
        game.bird.draw(game.screen, None, False)
        game.screen.blit(game.score_text, (0, 0))
        pygame.display.flip()

pygame.quit()
