import pygame
import random
from pygame.sprite import  Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import DEFAULT_TYPE,SCREEN_WIDTH, SOUND_BULLET_PLAYER,SPACESHIP
class Spaceship (Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_HEIGHT
    Y_POS = 500
    SHIP_SPEED = 10
    
    def __init__(self) :
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0

    def update(self,user_input,bullet_manager):
        key_actions = {
            pygame.K_LEFT: self.move_left,
            pygame.K_RIGHT: self.move_right,
            pygame.K_UP: self.move_up,
            pygame.K_DOWN: self.move_down,
            pygame.K_SPACE: lambda: self.shoot(bullet_manager)
        }
        for key, action in key_actions.items():
            if user_input[key]:
                action()

    def move_left(self):
        if self.rect.x > -40:
            self.rect.x -= 10
        else:
            self.rect.x += SCREEN_WIDTH
    def move_right(self):
        if self.rect.x < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x -= SCREEN_WIDTH
    def move_up(self):
        self.rect.y -= self.SHIP_SPEED
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self):
        self.rect.y += self.SHIP_SPEED
        if self.rect.y >= self.Y_POS:
            self.rect.y = self.Y_POS + 40

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)
        sound_explosion_player= pygame.mixer.Sound(SOUND_BULLET_PLAYER)
        pygame.mixer.Sound.play(sound_explosion_player)
        
    def set_image(self, size = (SHIP_WIDTH, SHIP_HEIGHT), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)
        