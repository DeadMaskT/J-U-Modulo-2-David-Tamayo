import pygame


class Bullets_manager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []

    def update(self, game):
        for bullet_player in self.bullets:
            bullet_player.update(self.bullets)
            if (
                bullet_player.rect.colliderect(game.enemy_manager.enemies[0].rect)
                and bullet_player.owner == "player"
            ):
                self.bullets.remove(bullet_player)
                game.enemy_manager.enemies.remove()

        for bullet_enemy in self.enemy_bullets:
            bullet_enemy.update(self.enemy_bullets)
            if (
                bullet_enemy.rect.colliderect(game.player.rect)
                and bullet_enemy.owner == "enemy"
            ):
                self.enemy_bullets.remove(bullet_enemy)
                game.playing = False
                pygame.time.delay(2000)
                break

    def draw(self, screen):
        for bullet_enemy in self.enemy_bullets:
            bullet_enemy.draw(screen)

        for bullet_player in self.bullets:
            bullet_player.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == "enemy" and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)

        if bullet.owner == "player" and len(self.bullets) < 1:
            self.bullets.append(bullet)
