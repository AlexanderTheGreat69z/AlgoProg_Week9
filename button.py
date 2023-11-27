import pygame.font

class Button:
    def __init__(self, main, text):

        # get screen dimensions
        self.screen = main.screen
        self.scr_rect = self.screen.get_rect()

        self.size = (200, 50)
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, *self.size)
        self.rect.center = self.scr_rect.center
        self._prepareText(text)

    def _prepareText(self, text):
        self.text_img = self.font.render(text, True, self.text_color)
        self.text_rect = self.text_img.get_rect()
        self.text_rect.center = self.rect.center

    def drawButton(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_img, self.text_rect)