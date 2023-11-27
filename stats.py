from settings import *

class Stats:
    def __init__(self):
        self.remainingLives = PLAYER_HEALTH
        self.score = 0
        self.highscore = 0
        self.level = 1
        self.reset()

    def reset(self):
        self.remainingLives = PLAYER_HEALTH
        self.score = 0