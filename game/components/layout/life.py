import pygame

from pygame.sprite import Sprite

from game.utils.constants import HEART, HEART_HEIGHT, HEART_WIDTH, VOID_HEART


class Life(Sprite):
    X_POS = HEART_WIDTH + 10
    Y_POS = 10

    def __init__(self, x_pos=X_POS, y_pos=Y_POS):
        self.img = HEART
        self.heart_width = HEART_WIDTH
        self.heart_height = HEART_HEIGHT
        self.img = pygame.transform.scale(
            self.img, (self.heart_width, self.heart_height)
        )
        self.rect = self.img.get_rect()
        self.rect.x = x_pos - self.heart_width
        self.rect.y = y_pos
        

    def update(self):
        pass

    def draw(self, screen,game):
        self.rect.x = self.X_POS
        for heart in range(game.num_hearts):
            screen.blit(self.img, (self.rect.x, self.rect.y))
            self.rect.x += 25

    def set_img(self, image=HEART, size=(HEART_WIDTH, HEART_HEIGHT)):
        self.img = image
        self.img = pygame.transform.scale(self.img, (size))
