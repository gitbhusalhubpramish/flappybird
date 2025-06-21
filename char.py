import pygame

class Bird:
    def __init__(self):
        self.img = pygame.image.load('./image/birdmidwing.webp')
        self.img = pygame.transform.scale(self.img, (30, 30))
        self.x = 100
        self.y = 200

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))