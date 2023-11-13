class Settings:
    def __init__(self):
        #Static Settings
        # Game settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5
        

        #bullet settings
        
        self.bullet_width = 3
        self.bullet_height = 15
        self. bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        #alien Settings
        
        self.fleet_drop_speed = 10
        
        

        #Game speed up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        #Ships
        self.ship_limit = 3
        
        #Bullets
        self.bullet_speed = 1.0
        
        #Aliens
        self.alien_speed = 1.0

                
        #Fleet
        # fleet direction -1 for left and 1 for right
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        #Increase speed setting
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale