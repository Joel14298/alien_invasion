import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #loading alien figure in to the game
        self.image = pygame.image.load('images/alien.bmp')

        self.rect = self.image.get_rect()
        

        #Start each alien near the top-left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store aliens position in float
        self.x = float(self.rect.x)

    def update(self):
            self.x += self.settings.alien_speed
            self.rect.x = self.x

        