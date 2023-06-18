import random
import time

import pygame
from game.components.enemies.enemy import Enemy
from game.components.explosion import Explosion
from game.utils.constants import SOUND_EXPLOSION



class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.last_enemy_time = time.time()

    def update(self,game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies,game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1 or time.time() - self.last_enemy_time >= 2:
            self.SPEED_Y = random.randint(1,5)
            self.SPEED_X = random.randint(1,8)
            enemy = Enemy(self.SPEED_Y,self.SPEED_X)
            self.enemies.append(enemy)
            self.last_enemy_time = time.time()

    def destroy_enemy(self, bullet,game):
        for enemy in  self.enemies:
            # implementar explosion 
            if enemy.rect.colliderect(bullet.rect):
                self.enemies.remove(enemy)
                expl = Explosion(enemy.rect.center)
                game.all_sprites.add(expl)
                sound_explosion= pygame.mixer.Sound(SOUND_EXPLOSION)
                pygame.mixer.Sound.play(sound_explosion)
                score = game.scoremanager.update_score()
                game.scoremanager.scorelist(score)
                return True
            
    def reset(self):
        self.enemies = []

