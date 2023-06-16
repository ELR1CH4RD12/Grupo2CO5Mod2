import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.utils.constants import BG, FONT_STYLE,ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import   Spaceship
from game.components.scoreManager import ScoreManager

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
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.scoremanager = ScoreManager()

        self.menu = Menu ('Press Any Key to start...', self.screen)

    def execute (self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                #implementar
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.score = 0
        self.bullet_manager.reset()  #implementar
        self.enemy_manager.reset()
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
        usaer_input = pygame.key.get_pressed()
        self.enemy_manager.update(self)
        self.bullet_manager.update(self,self.enemy_manager)
        self.player.update(usaer_input,self.bullet_manager)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        #pygame.display.flip()

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
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT //2

        self.menu.reset_screen_color(self.screen)

        if self.scoremanager.death_count > 0:
            self.menu.update_message('Game over Prees any key to restart')
            self.menu.show_scores(str(self.scoremanager.score), str(self.scoremanager.highscore()), str(self.scoremanager.death_count))
        self.menu.draw(self.screen)
        icon = pygame.transform.scale (ICON, (80,120))
        self.screen.blit(icon, (half_screen_width - 50, half_screen_height -120))
        
        
        self.menu.update(self)

    def update_score(self):
        self.score += 1

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.scoremanager.score}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (100, 100)
        self.screen.blit(text, text_rect)
