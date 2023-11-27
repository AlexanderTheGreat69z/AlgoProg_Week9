from settings import *

class Stats:
    def __init__(self):
        self.reset()
    def reset(self):
        self.remainingLives = PLAYER_HEALTH