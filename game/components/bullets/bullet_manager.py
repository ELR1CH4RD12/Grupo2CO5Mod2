
import time
import pygame


from game.utils.constants import SHIELD_TYPE, SOUND_EXPLOSION_PLAYER


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.last_bullet_time = time.time()
        

    def update (self, game, enemy_manager):
        for enemy in enemy_manager.enemies:
            if enemy.rect.colliderect(game.player.rect):
                sound_explosion_player= pygame.mixer.Sound(SOUND_EXPLOSION_PLAYER)
                pygame.mixer.Sound.play(sound_explosion_player)
                game.scoremanager.deathCount()
                game.menu.actualscreen = True
                game.playing = False
                pygame.time.delay(2000)
                break
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                if game.player.power_up_type != SHIELD_TYPE:
                    game.scoremanager.deathCount()
                    game.menu.actualscreen = True
                    sound_explosion_player= pygame.mixer.Sound(SOUND_EXPLOSION_PLAYER)
                    pygame.mixer.Sound.play(sound_explosion_player)
                    game.playing = False
                    pygame.time.delay(2000)
                    break
                self.enemy_bullets.remove(bullet)
            else:
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
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' :
            self.bullets.append(bullet)
            self.last_bullet_time = time.time()

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
            