import pygame.font

class Scoreboard:
    #Class for report score information

    def __init__(self, ai_game):
        #Initialise scorebaord
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Font settings of the soreboard
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initiale score image
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Display the score on the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        #Drawing Score card in the game
        self.screen.blit(self.score_image, self.score_rect)
