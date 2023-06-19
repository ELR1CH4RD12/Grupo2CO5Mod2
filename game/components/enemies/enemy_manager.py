import random
import time

import pygame
from game.components.enemies.enemy import Enemy
from game.components.explosion import Explosion
from game.utils.constants import SHIELD_TYPE, SOUND_EXPLOSION, SOUND_EXPLOSION_PLAYER



class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.last_enemy_time = time.time()

    def update(self,game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies,game)
            if enemy.rect.colliderect(game.player.rect):
                if game.player.power_up_type != SHIELD_TYPE:
                    game.player.lives -= 1
                    explode = Explosion(enemy.rect.center)
                    game.all_sprites.add(explode)
                    game.enemy_manager.enemies.remove(enemy)
                    explode = Explosion(game.player.rect.center)
                    game.all_sprites.add(explode)
                    game.player.hide()
                    sound_explosion_player= pygame.mixer.Sound(SOUND_EXPLOSION_PLAYER)
                    pygame.mixer.Sound.play(sound_explosion_player)
                    if game.player.lives==0:
                        game.scoremanager.deathCount()
                        game.menu.actualscreen = True
                        game.playing = False
                        pygame.time.delay(2000)
                        break
                else:
                    game.enemy_manager.enemies.remove(enemy)
                    explode = Explosion(enemy.rect.center)
                    game.all_sprites.add(explode)

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

