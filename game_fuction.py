import sys
import pygame
import random
from card import Card
import time

"""TEMPORARY DATA"""
# temp data of cards
temp_cards = []
all_open_cards = []
hinted_card = []
card_counter = 0

def reset_temp_data():
    global temp_cards,card_counter,all_open_cards,hinted_card
    # reset temporary data
    temp_cards = []
    # reset the all_open_card if the game doesn't finish
    all_open_cards = []
    hinted_card = []
    card_counter = 0

"""CARD FUCTION"""

# The function to flip a card
def flip_card(card):
    global all_open_cards, card_counter, temp_cards
    temp_cards.append(card)
    card.hint_condition = False
    card.flip_condition = False
    if card not in all_open_cards:
        all_open_cards.append(card)
    card.check_flip()
    card_counter += 1

# The function to reflip all cards
def reflip_card(cards):
    global temp_cards, card_counter,hinted_card
    for card in cards:
        card.flip_condition = True
        card.check_flip()
    temp_cards = []
    hinted_card = []
    card_counter = 0

# This fuction for check the card whether the cards is the same or not
def check_card(cards, set, sb, stats, screen, timer):
    global temp_cards , card_counter
    check_time(set, timer, stats)
    if card_counter == 2 and temp_cards[0].get_card_type() == temp_cards[1].get_card_type():
        stats.score += set.card_points * card_counter
        sb.prep_score()
        check_high_score(stats, sb)
        for card in cards:
            if card == temp_cards[0] or card == temp_cards[1]:
                time.sleep(0.3)
                cards.remove(card)
                all_open_cards.remove(card)
        temp_cards = []
        card_counter = 0
    elif card_counter == 2 and temp_cards[0].get_card_type() != temp_cards[1].get_card_type():
        time.sleep(0.3)
        reflip_card(cards)
    if len(cards) == 0:
        start_game(set, screen, stats, sb, cards, timer)
    if card_counter > 2:
        reflip_card(cards)

# This fuction to check the card and mouse collisions
def check_mouse_card_collisions(cards):
    for card in cards:
        if card.rect.collidepoint(pygame.mouse.get_pos()):
            card.flip_condition = False
            card.check_flip()
            if card not in temp_cards:
                flip_card(card)
            elif card in temp_cards:
                reflip_card(cards)

"""-- To Georgius, 
thank you for helping me figuring out this problem --"""

# To get the number of card in a row
def get_number_cards_x(set, card_width):
    number_cards_x = int(set.screen_width / card_width)
    return number_cards_x

# To get the number of row in the screen
def get_number_rows(set, card_height):
    number_of_rows = int(set.screen_height / card_height)
    return number_of_rows

# This function get the number of add to get to the middle point (width)
def get_calc_at_mid_wid(set,card):
    return int((set.screen_width - get_number_cards_x(set, card.rect.width) * card.rect.width) / 2)

# This fuction get the number of add to get to the middle point (height)
def get_calc_at_mid_hei(set,card):
    return int((set.screen_height - get_number_rows(set, card.rect.height) * card.rect.height) / 2)

# This fuction is to create a single card
def create_cards(set, screen, cards, card_number, row_number):
    # card type
    # to check the card if already exist
    global temp_cards
    type_card = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    card_model = ['Diamond', 'Hearts', 'Clubs', 'Spade']
    while True:
        type_card_num = random.randint(0, 12)
        card_model_num = random.randint(0, 3)
        if [type_card_num, card_model_num] not in temp_cards :
            temp_cards.append([type_card_num, card_model_num])
            break
    card = Card(set, screen, [type_card[type_card_num], card_model[card_model_num]])
    card.rect.x = card.rect.width * card_number + get_calc_at_mid_wid(set,card)
    card.rect.y = card.rect.height * row_number + get_calc_at_mid_hei(set,card)
    cards.add(card)

# This fuction ist to create a multilayer card that doesn't have been used yet
def create_multiple_cards(set, screen, cards):
    global temp_cards
    reset_temp_data()
    # sample cards to calculate
    card = Card(set, screen, ['As', 'Hearts'])
    number_cards_x = get_number_cards_x(set, card.rect.width)
    number_rows = get_number_rows(set, card.rect.height)
    for row_number in range(number_rows):
        for card_number in range(number_cards_x):
            if len(temp_cards) != 52:
                create_cards(set, screen, cards, card_number, row_number)
            else:
                break
    temp_cards = []

""" RUN THE GAME """

# for testing puroses and run the game by it self
def run_the_game(cards,stats,sb):
    global hinted_card, temp_cards
    #for break the loop purposes
    x = 0
    for card in cards:
        y = random.randint(0,1)
        m = random.randint(0,500)
        if len(hinted_card) != 0 and temp_cards == 0:
            if hinted_card[0] == card:
                flip_card(card)
                hinted_card.remove(card)
                break
        elif m == 1 and stats.max_number_hint != 0 and len(temp_cards) == 0:
            run_the_game_hint(cards,stats,sb)
            break
        elif y and card not in temp_cards and card not in all_open_cards:
            flip_card(card)
            break
        elif y and len(all_open_cards) == len(cards) and len(temp_cards) == 0:
            flip_card(card)
            break
        else:
            for card2 in all_open_cards:
                if y and len(temp_cards) != 0 and len(all_open_cards) != 0:
                    if temp_cards[0].get_card_type() == card2.get_card_type() and temp_cards[0] != card2:
                        flip_card(card2)
                        # this is for breaking the first loop after breaking this loop
                        x = 1
                        break
                else:
                    break
            if x:
                break

# this will run the game and flip the card to hint mode which is yellow stipe card
def run_the_game_hint(cards,stats,sb):
    global hinted_card
    if stats.max_number_hint>0:
        stats.max_number_hint -= 1
        sb.prep_hint()
        if len(cards) != 0:
            for card in cards:
                # this to create the card not always show as the first one
                x = random.randint(0,1)
                # this is to make sure the card that are hinted are not the same as before
                if x and card not in hinted_card:
                    card.hint_condition = True
                    hinted_card.append(card)
                    card.check_flip()
                    for card2 in cards:
                        if card.get_card_type() == card2.get_card_type() and card != card2 and card2 not in hinted_card:
                            card2.hint_condition = True
                            hinted_card.append(card2)
                            card2.check_flip()
                            break
                    break

""" GAME STARTING """

# This fuction checking button mouse touch point
def check_play_button(set, screen, stats, sb, play_button, cards, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        set.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        cards.empty()
        create_multiple_cards(set, screen, cards)

# cards = 0
def start_game(set, screen, stats, sb, cards, timer):
    cards.empty()
    reset_temp_data()
    # start a new game in the next level
    timer.reset_time()
    set.increase_data() 
    stats.level += 1
    if stats.level != 1:
        stats.max_number_hint += 1
        sb.prep_hint()
    sb.prep_level()
    create_multiple_cards(set, screen, cards)

"""SCORING FUNCTION """

# To check the high score the update the high score
def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
        stats.update_highscore()

""" TIME FUNCTION """

# To Check the time whether it 0 or not
def check_time(set, timer, stats):
    if timer.get_time_left() < 0:
        stats.game_active = False
        stats.number_of_game += 1
        timer.reset_time()
    else:
        timer.update_time(set.min_fr_time)

""" SYSTEM FUCTION """

# This function to check every event
def check_event(set, cards, stats, sb, play_button, screen):
    global card_counter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # for Help Purposes
            if stats.game_active:
                if event.key == pygame.K_F1 :
                    run_the_game_hint(cards,stats,sb)
                # for Testing Purposes
                elif event.key == pygame.K_r:
                    stats.run_the_game = True
                elif event.key == pygame.K_s:
                    stats.run_the_game = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if stats.game_active:
                if card_counter < 2:
                    check_mouse_card_collisions(cards)
            else:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(set, screen, stats, sb, play_button, cards, mouse_x, mouse_y)

# This function is to update all the screen and the things inside it
def update_screen(set, screen, cards, play_button, stats, sb, timer):
    screen.fill(set.bg_color)
    cards.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    sb.show_score()
    timer.draw_timer()
    pygame.display.flip()
    if stats.run_the_game:
        time.sleep(0.3)
        timer.update_time(set.min_fr_time*3)
