import pygame

from game.utils.constants import SHIELD_TYPE


class Bullets_manager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []

    def update(self, game):
        for bullet_player in self.bullets:
            bullet_player.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if (
                    bullet_player.rect.colliderect(enemy.rect)
                    and bullet_player.owner == "player"
                ):
                    self.bullets.remove(bullet_player)
                    game.enemy_manager.enemies.remove(enemy)
                    game.score += 100

        for bullet_enemy in self.enemy_bullets:
            bullet_enemy.update(self.enemy_bullets)
            if (
                bullet_enemy.rect.colliderect(game.player.rect)
                and bullet_enemy.owner == "enemy"
            ):
                self.enemy_bullets.remove(bullet_enemy)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.num_hearts -= 1
                    if game.num_hearts == 0:
                        game.playing = False
                        game.death_score += 1
                        pygame.time.delay(1000)
                        break

    def draw(self, screen):
        for bullet_enemy in self.enemy_bullets:
            bullet_enemy.draw(screen)

        for bullet_player in self.bullets:
            bullet_player.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == "enemy" and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)

        if bullet.owner == "player" and len(self.bullets) < 3:
            self.bullets.append(bullet)
