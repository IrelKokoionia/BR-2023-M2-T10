import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

        
    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird(),
        ]
        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,1)])
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if pygame.sprite.collide_mask(game.player, obstacle):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break             

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    def reset_obstacles(self):
        self.obstacles = []