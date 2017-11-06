import pygame.ftfont
import game_fuction as gf
from card import Card 

class Scoreboard:
    def __init__(self,set,screen,stats):
        # Example of a card to take messurment of the height and width of card after scale
        self.card_ex = Card(set, screen, ['As', 'Hearts'])
        # messure the minus for the bottom and right for sync with the card
        self.min_bottom = gf.get_calc_at_mid_hei(set,self.card_ex)
        self.min_right = gf.get_calc_at_mid_wid(set,self.card_ex)

        # determine the font size
        self.font_size =int(self.card_ex.rect.height/4)

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.set = set
        self.stats = stats
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, self.font_size)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_hint()

    def prep_hint(self):
        hint_str = "Hint : {:,}".format(self.stats.max_number_hint)
        self.hint_image = self.font.render(hint_str, True, self.text_color, None)
        self.hint_rect = self.hint_image.get_rect()
        self.hint_rect.bottom = self.screen_rect.bottom - self.min_bottom 
        self.hint_rect.right = self.screen_rect.right - self.min_right 

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.bottom = self.screen_rect.bottom - self.min_bottom - self.font_size
        self.score_rect.right = self.screen_rect.right - self.min_right

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = '{:,}'.format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,None)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.bottom = self.screen_rect.bottom - self.min_bottom - self.font_size*2
        self.high_score_rect.right = self.screen_rect.right - self.min_right

    def prep_level(self):
        self.level_image = self.font.render("Lv."+str(self.stats.level),True,self.text_color,None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.bottom = self.screen_rect.bottom - self.min_bottom - self.font_size*3
        self.level_rect.right = self.screen_rect.right - self.min_right

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.hint_image,self.hint_rect)

