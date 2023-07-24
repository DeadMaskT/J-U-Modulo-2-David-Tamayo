from game.components.layout.life import Life
from game.components.layout.score import Score


class Layout:
    def __init__(self):
        self.heart = Life()
        self.score = Score()

    def update(self, game):
        self.score.update(game.score)

    def draw(self, screen, game):
        self.score.draw(screen)
        self.heart.draw(screen, game)
