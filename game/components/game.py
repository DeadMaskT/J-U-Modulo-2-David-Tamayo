import pygame
from game.components.bullets.bullets_manager import Bullets_manager
from game.components.enemies.enemy_manager import Enemy_manager
from game.components.game_over import GameOver
from game.components.layout.layout import Layout
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.spaceship import Spaceship

from game.utils.constants import (
    BG,
    BG_END,
    BTN_RESET,
    FONT_STYLE,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    FPS,
    DEFAULT_TYPE,
)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = Enemy_manager()
        self.bullet_manager = Bullets_manager()
        self.power_up_manager = PowerUpManager()
        self.death_score = 0
        self.score = 0
        self.num_hearts = 3
        self.menu = Menu("Press Any Key to start.....", self.screen)
        self.layout = Layout()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        self.menu.update(self)
        self.layout.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.layout.draw(self.screen, self)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)

        if self.num_hearts <= 0:
            self.menu.start = False
            image = pygame.transform.scale(BG_END, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.screen.blit(image, (0, 0))
            self.menu.update_message("estadisticas:")
            self.menu.message(self.screen, "Game Over", 420, 100, 50)
            self.show_score(self.screen)
            self.btn_reset(self.screen)

        self.menu.draw(self.screen)
        self.menu.update(self)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round(
                (self.player.power_time_up - pygame.time.get_ticks()), 2
            )

            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 30)
                text = font.render(
                    f"Time {self.player.power_up_type.capitalize()}: {time_to_show}",
                    True,
                    (255, 255, 255),
                )
                text_rect = text.get_rect()
                text_rect.bottomleft = (10, SCREEN_HEIGHT)
                self.screen.blit(text, text_rect)
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_img()

    def show_score(self, screen):
        self.menu.message(screen, f"Score: {self.score}", 420, 350, 30)
        self.menu.message(screen, f"deads: {self.death_score}", 600, 350, 30)

    def btn_reset(self, screen):
        btn = BTN_RESET
        btn_rect = btn.get_rect()
        btn_rect.x = SCREEN_WIDTH // 2
        btn_rect.y = 450
        screen.blit(btn, (btn_rect.x, btn_rect.y))

        mouse = pygame.mouse.get_pos()
        if btn_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] == 1:
            self.reset_game()
            self.run()

    def reset_game(self):
        self.enemy_manager.enemies.pop()
        self.score = 0
        self.num_hearts = 3
 