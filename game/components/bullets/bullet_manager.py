
import time
import pygame
from game.components.explosion import Explosion


from game.utils.constants import SHIELD_TYPE, SOUND_EXPLOSION_PLAYER


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.last_bullet_time = time.time()
        

    def update (self, game, enemy_manager):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                if game.player.power_up_type != SHIELD_TYPE:
                    explode = Explosion(game.player.rect.center)
                    game.all_sprites.add(explode)
                    game.player.hide()
                    game.player.lives -= 1
                    sound_explosion_player= pygame.mixer.Sound(SOUND_EXPLOSION_PLAYER)
                    pygame.mixer.Sound.play(sound_explosion_player)
                    if game.player.lives == 0:
                        game.scoremanager.deathCount()
                        game.player.lives = 3
                        game.menu.actualscreen = True
                        game.playing = False
                        pygame.time.delay(2000)
                        break
                


        
        for bullet in self.bullets:
            bullet.update(self.bullets)
            delete=enemy_manager.destroy_enemy(bullet,game)
            if delete:
                self.bullets.remove(bullet)

    def draw (self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy':
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' :
            self.bullets.append(bullet)
            self.last_bullet_time = time.time()

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
            