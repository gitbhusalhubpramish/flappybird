from char import Bird,pipe
import pygame
class game:
  def __init__(self, screen):
    self.bird = Bird()
    self.pipes = [pipe()]
    self.score = 0
    self.game_over = False
    self.gravity = 1.59
    self.jump_strength = -60
    self.screen = screen
    self.clock = pygame.time.Clock()
    self.prevy = None
    self.restart = pygame.image.load('./image/restart.png').convert_alpha()
    self.ovrscr = pygame.image.load('./image/score.png').convert_alpha()
    self.best = 0
    self.score = 0
    self.score_text = pygame.font.SysFont('Arial', 50).render(str(self.score), True, (0, 0, 0))
    # self.restart = pygame.transform.scale(self.restart, (50, 50))
  def run(self, jump):
    # Limit frame rate first
    dt = self.clock.tick(60)
    
    if not self.game_over:
      # Apply physics
      if jump:
        self.prevy = self.bird.y
        self.bird.y += self.jump_strength
      else:
        self.bird.y += self.gravity
      
      # Update pipes
      for pp in self.pipes:
        pp.update()
        
    else:
      self.gameover()
        
    # Render everything
    self.screen.fill((135, 206, 235))  # Sky blue background
    self.bird.update()
    self.bird.draw(self.screen, self.prevy, self.game_over)
    
    for pp in self.pipes:
      if pp.x < -pp.top_img.get_width():
        self.pipes.remove(pp)
      if pp.x == 250:
        self.pipes.append(pipe())
      pp.draw(self.screen)
      # Check for collisions
      if self.bird.x + 50 > pp.x and self.bird.x < pp.x + 50:
        if self.bird.y < pp.top_height or self.bird.y + 35 > pp.bottom_y:
          self.game_over = True
      if self.bird.y > 600-self.bird.frame_height:
        self.game_over = True
      if pp.x == self.bird.x:
        self.score += 1
    self.score_text = pygame.font.SysFont('Arial', 50).render(str(self.score), True, (0, 0, 0))
    self.screen.blit(self.score_text, (0, 0))
    
    pygame.display.flip()

  def gameover(self):
    while self.bird.y < 600-self.bird.frame_height:
      self.bird.y += self.gravity * 1.5
      self.screen.fill((135, 206, 235))  # Sky blue background
      self.bird.update()
      for pp in self.pipes:
        pp.draw(self.screen)
      self.bird.draw(self.screen, self.prevy, self.game_over)
      pygame.display.flip()
    self.screen.blit(self.ovrscr, (250, 20))
    self.best = max(self.best, self.score)
    best_text = pygame.font.SysFont('Arial', 50).render(str(self.best), True, (0, 0, 0))
    self.screen.blit(self.score_text, (325, 70))
    self.screen.blit(best_text, (325, 150))
    game_over_text = pygame.font.SysFont('Arial', 50).render('Game Over', True, (0, 0, 0))
    self.screen.blit(game_over_text, (200, 250))
    self.screen.blit(self.restart,(230, 350))
    pygame.display.flip()
  def restartgame(self):
    self.bird = Bird()
    self.pipes = [pipe()]
    self.score = 0
    self.game_over = False