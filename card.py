import pygame
import math
from pygame.sprite import Sprite


class Card(Sprite):
    def __init__(self, set, screen, card_type):
        super(Card, self).__init__()
        self.screen = screen
        self.set = set
        self.card_type = card_type

        # condition of card flip
        self.flip_condition = True

        # condition of hint = True
        self.hint_condition = False

        # card start with a cover card
        self.card = pygame.image.load('Database\\Cards\\CardCover.png')

        # get card rect
        self.card_rect = self.card.get_rect()

        # calculate the are of the screen
        self.screen_area = set.screen_width * set.screen_height
        # asumming there are 52 card with an extra card for other things ('I know this is magic number')
        self.card_area = self.screen_area / 62
        self.card_ratio_w_to_h = self.card_rect.width/self.card_rect.height
        self.card_re_rect_width = math.ceil(math.sqrt(self.card_ratio_w_to_h * self.card_area))
        self.card_re_rect_height = math.ceil(math.sqrt((1/self.card_ratio_w_to_h) * self.card_area))

        # create the trasformed scale image
        self.image = pygame.transform.scale(self.card, (self.card_re_rect_width,self.card_re_rect_height))
        self.rect = self.image.get_rect()

    # return card number
    def get_card_type(self):
        return self.card_type[0]

    # return card logo
    def get_card_class(self):
        return self.card_type[1]

    # refliping the card based on flip_condition
    def check_flip(self):
        if self.hint_condition:
            # show the hinted image
            self.card = pygame.image.load('Database\\Cards\\CardCover(hint).png')
        elif self.flip_condition:
            self.card = pygame.image.load('Database\\Cards\\CardCover.png')
        else:
            self.card = pygame.image.load('Database\\Cards\\{0}of{1}.png'.format(self.card_type[0], self.card_type[1]))
        self.image = pygame.transform.scale(self.card, (self.card_re_rect_width,self.card_re_rect_height))
