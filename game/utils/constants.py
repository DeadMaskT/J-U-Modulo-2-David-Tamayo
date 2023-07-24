import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Other/shield.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, "Other/Track.png"))
BG_END = pygame.image.load(os.path.join(IMG_DIR, "Other/bg_end.jpg"))

BTN_RESET = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))
GAME_OVER_WIDTH = 500
GAME_OVER_HEIGHT = 200


HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/heart.png"))
VOID_HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/void_heart.png"))
HEART_WIDTH = 50
HEART_HEIGHT = 40

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HEART_TYPE = "Heart"

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png")
)
SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 60
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_WIDTH = 40
ENEMY_HEIGHT = 60

FONT_STYLE = "freesansbold.ttf"
