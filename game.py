from char import Bird,pipe
import pygame
class game:
  def __init__(self, screen):
    self.bird = Bird()
    self.pipes = [pipe()]
    self.score = 0
    self.game_over = False
    self.gravity = 0.5
    self.jump_strength = -10
    self.screen = screen
    self.clock = pygame.time.Clock()
  def run(self, jump):
    # Limit frame rate first
    dt = self.clock.tick(60)
    
    if not self.game_over:
      # Apply physics
      if jump:
        self.bird.y += self.jump_strength
      else:
        self.bird.y += self.gravity
      
      # Update pipes
      for pp in self.pipes:
        pp.update()
    
    # Render everything
    self.screen.fill((135, 206, 235))  # Sky blue background
    self.bird.update()
    self.bird.draw(self.screen)
    
    for pp in self.pipes:
      pp.draw(self.screen)
    
    pygame.display.flip()