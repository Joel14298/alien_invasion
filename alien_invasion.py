import sys
import pygame
from settings import Settings
from ships import Ship
from bullet import Bullet


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        # size of the game window
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height 
        pygame.display.set_caption("Alien Invasion")  # title of the game

        self.ships = Ship(self)  # Adding the ship to the game
        self.bullets = pygame.sprite.Group() #Adding bullet dunctionality

        self.bg_color = self.settings.bg_color  # set the background color

    def run_game(self):
        while True:
            self._check_events()
            self.ships.update_ship()
            self._update_bullets()
            self._update_screen()



    def _check_events(self):
        for event in pygame.event.get():  # has an event listener called event
            if event.type == pygame.QUIT:  # if 'x' button is clicked
                sys.exit()  # close the game window

            # On pressing Left and right key the space ship will move once released it stop
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ships.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ships.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ships.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ships.moving_left = False

    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullets_allowed:   
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #get rid of the bullet once shot and update the total bullets
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                print(len(self.bullets))


    def _update_screen(self):
        # redraw the screen with every loop
        self.screen.fill(self.settings.bg_color)
        self.ships.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # ensures that new element are showing up on the display new position of the game
        pygame.display.flip()


if __name__ == '__main__':
    # Make an instance of the game window
    ai = AlienInvasion()
    ai.run_game()
