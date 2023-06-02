import random

from dino_runner.utils.constants import ENEMY_4_BIRD, ENEMY_5_BIRD
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    BIRD = [
        ENEMY_4_BIRD,
        ENEMY_5_BIRD
    ]
    def __init__(self):
        image = self.BIRD[random.randint(0, 1)]
        super().__init__(image)
        self.rect.y = random.randrange(185, 205)