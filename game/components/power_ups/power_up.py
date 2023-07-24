import random, pygame

from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Power_Up(Sprite):
    SIZE = (40, 40)

    def __init__(self, image, type):
        self.img = image
        self.img = pygame.transform.scale(self.img, self.SIZE)
        self.type = type
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(120, SCREEN_WIDTH - 120)
        self.rect.y = 0
        self.start_time = 0

    def update(self, game_speed, power_ups):
        self.rect.y += game_speed
        if self.rect.y > SCREEN_HEIGHT:
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.img, self.rect)
