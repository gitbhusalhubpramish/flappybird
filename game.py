from char import Bird,pipe
import pygame
class game:
  def __init__(self, screen):
    self.bird = Bird()
    self.pipes = [pipe()]
    self.score = 0
    self.game_over = False
    self.gravity = 1.5
    self.jump_strength = -60
    self.screen = screen
    self.clock = pygame.time.Clock()
    self.prevy = self.bird.y
  def run(self, jump):
    # Limit frame rate first
    dt = self.clock.tick(60)
    
    if not self.game_over:
      # Apply physics
      if jump:
        self.prevy = self.bird.y
        self.bird.y += self.jump_strength
      else:
        self.prevy = self.bird.y
        self.bird.y += self.gravity
      
      # Update pipes
      for pp in self.pipes:
        pp.update()
        
        
    
    # Render everything
    self.screen.fill((135, 206, 235))  # Sky blue background
    self.bird.update()
    self.bird.draw(self.screen, self.prevy)
    
    for pp in self.pipes:
      if pp.x < -pp.top_img.get_width():
        self.pipes.remove(pp)
      if pp.x == 250:
        self.pipes.append(pipe())
      pp.draw(self.screen)
    
    pygame.display.flip()