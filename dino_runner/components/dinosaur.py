import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD, HAMMER_TYPE, RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER
from dino_runner.components.power_ups.hammer import HammerManager

X_POS = 80
Y_POS = 250
Y_POS_DUCK = 265
JUMP_VEL = 8.0

DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}


class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 310
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.hammer_manager = HammerManager()
        self.setup_state()
    
    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.hammer = False
        self.show_text = False
        self.has_hammer = False
        self.power_up_time = 0
    
    def update(self, user_input, game_speed, obstacles, music):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump(music)
        elif self.dino_duck:
            self.duck()
        
        if self.has_hammer:
            self.has_hammer = self.hammer_manager.update(game_speed, obstacles)
        
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False   
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True    
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
        
        if user_input[pygame.K_SPACE] and not self.has_hammer and self.hammer:
            self.has_hammer = self.hammer_manager.generate_hammer(self.rect.x, self.rect.y)
            
        if self.step_index >= 9:
            self.step_index = 0
        
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = X_POS
        self.rect.y = Y_POS 
        self.step_index += 1
    
    def jump(self, music):
        self.image = JUMP_IMG[self.type]
        if self.jump_vel == JUMP_VEL:
            music.play_sound("jump")
        self.mask = pygame.mask.from_surface(self.image)
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL
    def duck(self):
        self.image = DUCK_IMG[self.type]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = X_POS
        self.rect.y = Y_POS_DUCK
        self.step_index += 1
        self.dino_duck = False   
            
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.has_hammer:
            self.hammer_manager.draw(screen)
