import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3

class Cactus(Obstacle):

    CACTUS = [
        (ENEMY_1, 235),
        (ENEMY_2, 235),
        (ENEMY_3, 245)
    ]

    def __init__(self):
        image, cactus_pos = self.CACTUS[random.randint(0, 2)]
        super().__init__(image)
        self.rect.y = cactus_pos