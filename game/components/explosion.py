import pygame
from game.utils.constants import EXPLOSION_ANIM

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.image = EXPLOSION_ANIM[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0 
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60

    def update (self):
        now = pygame.time.get_ticks ()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(EXPLOSION_ANIM):
                self.kill()
            else:
                center = self.rect.center
                self.image = EXPLOSION_ANIM[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center =  center
    
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))

        
