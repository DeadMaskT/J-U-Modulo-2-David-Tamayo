import random

import pygame
from game.components.power_ups.heart_power_up import HeartPowerUp
from game.components.power_ups.shield import Shield

from game.utils.constants import HEART_TYPE, SHIELD_TYPE, SPACESHIP_SHIELD


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(2000, 5000)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generete_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up):
                if power_up.type == SHIELD_TYPE:
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (
                        self.duration * 1000
                    )
                    game.player.set_img((95, 75), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)
                if power_up.type == HEART_TYPE:
                    game.player.power_up_type = power_up.type
                    game.num_hearts += 1
                    self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generete_power_up(self):
        power_up = [Shield(), HeartPowerUp()]
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up[random.randint(0, 1)])
