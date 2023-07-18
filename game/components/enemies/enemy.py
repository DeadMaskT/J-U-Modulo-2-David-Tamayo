import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet

from game.utils.constants import (
    ENEMY_1,
    ENEMY_2,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SPACESHIP_HEIGHT,
    SPACESHIP_WIDTH,
)


class Enemy(Sprite):
    X_POS = [50, 100, 150, 200, 250, 350, 300, 400, 450, 500, 550, 600, 650, 700, 750]
    Y_POS = 20
    SPEED_Y = 1
    SPEED_X = 5
    MOVE_X = {0: "left", 1: "right"}
    IMG_ENEMY = {0: ENEMY_1, 1: ENEMY_2}

    def __init__(self):
        self.img = self.IMG_ENEMY[random.randint(0, 1)]
        self.enemy_width = SPACESHIP_WIDTH
        self.enemy_height = SPACESHIP_HEIGHT
        self.spaceship_width = SPACESHIP_WIDTH
        self.spaceship_height = SPACESHIP_HEIGHT
        self.img = pygame.transform.scale(
            self.img, (self.spaceship_width, self.spaceship_height)
        )
        self.rect = self.img.get_rect()
        self.rect.x = self.X_POS[random.randint(0, len(self.X_POS) - 1)]
        self.rect.y = self.Y_POS
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X
        self.movement_x = self.MOVE_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.type = "enemy"
        self.index = 0
        self.shooting_time = random.randint(30, 50)

    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        if self.movement_x == "left":
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        self.change_movement()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))

    def change_movement(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == "right") or (
            self.rect.x >= SCREEN_WIDTH - self.spaceship_width
        ):
            self.movement_x_for = random.randint(20, 90)
            self.movement_x = "left"
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == "left") or (
            self.rect.x <= 10
        ):
            self.movement_x_for = random.randint(10, 60)
            self.movement_x = "right"
            self.index = 0

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)
