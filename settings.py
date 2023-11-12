class Settings:
    def __init__(self):
        # Game settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self. bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        #alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50
        # fleet direction -1 for left and 1 for right
        self.fleet_direction = 1