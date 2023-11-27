import pygame.font
from pygame.sprite import Group
from player import Player
from settings import *

class Scoreboard:
    def __init__(self, main):
        self.main = main
        self.screen = main.screen
        self.scr_rect = self.screen.get_rect()
        self.stats = main.stats

        self.color = (255,0,0)
        self.font = pygame.font.SysFont(None, 48)

        self.setScore()
        self.setHighscore()
        self.setLevel()
        self.setShips()

    def setScore(self):
        score = self.stats.score
        score_text = f'Score: {score:,}'
        self.score_img = self.font.render(score_text, True, self.color, BG_COLOR)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.scr_rect.right - 20
        self.score_rect.top = 20
    
    def showScore(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.hs_img, self.hs_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)

    def setHighscore(self):
        highscore = self.stats.highscore
        hs_text = f'Highscore: {highscore:,}'
        self.hs_img = self.font.render(hs_text, True, self.color, BG_COLOR)
        self.hs_rect = self.hs_img.get_rect()
        self.hs_rect.centerx =  self.scr_rect.centerx
        self.hs_rect.top = self.score_rect.top
    
    def checkHighscore(self):
        if self.stats.score > self.stats.highscore:
            self.stats.highscore = self.stats.score
            self.setHighscore()

    def setLevel(self):
        level = self.stats.level
        level_text = f'Level: {level}'
        self.level_img = self.font.render(level_text, True, self.color, BG_COLOR)
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right =  self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def setShips(self):
        self.ships = Group()
        for ships in range(self.stats.remainingLives):
            ship = Player(self.main)
            ship.rect.x = 10 + ships * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)