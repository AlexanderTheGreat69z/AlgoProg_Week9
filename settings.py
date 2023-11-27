import pygame
pygame.mixer.init()

# Screen Details
SCREEN_WIDTH  = 1200
SCREEN_HEIGHT = 800
BG_COLOR      = (100,100,255)

# Player Details
PLAYER_IMAGE  = pygame.image.load('assets/player.png')
PLAYER_HEALTH = 3
PLAYER_SIZE   = 100
PLAYER_SPEED  = 10

# Bullet Details
BULLET_SFX    = pygame.mixer.Sound('assets/bullet.mp3')
BULLET_SIZE   = (10, 30)
BULLET_SPEED  = 30
BULLET_COLOR  = (255,0,0)
BULLET_MAX    = 3

# Enemy Details
ENEMY_IMAGE   = pygame.image.load('assets/enemy.png')
ENEMY_SFX     = pygame.mixer.Sound('assets/enemyHit.mp3')
ENEMY_SIZE    = 75
ENEMY_SPEED   = 10
enemy_drop    = 10
enemy_dir     = 1