import pygame
from game.utils.constants import (
    FONT_STYLE,
    GAME_OVER,
    GAME_OVER_HEIGHT,
    GAME_OVER_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class GameOver:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self):
        self.img = GAME_OVER
        self.go_width = GAME_OVER_WIDTH
        self.go_height = GAME_OVER_HEIGHT
        self.img = pygame.transform.scale(self.img, (self.go_width, self.go_height))
        self.rect = self.img.get_rect()
        self.rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        self.death_counter = 0
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(str(self.death_counter), True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 40)

    def update(self,game):
        pygame.display.update()
        self.update_death_counter(game.death_score)

    def draw(self, screen):
        screen.blit(self.img, self.rect)
        screen.blit(self.text, self.text_rect)

    def update_death_counter(self, counter):
        self.text = self.font.render(str(counter), True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 40)
