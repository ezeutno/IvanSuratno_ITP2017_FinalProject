class Game_stats:
    def __init__(self,set):
        self.set = set
        self.high_score = int(open('Database\\high_score.txt','r').read())
        self.reset_stats()
        self.game_active = False

        # this to run the game by it self
        self.run_the_game = False

        # stats how many game have been played
        self.number_of_game = 1

    def reset_stats(self):
        self.max_number_hint = 3
        self.score = 0
        self.level = 1

    def update_highscore(self):
        open('Database\\high_score.txt','w').write(str(self.high_score))
