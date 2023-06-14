import random
import time
from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.last_enemy_time = time.time()

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)

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

