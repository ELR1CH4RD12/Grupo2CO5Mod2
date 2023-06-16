import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 50)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        self.actualscreen = False
        self.score = 0
        self.highscore = 0
        self.deaths = 0

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw (self, screen ):
        screen.blit(self.text, self.text_rect)
        if self.actualscreen:
            screen.blit(self.score, self.text_rect2)
            screen.blit(self.highscore, self.text_rect3)
            screen.blit(self.deaths, self.text_rect4)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def update_message(self, message):
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH + 20, self.HALF_SCREEN_HEIGHT)


    def show_scores(self, score, highscore, deaths):
        self.score = self.font.render("Your score: " + score, True, (0, 0, 0))
        self.text_rect2 = self.score.get_rect()
        self.text_rect2.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)

        self.highscore = self.font.render("Highest score: " + highscore, True, (0, 0, 0))
        self.text_rect3 = self.highscore.get_rect()
        self.text_rect3.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)

        self.deaths = self.font.render("Total deaths: " + deaths, True, (0, 0, 0))
        self.text_rect4 = self.score.get_rect()
        self.text_rect4.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)