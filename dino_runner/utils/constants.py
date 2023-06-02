import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants

SOUNDS_DIR = os.path.join(IMG_DIR, "Sounds")

background_2 = os.path.join(SOUNDS_DIR, "Mario/musica_fundo.mp3") 

sound_dead = os.path.join(SOUNDS_DIR, "Dino/sound_dead.wav")  

sound_gameover = os.path.join(SOUNDS_DIR, "Dino/sound_game-over.mp3")  

sound_jump = os.path.join(SOUNDS_DIR, "Mario/mario_jump.wav") 

sound_score = os.path.join(SOUNDS_DIR, "Dino/sound_score.wav")   

sound_start = os.path.join(SOUNDS_DIR, "Mario/sound_start.wav")


MARIO_SOUNDS = {"background": background_2,
                "dead": sound_dead,
                "gameover": sound_gameover,
                "jump": sound_jump,
                "score": sound_score,
                "start": sound_start}

MARIO_SPRITE_SHEET = pygame.image.load(os.path.join(IMG_DIR, 'Mario/Mario_Sheet.png'))

MARIO_RUNNING = []
for i in range(3):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 0), (32, 32))
    MARIO_RUNNING.append(pygame.transform.scale(img, (88, 94)))

img = MARIO_SPRITE_SHEET.subsurface((32 * 3, 0), (32, 32))
MARIO_JUMPING = pygame.transform.scale(img, (88, 94))

img = MARIO_SPRITE_SHEET.subsurface((32 * 4, 0), (32, 32))
MARIO_DUCKING = pygame.transform.scale(img, (88, 94))

#SHIELD MARIO
MARIO_RUNNING_SHIELD = []
for i in range(3):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32), (32, 32))
    MARIO_RUNNING_SHIELD.append(pygame.transform.scale(img, (88, 94)))

img = MARIO_SPRITE_SHEET.subsurface((32 * 3, 32), (32, 32))
MARIO_JUMPING_SHIELD = pygame.transform.scale(img, (88, 94))

img = MARIO_SPRITE_SHEET.subsurface((32 * 4, 32), (32, 32))
MARIO_DUCKING_SHIELD = pygame.transform.scale(img, (88, 94))

#HAMMER MARIO
MARIO_RUNNING_HAMMER = []
for i in range(3):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32 * 2), (32, 32))
    MARIO_RUNNING_HAMMER.append(pygame.transform.scale(img, (88, 94)))

img = MARIO_SPRITE_SHEET.subsurface((32 * 3, 32 * 2), (32, 32))
MARIO_JUMPING_HAMMER = pygame.transform.scale(img, (88, 94))

img = MARIO_SPRITE_SHEET.subsurface((32 * 4, 32 * 2), (32, 32))
MARIO_DUCKING_HAMMER = pygame.transform.scale(img, (88, 94))

#MARIO ENEMIES
img = MARIO_SPRITE_SHEET.subsurface((32 * 0, 32 * 3), (32, 32))
ENEMY_5_BIRD = pygame.transform.scale(img, (88, 94))

ENEMY_1 = []
for i in range(1, 3):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32 * 3), (32, 32))
    ENEMY_1.append(pygame.transform.scale(img, (100, 114)))

ENEMY_2 = []
for i in range(3, 5):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32 * 3), (32, 32))
    ENEMY_2.append(pygame.transform.scale(img, (100, 114)))

ENEMY_3 = []
for i in range(2):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32 * 4), (32, 32))
    ENEMY_3.append(pygame.transform.scale(img, (88, 94)))

ENEMY_4_BIRD = []
for i in range(2, 5):
    img = MARIO_SPRITE_SHEET.subsurface((32 * i, 32 * 4), (32, 32))
    ENEMY_4_BIRD.append(pygame.transform.scale(img, (88, 94)))

RUNNING = MARIO_RUNNING

RUNNING_SHIELD = MARIO_RUNNING_SHIELD

RUNNING_HAMMER = MARIO_RUNNING_HAMMER

JUMPING = MARIO_JUMPING

JUMPING_SHIELD = MARIO_JUMPING_SHIELD

JUMPING_HAMMER = MARIO_JUMPING_HAMMER

DUCKING = MARIO_DUCKING

DUCKING_SHIELD = MARIO_DUCKING_SHIELD

DUCKING_HAMMER = MARIO_DUCKING_HAMMER

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]

LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/sprite_mario_hammer2.png'))

HOURGLASS = pygame.image.load(os.path.join(IMG_DIR, 'Other/Hourglass.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Mario/BackGround.png')) #esse é a linha que aparece onde o dino fica em cima

# ICON = pygame.image.load(os.path.join(IMG_DIR, 'Other/icon.png'))
# ICON_DEATH = pygame.image.load(os.path.join(IMG_DIR, 'Other/icon_death.png'))
ICON = pygame.image.load(os.path.join(IMG_DIR, 'Other/Mario_ICON2.png'))
ICON_DEATH = pygame.image.load(os.path.join(IMG_DIR, 'Other/mario_death.png'))

HAMMER_MARIO = pygame.image.load(os.path.join(IMG_DIR, 'Other/sprite_mario_hammer2.png'))

ICON_MARIO_INICIO = pygame.image.load(os.path.join(IMG_DIR, 'Other/Mario_icon.inicio.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

JUMP_SOUND =  os.path.join(SOUNDS_DIR, "Mario/mario_jump.mp3") 

POWER_UP_SOUNDS = os.path.join(os.path.join(SOUNDS_DIR, "Mario/mario_power-up.mp3"))

START_MARIO_SONDS = os.path.join(SOUNDS_DIR, "Mario/sound_start.mp3")

THEME_MUSIC = os.path.join(SOUNDS_DIR, "Mario/musica_fundo.mp3")

MARIO_SOUNDS = {"background": THEME_MUSIC,
                "jump": JUMP_SOUND,
                "power_up": POWER_UP_SOUNDS,
                "start": START_MARIO_SONDS}

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
HOURGLASS_TYPE = "hourglass"