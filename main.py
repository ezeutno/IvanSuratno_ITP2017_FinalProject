import pygame
import game_fuction as gf
from settings import Settings as settings
from pygame.sprite import Group
from scoreboard import Scoreboard as Sb
from stats import Game_stats as Gs
from timer import Timer
from playbutton import Play_button
from game_over import Game_over as Go

def main():
    pygame.init()
    set = settings()
    stats = Gs(set)
    pygame.display.set_caption(set.caption)
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    sb = Sb(set,screen,stats)
    timer = Timer(screen)
    play_button = Play_button(screen, "Click to Play")
    cards = Group()
    while True:
        # this comment to run the game by it self
        if stats.run_the_game and stats.game_active:
            gf.run_the_game(cards,stats,sb)
            
        gf.check_event(set,cards,stats,sb,play_button,screen)
        gf.update_screen(set,screen,cards,play_button,stats,sb,timer)        

        if stats.game_active == False:
            if stats.number_of_game > 1:
                # Game over button
                play_button = Go(screen,stats)
                # this make sure computer doesn't run the game in the background after fail playing it
            stats.run_the_game = False

        if stats.game_active:
            # if the game_active anc check the card then remove it
            gf.check_card(cards, set, sb, stats, screen, timer)
main()

# Credits to Python Crash Course, Alien Invasion Chapter 12-14