
import time
import pygame


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.last_bullet_time = time.time()
        

    def update (self, game, enemy_manager):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                game.scoremanager.deathCount()
                game.menu.actualscreen = True
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
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
            