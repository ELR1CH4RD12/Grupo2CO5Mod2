import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import  SHIELD, SHIELD_TYPE


class Shield(PowerUp):
    def __init__(self):
        self.size = (40, 40)
        self.image = pygame.transform.scale(SHIELD, self.size)
        super().__init__(self.image, SHIELD_TYPE)