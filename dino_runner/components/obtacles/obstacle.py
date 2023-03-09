from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH
class Obstacle(Sprite):
    def __init(self, image, type):
          self.image = image
          selftype = type
          self.rect = self.image[self.type].get_rect()
          self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
         self.rect.x -= game_speed

         if self.rect.x < -100:
              obstacles.pop()

    def draw(self, screen):
         screen.blit(self.image[self.type], self.rect)
          

        
