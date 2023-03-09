import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS,BIRD,LARGE_CACTUS
from dino_runner.components.obstacles.bird import Bird

class ObtacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self,gane_speed,gane):

      if len(self.obstacles) == 0:
         obstacle_it = random.randint(0,2)
         match type:
          case 0:
           self.obstacles.append(Bird(BIRD))
          case 1:
           self.obstacles.append(Cactus(SMALL_CACTUS))
          case 2:
           self.obstacles.append(Cactus(LARGE_CACTUS))

         for obstacle in self.obstacles:
            obstacle.update(gane_speed, self.obstacles)

            if gane.player.dino_rect.colliderect(obstacle.rect):
                  pygame.time.delay(300)
                  gane.playing = False
                  break
            else:
                 self.obstacles.remove(obstacle)
                 
         def draw(self, screen):
            for obtacle in self.obstacles:
               obstacle.draw(screen)


