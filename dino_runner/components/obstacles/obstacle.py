import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image):
        self.image = image
        if type(self.image) == list:
            self.rect = self.image[0].get_rect()
            self.mask = pygame.mask.from_surface(self.image[0])
        else:
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0


    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        if type(self.image) == list:
            screen.blit(self.image[self.step_index // 5], self.rect)
            self.step_index += 1

            if self.step_index >= len(self.image) * 5 - 1:
                self.step_index = 0
        
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))