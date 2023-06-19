import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEART
class Heart(PowerUp):
    def __init__(self):
        self.size = (40, 40)
        self.image = pygame.transform.scale(HEART, self.size)
        super().__init__(self.image, type="Heart")