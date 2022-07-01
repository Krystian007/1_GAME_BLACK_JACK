"""
Game Black Jack

"""

from random import shuffle


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


    def __init__(self, name):
        self.name = name
        self.player_cards = []
        self.hand = []


    def reset_hand(self):
        """reset player hand"""
        self.hand = []


    def value_hand(self):
        """
        Count value players hand

        Returns
        -------
        Values card sum of int

        """
        value = 0
        for card in self.hand:
            if isinstance(card[0], int):
                value += card[0]
            elif card[0] == 'Ace':  #ustaw dla asa przedział albo dwie opcje
                if value < 11:
                    value += 11
                else:
                    value += 1
            else:
                value += 10
        return value

class Game():
    """game starts"""

    def __init__(self):
        self.player = Player(input('Enter your name: '))
        self.krupier = Player('Krupier')
        self.cards_deck = Deck()


    def player_decision(self):
        """
        players hand decisions

        Returns
        -------
        decision

        """
        print(f'\n\n\nyour hand is {self.player.hand}')
        print(f'those value is {self.player.value_hand()}')
        print(f'Crupier hand is {self.krupier.hand[0]}')
        decision = input("""1 - hit
2 - stand
3 - split
4 - double
5 - surrender
6 - leave the table

chose your move: """)
        if decision =='6':
            return False

        while True:

            if decision == '1':
                self.player.hand.append(self.cards_deck.draw())
                if self.player.value_hand() < 21:
                    print(f'\n\n\nyour hand is {self.player.hand}')
                    print(f'those value is {self.player.value_hand()}')
                    print(f'Crupier hand is {self.krupier.hand[0]}')
                    decision = input("""1 - hit
2 - stand
3 - split
4 - double
5 - surrender
6 - leave the table

chose your move: """)
                else:
                    print(f'''\n\n\nYou have too much,
you took {self.player.hand[-1]}
your sum of the cards are {self.player.value_hand()}
You lost''')
                    break

            elif decision =='2':
                break

            elif decision =='3':
                # if len(self.player.hand) == 0 and self.player.hand[0] == self.player.hand[1]:
                break
            elif decision =='4':
                break
            elif decision =='5':
                break
            else:
                decision = input("""You must choice
                                      
1 - hit
2 - stand
3 - split
4 - double
5 - surrender
6 - leave the table

chose your move: """)


    def start_game(self):
        """create game with krupier"""

        while True:

            self.krupier.hand.append(self.cards_deck.draw())
            self.player.hand.append(self.cards_deck.draw())
            self.krupier.hand.append(self.cards_deck.draw())
            self.player.hand.append(self.cards_deck.draw())
            if self.player_decision() is False:
                break



            self.player.reset_hand()
            self.krupier.reset_hand()

game = Game()
game.start_game()
