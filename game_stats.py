class GameStats:
    
    def __init__(self,ai_game):
        #Initialising the stats
        self.settings = ai_game.settings
        self.reset_stats()
        
        
        #Start Alien invasion in an Active state
        self.game_active = False

    def reset_stats(self):
        #"Intialise the states that can change in the game"
        self.ships_left = self.settings.ship_limit
        self.score = 0
    
    