import pygame

from pygame.sprite import Sprite

from game.utils.constants import (
    SPACESHIP,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SPACESHIP_HEIGHT,
    SPACESHIP_WIDTH,
)


class Spaceship(Sprite):
    SPACESHIP_SPEED = 10

    def __init__(self):
        self.img = SPACESHIP
        self.spaceship_width = SPACESHIP_WIDTH
        self.spaceship_height = SPACESHIP_HEIGHT
        self.img = pygame.transform.scale(
            self.img, (self.spaceship_width, self.spaceship_height)
        )
        self.rect = self.img.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) - self.spaceship_width
        self.rect.y = 500

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()

        if user_input[pygame.K_RIGHT]:
            self.move_right()

        if user_input[pygame.K_UP]:
            self.move_up()

        if user_input[pygame.K_DOWN]:
            self.move_down()

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))

    def move_left(self):
        if self.rect.x < -10:
            self.rect.x = 1080

        self.rect.x -= self.SPACESHIP_SPEED

    def move_right(self):
        if self.rect.x > 1070:
            self.rect.x = -9

        self.rect.x += self.SPACESHIP_SPEED

    def move_up(self):
        if self.rect.y == 0:
            return

        self.rect.y -= self.SPACESHIP_SPEED

    def move_down(self):
        if self.rect.y == 540:
            return

        self.rect.y += self.SPACESHIP_SPEED
