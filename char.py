import pygame

class Bird:
    def __init__(self):
        self.img = pygame.Surface((34, 24), pygame.SRCALPHA)
        pygame.draw.ellipse(self.img, (255, 255, 0), [0, 0, 34, 24])
        self.img = pygame.transform.scale(self.img, (30, 30))
        self.x = 100
        self.y = 200

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))