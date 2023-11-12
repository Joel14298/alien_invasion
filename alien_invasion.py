import sys
from time import sleep


import pygame



from settings import Settings
from game_stats import GameStats
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

        #Create an instance to store the game stats
        self.stats = GameStats(self)
        
        
        self.ships = Ship(self)  # Adding the ship to the game
        self.bullets = pygame.sprite.Group() #Adding bullet functionality
        self.aliens = pygame.sprite.Group() #Adding aliens

        self._create_enemy_fleet()

        self.bg_color = self.settings.bg_color  # set the background color

    def run_game(self):
        while True:
            self._check_events()
            
            if self.stats.game_active:
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

        self._check_bullet_enemy_collisions()

    def _check_bullet_enemy_collisions(self):
        #Remove any bullets that have collided with the enemy
            #Check for any bullets that have hit the aliens and remove if so hit the aliens.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_enemy_fleet()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        #Check for aliens and collision
        if pygame.sprite.spritecollideany(self.ships, self.aliens):
            self._ship_hit()
            
        #look for hiiting aliens at the bottom of the screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        
        if self.stats.ships_left > 0:
            #Decrement the total number of ships once lost
            self.stats.ships_left -= 1

            #Removing remaining aliens and bullets
            self.aliens.empty() 
            self.bullets.empty()

            #Create a new fleet
            self._create_enemy_fleet()
            self.ships.center_ship()

            #pause
            sleep(0.5)
        else:
            self.stats.game_active = False
        
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
        
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

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

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
