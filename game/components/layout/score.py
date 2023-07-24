import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Score:
    Y_POS = 10
    X_POS = SCREEN_WIDTH // 2

    def __init__(self, counter=0, x_pos=X_POS, y_pos=Y_POS):
        self.score = str(counter)
        self.font = pygame.font.Font(FONT_STYLE, 50)
        self.text = self.font.render(self.score, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.midtop = (x_pos, y_pos)

    def update(self, counter):
        self.text = self.font.render(str(counter), True, (255, 255, 255))

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
