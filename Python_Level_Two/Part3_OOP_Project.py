#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

import random

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print('Deck forms')
        self.allcards = [(s,r) for s in SUITE for r in RANKS];

    def split_cards(self):
        print('Deck splits')
        return [self.allcards[:26],self.allcards[26:]];

    def shuffle_cards(self):
        print('Deck shuffles')
        random.shuffle(self.allcards);

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, deck):
        print('hand recieves the deck')
        self.deck = deck;

    def remove_card(self):
        print('hand_removes')
        return self.deck.pop()

    def add_cards(self,cards):
        print('hand_adds')
        self.deck.extend(cards)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        print('player enters');
        self.name = name;
        self.hand = hand;

    def play_card(self):
        print(self.name + ' plays');
        return self.hand.remove_card();

    def play_war(self):
        war = []

        if len(self.hand.deck) < 3:
            return war;
        else:
            for i in range(3):
                war.append(self.hand.deck.pop())
            return war

    def check_card(self):
        print('card check');
        if len(self.hand.deck) != 0:
            return True

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

deck = Deck();
deck.shuffle_cards();
player_deck = deck.split_cards()[0];
comp_deck = deck.split_cards()[1];
print(type(player_deck));
player_hand = Hand(player_deck);
comp_hand = Hand(comp_deck);

player = Player('player',player_hand);
comp = Player('comp',comp_hand);

while player.check_card() and comp.check_card():

    table_cards = []

    player_card = player.play_card();
    comp_card = comp.play_card();
    table_cards.append(player_card);
    table_cards.append(comp_card);

    print(player.name + ': ' + str(RANKS.index(player_card[1]))+ '; ' + comp.name + ': ' + str(RANKS.index(comp_card[1])))

    if RANKS.index(player_card[1]) > RANKS.index(comp_card[1]):
        print('player wins')
        player_hand.add_cards(table_cards)
    elif RANKS.index(player_card[1]) < RANKS.index(comp_card[1]):
        print('comp wins')
        comp_hand.add_cards(table_cards)
    elif RANKS.index(player_card[1]) == RANKS.index(comp_card[1]):
        print('war')
        table_cards.extend(player.play_war())
        table_cards.extend(comp.play_war())

        player_card = player.play_card();
        comp_card = comp.play_card();
        table_cards.append(player_card);
        table_cards.append(comp_card);

        if RANKS.index(player_card[1]) > RANKS.index(comp_card[1]):
            print('player wins')
            player_hand.add_cards(table_cards)
        elif RANKS.index(player_card[1]) < RANKS.index(comp_card[1]):
            print('comp wins')
            comp_hand.add_cards(table_cards)

if player.check_card(): print('\n player wins')
else: print('\n comp wins')
    # if :
# Use the 3 classes along with some logic to play a game of war!
