import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class Cactus(Obstacle):

    CACTUS = [
        (SMALL_CACTUS, 325),
        (LARGE_CACTUS, 300)
    ]

    def __init__(self):
        image, cactus_pos = self.CACTUS[random.randint(0, 1)]
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = cactus_pos