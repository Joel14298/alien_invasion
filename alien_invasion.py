import sys
import pygame
from settings import Settings
from ships import Ship
from bullet import Bullet
from alien import Alien


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
        self.bullets = pygame.sprite.Group() #Adding bullet functionality
        self.aliens = pygame.sprite.Group() #Adding aliens

        self._create_enemy_fleet()

        self.bg_color = self.settings.bg_color  # set the background color

    def run_game(self):
        while True:
            self._check_events()
            self.ships.update_ship()
            self._update_bullets()
            self._update_aliens()
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

    def _update_aliens(self):
        self.aliens.update()

    def _create_enemy_fleet(self):
        #making an alien fleet
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        availible_space_x = self.settings.screen_width - ( 2 * alien_width)
        number_aliens_x = availible_space_x // (2 * alien_width) 
        # self.aliens.add(alien)

        #Determine the number of rows of the aliens
        ship_height = self.ships.rect.height
        availible_space_y =(self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = availible_space_y // (2 * alien_height)

        # for full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
        


    def _update_screen(self):
        # redraw the screen with every loop
        self.screen.fill(self.settings.bg_color)
        self.ships.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)

        # ensures that new element are showing up on the display new position of the game
        pygame.display.flip()


if __name__ == '__main__':
    # Make an instance of the game window
    ai = AlienInvasion()
    ai.run_game()
