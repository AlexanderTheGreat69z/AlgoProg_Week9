import pygame, sys
from settings import *
from player import Player, Bullet
from enemy import Enemy
from stats import Stats
from time import sleep
pygame.init()

#Set window title
pygame.display.set_caption("Pew Pew Bang Bang")

class main:
    def __init__(self):

        # Game values
        self.screen   = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock    = pygame.time.Clock()

        # Game Objects
        self.player  = Player(self)
        self.stats   = Stats()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Other Attributes
        self.game_active = True
        self._generateRow()
    
    ########################### | INPUT EVENTS | ###########################

    # Check for input events
    def _events(self):
        for e in pygame.event.get():

            # On window exit
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # On key press
            if e.type == pygame.KEYDOWN: self._keydown(e)
            # On key release
            elif e.type == pygame.KEYUP: self._keyup(e)
            # On Left click
            if e.type == pygame.MOUSEBUTTONDOWN: self._fire()
    
    def _keydown(self, e):
        # Close game on Esc key pressed
        if e.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        # Move right on 'D' pressed
        if e.key == pygame.K_d:
            self.player.moveRight = True
        # Move left on 'A' pressed
        if e.key == pygame.K_a:
            self.player.moveLeft = True
    
    def _keyup(self, e):
        # Stop right on 'D' released
        if e.key == pygame.K_d:
            self.player.moveRight = False
        # Stop left on 'A' released
        if e.key == pygame.K_a:
            self.player.moveLeft = False

    ########################### | BULLET FUNCTIONS | ###########################
    def _fire(self):
        if len(self.bullets) < BULLET_MAX:
            BULLET_SFX.play()
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _updateBullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy(): 
            if bullet.rect.bottom <= 0: self.bullets.remove(bullet)
        self._bulletHit()
    
    def _bulletHit(self):
        collide = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if collide: 
            ENEMY_SFX.play()
        if not self.enemies: 
            self.bullets.empty()
            self._generateRow()
    
    ########################### | ENEMY FUNCTIONS | ###########################
    def _createEnemy(self, x, y):
        new_enemy = Enemy(self)
        new_enemy.x = x

        new_enemy.rect.x = x
        new_enemy.rect.y = y
        self.enemies.add(new_enemy)

    def _generateRow(self):
        enemy = Enemy(self)
        # self.enemies.add(enemy)
        enemy_width, enemy_height = enemy.rect.size
        current_x, current_y = enemy_width, enemy_height

        while current_y < (SCREEN_HEIGHT - 3*enemy_height):
            while current_x < (SCREEN_WIDTH - 2*enemy_width):
                self._createEnemy(current_x, current_y)
                current_x += 2*enemy_width
            current_x = enemy_width
            current_y += 2*enemy_height

    def _checkRowEdge(self):
        for enemy in self.enemies.sprites():
            if enemy.check():
                self._changeRowDir(enemy_dir)
                break
    
    def _checkBottom(self):
        for enemy in self.enemies.sprites():
            if enemy.rect.bottom >= SCREEN_HEIGHT:
                self._playerHit()
                break
            
    def _changeRowDir(self, dir):
        for enemy in self.enemies.sprites():
            enemy.rect.y += enemy_drop
        dir = dir * -1

    def _playerHit(self):

        if self.stats.remainingLives > 0:

            # Decrease lives
            self.stats.remainingLives -= 1

            # Remove remaining entities
            self.bullets.empty()
            self.enemies.empty()

            # Regenerate row and re-center player
            self._generateRow()
            self.player.respawn()

            # Pause
            sleep(0.5)

        else: self.game_active = False

    def _updateEnemy(self):
        self._checkRowEdge()
        self.enemies.update()
        if pygame.sprite.spritecollideany(self.player, self.enemies): self._playerHit()
        self._checkBottom()

    ########################### | UPDATE | ###########################

    # Screen update function
    def _update(self):

        # Fill background with color
        self.screen.fill(BG_COLOR)

        # Spawn Player
        self.player.spawn()

        # Spawn Bullet
        for bullet in self.bullets.sprites(): bullet.spawn()
        print(len(self.bullets))

        # Spawn enemies
        self.enemies.draw(self.screen)

        # Update Frames
        pygame.display.flip()
        pygame.display.update()

    # Game Execution
    def run(self):
        while True:
            self._events()
            if self.game_active:
                self.player.update()
                self._updateBullets()
                #self._updateEnemy()
            self._update()
            print(self.stats.remainingLives)
            
            # Set framerate
            self.clock.tick(60)

# Start the Game
if __name__ == "__main__": main().run()