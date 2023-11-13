class GameStats:
    
    def __init__(self,ai_game):
        #Initialising the stats
        self.settings = ai_game.settings
        self.reset_stats()
        
        #Start Alien invasion in an Active state
        self.game_active = False

        #High-score
        self.high_score = 0

    def reset_stats(self):
        #"Intialise the states that can change in the game"
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    