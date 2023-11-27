import pygame
from pygame.sprite import Sprite
from settings import *

class Player(Sprite):
    def __init__(self, main):

        # Inherit Sprite
        super().__init__()

        # Get screen details
        self.screen   = main.screen
        self.scr_rect = main.screen.get_rect()

        # Set player sprite
        self.image = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect  = self.image.get_rect()

        # Position player spawnpoint
        self.rect.midbottom = self.scr_rect.midbottom

        # Store position of player
        self.x = float(self.rect.x)

        # Set movement check
        self.moveRight = False
        self.moveLeft  = False
    
    # Function to put player sprite into screen
    def spawn(self):
        self.screen.blit(self.image, self.rect)
    
    def respawn(self):
        self.rect.midbottom = self.scr_rect.midbottom
        self.x = float(self.rect.x)
    
    def update(self):
        if self.moveRight and self.rect.right < self.scr_rect.right: self.x += PLAYER_SPEED
        if self.moveLeft and self.rect.left > self.scr_rect.left   : self.x -= PLAYER_SPEED
        self.rect.x = self.x

class Bullet(Sprite):
    def __init__(self, main):

        # Inherit Sprite
        super().__init__()

        # Get screen
        self.screen = main.screen
        
        # Set bullet simension and position
        self.rect = pygame.Rect(0, 0, *BULLET_SIZE)
        self.rect.midtop = main.player.rect.midtop

        # Store bullet position
        self.y = float(self.rect.y)

    # Make bullet appear
    def spawn(self):
        pygame.draw.rect(self.screen, BULLET_COLOR, self.rect)
    
    # Make bullet move
    def update(self):
        self.y -= BULLET_SPEED
        self.rect.y = self.y