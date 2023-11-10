import pygame


class Ship:
    def __init__(self, ai_game):  # passed Ai game to it, for esay access
        # Instailising the ships
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loading the ship in its rect
        self.image = pygame.image.load('images/main_ship.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()

        # setting the starting postition of the ship
        # loading the ship in a rectangle
        self.rect.midbottom = self.screen_rect.midbottom

        # storing decimal value for ships position
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update_ship(self):

        # updating the speed of the ship as per the settings
        # stops moving when the ship is trying to move after the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        # Drawing the ship in the location
        self.screen.blit(self.image, self.rect)
