"""
Game Black Jack

"""
from random import shuffle
from button import Button

class Deck():
    """Building the Deck"""

    def __init__(self):
        """Create all cards in the deck"""
        cards_numbers = range(2,11)
        cards_faces = ['Jack', 'Queen', 'King', 'Ace']
        cards_colors = ['Clubs','Diamonds','Hearts','Spades']

        self.all_cards = [[face, color] for face in
                         cards_faces for color in cards_colors] + \
                         [[number, color] for number in
                         cards_numbers for color in cards_colors]
        self.all_cards = self.all_cards * 6
        shuffle(self.all_cards)


    def draw(self):
        """
        Drawing a card from a deck

        Returns
        -------
        first card from deck top

        """
        try:

            return self.all_cards.pop(0)

        except IndexError:
        #shuffling the cards

            self.__init__()
            return self.all_cards.pop(0)




class Player():
    """Creating a new player"""


    def __init__(self):
        self.player_cards = []
        self.hand = []
        self.hand_2 = []


    def reset_hand(self):
        """reset player hand"""
        self.hand = []
        self.hand_2 = []


    def value_hand(self, hand):
        """
        Count value players hand

        Returns
        -------
        Values card sum of int

        """
        value = 0
        for card in hand:
            if isinstance(card[0], int):
                value += card[0]
            elif card[0] == 'Ace':
                if value < 11:
                    value += 11
                else:
                    value += 1
            else:
                value += 10
        return value

class GameData():
    """game starts"""

    def __init__(self, parents):
        self.parents = parents
        self.player = Player()
        self.krupier = Player()
        self.cards_deck = Deck()


    def hit(self):
        """ hit - draw the card to user deck """

        if self.parents.check_split:

            if self.parents.check_split == 'second':
                self.player.hand_2.append(self.cards_deck.draw())
                if (self.player.hand_2[0][0] == 'Ace' and self.player.hand_2[1][0] ==
                'Ace') or self.player.value_hand(self.player.hand_2) == 21:
                    self.parents.walet.add_value_2(self.parents.walet.bet_2*2.5)
                    self.parents.communicate_2 = 'black_jack'
                    self.parents.stage = 'begin'

#############################################################################
                    if self.parents.communicate == '':
                        while self.krupier.value_hand(self.krupier.hand) < 17:
                            self.krupier.hand.append(self.cards_deck.draw())

                            self.parents.check_krupier = 1

                            if self.krupier.value_hand(self.krupier.hand) > 21:
                                self.parents.walet.add_value(self.parents.walet.bet*2)
                                self.parents.communicate = 'won'
                                self.parents.check_split = 'second'


                            else:
                                if self.krupier.value_hand(self.krupier.hand) > \
                                self.player.value_hand(self.player.hand):
                                    self.parents.walet.bet = 0
                                    self.parents.communicate = 'lose'
                                    self.parents.check_split = 'second'


                                elif self.krupier.value_hand(self.krupier.hand) < \
                                self.player.value_hand(self.player.hand):
                                    self.parents.walet.add_value(self.parents.walet.bet*2)
                                    self.parents.communicate = 'won'
                                    self.parents.check_split = 'second'


                                elif self.krupier.value_hand(self.krupier.hand) == \
                                self.player.value_hand(self.player.hand):
                                    self.parents.walet.bet = self.parents.walet.bet + \
                                                            self.parents.walet.bet_2
                                    self.parents.communicate = 'draw'
                                    self.parents.check_split = 'second'
#############################################################################

                elif self.player.value_hand(self.player.hand_2) > 21:
                    self.parents.walet.bet_2 = 0
                    self.parents.communicate_2 = 'lose'
                    self.parents.stage = 'begin'


#############################################################################
                    if self.parents.communicate == '':
                        while self.krupier.value_hand(self.krupier.hand) < 17:
                            self.krupier.hand.append(self.cards_deck.draw())

                            self.parents.check_krupier = 1

                            if self.krupier.value_hand(self.krupier.hand) > 21:
                                self.parents.walet.add_value(self.parents.walet.bet*2)
                                self.parents.communicate = 'won'
                                self.parents.check_split = 'second'

                            else:
                                if self.krupier.value_hand(self.krupier.hand) > \
                                self.player.value_hand(self.player.hand):
                                    self.parents.walet.bet = 0
                                    self.parents.communicate = 'lose'
                                    self.parents.check_split = 'second'

                                elif self.krupier.value_hand(self.krupier.hand) < \
                                self.player.value_hand(self.player.hand):
                                    self.parents.walet.add_value(self.parents.walet.bet*2)
                                    self.parents.communicate = 'won'
                                    self.parents.check_split = 'second'

                                elif self.krupier.value_hand(self.krupier.hand) == \
                                self.player.value_hand(self.player.hand):
                                    self.parents.walet.bet = self.parents.walet.bet + \
                                                            self.parents.walet.bet_2
                                    self.parents.communicate = 'draw'
                                    self.parents.check_split = 'second'
#############################################################################

            else:
                self.player.hand.append(self.cards_deck.draw())
                if (self.player.hand[0][0] == 'Ace' and self.player.hand[1][0] ==
                'Ace') or self.player.value_hand(self.player.hand) == 21:
                    self.parents.walet.add_value(self.parents.walet.bet*2.5)
                    self.parents.communicate = 'black_jack'
                    self.parents.check_split = 'second'

                elif self.player.value_hand(self.player.hand) > 21:
                    self.parents.walet.bet = 0
                    self.parents.communicate = 'lose'
                    self.parents.check_split = 'second'

        else:
            # without split
            self.player.hand.append(self.cards_deck.draw())
            if (self.player.hand[0][0] == 'Ace' and self.player.hand[1][0] ==
                'Ace') or self.player.value_hand(self.player.hand) == 21:
                self.parents.walet.add_value(self.parents.walet.bet*2.5)
                self.parents.communicate = 'black_jack'
                self.parents.stage = 'begin'

            elif self.player.value_hand(self.player.hand) > 21:
                self.parents.walet.bet = 0
                self.parents.check_krupier = 1
                self.parents.communicate = 'lose'
                self.parents.stage = 'begin'


    def stand(self):
        """ stand - check for krupier hand and wait for results """


        if self.parents.check_split:

            if self.parents.check_split == 'second':
                self.parents.check_krupier = 1
                while self.krupier.value_hand(self.krupier.hand) < 17:
                    self.krupier.hand.append(self.cards_deck.draw())


                if self.krupier.value_hand(self.krupier.hand) > 21:
                    self.parents.walet.add_value_2(self.parents.walet.bet_2*2)
                    self.parents.communicate_2 = 'won'
                    self.parents.stage = 'begin'


                else:
                    if self.krupier.value_hand(self.krupier.hand) > \
                    self.player.value_hand(self.player.hand_2):
                        self.parents.walet.bet_2 = 0
                        self.parents.communicate_2 = 'lose'
                        self.parents.stage = 'begin'

                    elif self.krupier.value_hand(self.krupier.hand) < \
                    self.player.value_hand(self.player.hand_2):
                        self.parents.walet.add_value_2(self.parents.walet.bet_2*2)
                        self.parents.communicate_2 = 'won'
                        self.parents.stage = 'begin'

                    elif self.krupier.value_hand(self.krupier.hand) == \
                    self.player.value_hand(self.player.hand_2):
                        self.parents.walet.add_value_2(self.parents.walet.bet_2*2)
                        self.parents.communicate_2 = 'won'
                        self.parents.stage = 'begin'

####################################################################3
                self.parents.check_krupier = 1

                if self.krupier.value_hand(self.krupier.hand) > 21:
                    self.parents.walet.add_value(self.parents.walet.bet*2)
                    self.parents.communicate = 'won'
                    self.parents.check_split = 'second'

                else:
                    if self.krupier.value_hand(self.krupier.hand) > \
                    self.player.value_hand(self.player.hand):
                        self.parents.walet.bet = 0
                        self.parents.communicate = 'lose'
                        self.parents.check_split = 'second'

                    elif self.krupier.value_hand(self.krupier.hand) < \
                    self.player.value_hand(self.player.hand):
                        self.parents.walet.add_value(self.parents.walet.bet*2)
                        self.parents.communicate = 'won'
                        self.parents.check_split = 'second'

                    elif self.krupier.value_hand(self.krupier.hand) == \
                    self.player.value_hand(self.player.hand):
                        self.parents.walet.bet = self.parents.walet.bet + \
                                                self.parents.walet.bet_2
                        self.parents.communicate = 'draw'
                        self.parents.check_split = 'second'

########################################################################
            else:
                self.parents.check_split = 'second'

        else:
            # without split
            self.parents.check_krupier = 1
            while self.krupier.value_hand(self.krupier.hand) < 17:
                self.krupier.hand.append(self.cards_deck.draw())

            if self.krupier.value_hand(self.krupier.hand) > 21:
                self.parents.walet.add_value(self.parents.walet.bet*2)
                self.parents.walet.bet = 0
                self.parents.communicate = 'won'
                self.parents.stage = 'begin'

            elif self.krupier.value_hand(self.krupier.hand) > \
            self.player.value_hand(self.player.hand):
                self.parents.walet.bet = 0
                self.parents.communicate = 'lose'
                self.parents.stage = 'begin'

            elif self.krupier.value_hand(self.krupier.hand) < \
            self.player.value_hand(self.player.hand):
                self.parents.walet.add_value(self.parents.walet.bet*2)
                self.parents.walet.bet = 0
                self.parents.communicate = 'won'
                self.parents.stage = 'begin'

            elif self.krupier.value_hand(self.krupier.hand) == \
            self.player.value_hand(self.player.hand):
                self.parents.communicate = 'draw'
                self.parents.stage = 'begin'


    def split(self):
        """ split - if you have two the same cards, you can split them """

        self.player.hand_2.append(self.player.hand.pop(1))
        self.parents.walet.set_bet_2(self.parents.walet.bet)
        self.parents.check_split = True


    def split_2(self):
        """ split - if you have two different cards, you can split them but
        your turn is over"""

        self.player.hand_2.append(self.player.hand.pop(1))
        self.parents.walet.set_bet_2(self.parents.walet.bet)
        self.parents.check_split = True
        self.player.hand.append(self.cards_deck.draw())
        self.player.hand_2.append(self.cards_deck.draw())
        self.parents.check_split = 'second'


    def double(self, bet):
        """ you can double the bet """

        self.parents.walet.set_bet(bet)
        self.parents.check_double = False


    def double_2(self, bet):
        """ you can double the bet_2 """

        if self.parents.check_split == 'second':
            self.parents.walet.set_bet_2(bet)
            self.parents.check_double_2 = False

    def surrender(self):
        """ if you have bad cards you have to pass and get 50% ypur bets """

        self.parents.walet.add_value(self.parents.walet.bet/2)
        self.parents.walet.bet = 0
        self.parents.walet.add_value(self.parents.walet.bet_2/2)
        self.parents.walet.bet_2 = 0

    def start_game(self):
        """create game with krupier"""

        self.krupier.hand.append(self.cards_deck.draw())
        self.player.hand.append(self.cards_deck.draw())
        self.krupier.hand.append(self.cards_deck.draw())
        self.player.hand.append(self.cards_deck.draw())

        if (self.player.hand[0][0] == 'Ace' and self.player.hand[1][0] ==
            'Ace') or self.player.value_hand(self.player.hand) == 21:
            self.parents.walet.add_value(self.parents.walet.bet*2.5)
            self.parents.communicate = 'black_jack'
            self.parents.stage = 'begin'


    def drawing_a_card(self):
        """ draw cards from main deck"""
        self.card_user = Button(self.parents, self.parents.size[0]/2,
                                self.parents.size[1]*0.8, 'image//card.png', 0.55).draw()


    def end_game(self):
        """ clear player and krupier decks """
        self.player.reset_hand()
        self.krupier.reset_hand()
