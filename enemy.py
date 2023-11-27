import pygame
from settings import *
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, main):

        # Inherit Sprite
        super().__init__()

        # Get game screen
        self.screen = main.screen

        # Set enemy image and sprite
        self.image = pygame.transform.scale(ENEMY_IMAGE, (ENEMY_SIZE, ENEMY_SIZE))
        self.rect  = self.image.get_rect()

        # Set enemy spawnpoint
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store enemy x pos
        self.x = float(self.rect.x)
    
    def update(self):
        self.x += ENEMY_SPEED * enemy_dir
        self.rect.x = self.x

    def check(self):
        scr_rect = self.screen.get_rect()
        return (self.rect.right >= scr_rect.right) or (self.rect.left <= 0)