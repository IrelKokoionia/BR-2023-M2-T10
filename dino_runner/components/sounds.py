import pygame
from dino_runner.utils.constants import MARIO_SOUNDS


class Sounds:
    def __init__(self):
        pygame.mixer.init()

    def play_background_sound(self):
        self.music = pygame.mixer.music.load(MARIO_SOUNDS["background"])
        pygame.mixer.music.set_volume(0.1)

        pygame.mixer.music.play(-1)
        

    def play_sound(self, type):
        sound = pygame.mixer.Sound(MARIO_SOUNDS[type.lower()])
        sound.set_volume(0.2)
        sound.play()