import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        #creating bullet object with ships position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #creating a bullet at 0,0
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ships.rect.midtop

        #Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
    
    def update(self):
        #Moving the bullet
        #update the decimal position of the bullet 
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        #Drawing the bullet
        pygame.draw.rect(self.screen, self.color, self.rect)