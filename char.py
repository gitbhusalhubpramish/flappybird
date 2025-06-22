import pygame
import random

class Bird:
    def __init__(self):
        self.sprite_sheet = pygame.image.load('./image/bird.png').convert_alpha()
        self.frame_width = 92
        self.frame_height = 64
        self.total_frames = 3
        self.current_frame = 0
        self.frame_duration = 100  # milliseconds per frame
        self.last_update = pygame.time.get_ticks()

        self.x = 100
        self.y = 200

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.total_frames
            self.last_update = now

    def draw(self, screen):
        frame_rect = pygame.Rect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
        frame = self.sprite_sheet.subsurface(frame_rect)
        frame = pygame.transform.scale(frame, (30, 20)) 
        screen.blit(frame, (self.x, self.y))



class pipe:
    def __init__(self):
        self.imgraw = pygame.image.load('./image/pipe.png').convert_alpha()
        self.x = 600
        self.gap = 150
        self.speed = 5
        self.top_height = random.randint(50, 300)

        self.top_img = pygame.transform.flip(self.imgraw, False, True)
        self.bottom_img = self.imgraw

        self.top_y = self.top_height - self.top_img.get_height()
        self.bottom_y = self.top_height + self.gap
    def update(self):
        self.x -= self.speed
    def draw(self, screen):
        screen.blit(self.top_img, (self.x, self.top_y))
        screen.blit(self.bottom_img, (self.x, self.bottom_y))
        