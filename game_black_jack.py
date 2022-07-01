"""
Game Black Jack



PNG Sources
<a href='https://pngtree.com/so/cartoon'>cartoon png from pngtree.com/</a>
<a href='https://pngtree.com/so/nine'>nine png from pngtree.com/</a>

"""

# from random import shuffle
import pygame
import black_jack
import walet
from button import Button

class Game():
    """ screan game """

    def __init__(self):
        # Initlaization
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.backgroundfile = pygame.image.load('image//table.jpg')
        self.engine = black_jack.GameData(self)
        self.check_krupier = 0
        self.communicate = ''
        self.check_split = False
        self.check_double = True
        self.check_double_2 = False
        self.walet = walet.Walet()

        # set position in main menu
        self.size = self.screen.get_size()
        self.start_button = Button(self, self.size[0]/2,self.size[1]/3,
                                   'image//start_btn.png', 1.2)
        self.exit_button = Button(self, self.size[0]/2, (self.size[1]/3)*2,
                                  'image//exit_btn.png', 1.2)

        # set position in game
        self.hit_button = Button(self, self.size[0]*0.05, self.size[1] - 300,
                                 'image//hit_btn.png', 0.6)
        self.stand_button = Button(self, self.size[0]*0.05, self.size[1] - 250,
                                   'image//stand_btn.png', 0.6)
        self.split_button = Button(self, self.size[0]*0.05, self.size[1] - 200,
                                   'image//split_btn.png', 0.6)
        self.double_button = Button(self, self.size[0]*0.05, self.size[1] - 150,
                                    'image//double_btn.png', 0.6)
        self.surrender_button = Button(self, self.size[0]*0.05, self.size[1] - 100,
                                       'image//surrender_btn.png', 0.6)
        self.leave_button = Button(self, self.size[0]*0.05, self.size[1] - 50,
                                   'image//leave_btn.png', 0.6)
        self.card_revers_image = Button(self, self.size[0]*0.92, self.size[1]/2,
                                        'image//card_reverse.png', 0.55)

        self.chips_10_button = Button(self, self.size[0]*0.74, self.size[1]*0.85,
                                'image//10.png', 0.75)
        self.chips_20_button = Button(self, self.size[0]*0.81, self.size[1]*0.85,
                                'image//20.png', 0.75)
        self.chips_50_button = Button(self, self.size[0]*0.88, self.size[1]*0.85,
                                'image//50.png', 0.75)
        self.chips_100_button = Button(self, self.size[0]*0.95, self.size[1]*0.85,
                                'image//100.png', 0.75)


        # config
        self.tps_max = 70.0
        self.place = 'menu'


        # run the game
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.quit:
                    run = False

            # Ticking
            self.tps_delta += self.tps_clock.tick()/3000.0
            while self.tps_delta >1/self.tps_max:

                # Drawing pattern
                self.screen.fill((0,0,0))
                self.screen.blit(self.backgroundfile, self.backgroundfile.get_rect())
    
    
                # Drawing main menu
                if self.place == 'menu':
                    start = self.start_button.draw()
                    exxit = self.exit_button.draw()
                    if start:
                        self.communicate = ''
                        self.communicate_2 = ''
                        self.check_split = False
                        self.check_double = True
                        self.check_double_2 = True
                        self.engine = black_jack.GameData(self)
                        self.walet = walet.Walet()
                        self.place = 'game'
                        self.stage = 'begin'
                    if exxit:
                        run = False
    
                # Drawing game screen
                if self.place == 'game':
                    hit_btn = self.hit_button.draw()
                    stand_btn = self.stand_button.draw()
                    split_btn = self.split_button.draw()
                    double_btn = self.double_button.draw()
                    surrender_btn = self.surrender_button.draw()
                    leave_btn = self.leave_button.draw()
    
                    chips_10 = self.chips_10_button.draw()
                    chips_20 = self.chips_20_button.draw()
                    chips_50 = self.chips_50_button.draw()
                    chips_100 = self.chips_100_button.draw()
    
    
                    # Drawing cards deck
                    card_revers_img = self.card_revers_image.draw()
                    for card in range(6):
                        card_revers_img = Button(self, self.size[0]*(0.94 - 0.01*card),
                                                 self.size[1]/2,'image//card_reverse.png',
                                                 0.55).draw()
    
                    # Drawing players cards
                    if self.check_split:
                        # when split
    
                        # when the same cards
                        if self.engine.player.hand[0][0] == self.engine.player.hand_2[0][0]:
                            card_to_draw = 0
                            for card in self.engine.player.hand:
                                Button(self, self.size[0]*((0.35) + 0.03*card_to_draw),
                                       self.size[1]*0.8, f'image//cards//{card[0]}_{card[1]}.png',
                                       0.55).draw()
                                card_to_draw += 1
    
                            card_to_draw = 0
                            for card in self.engine.player.hand_2:
                                Button(self, self.size[0]*((0.55) + 0.03*card_to_draw),
                                       self.size[1]*0.8, f'image//cards//{card[0]}_{card[1]}.png',
                                       0.55).draw()
                                card_to_draw += 1
                        else:
                            #when difrent cards
                            #first hand
                            Button(self, self.size[0]*((0.35)),
                                       self.size[1]*0.8, f'image//cards//{self.engine.player.hand[0][0]}_{self.engine.player.hand[0][1]}.png',
                                               0.55).draw()
                            Button(self, self.size[0]*((0.35) + 0.03),
                                       self.size[1]*0.75, f'image//cards//{self.engine.player.hand[1][0]}_{self.engine.player.hand[1][1]}.png',
                                               0.55, 90).draw()
    
                            # Second hand
                            Button(self, self.size[0]*((0.55)),
                                       self.size[1]*0.8, f'image//cards//{self.engine.player.hand_2[0][0]}_{self.engine.player.hand_2[0][1]}.png',
                                               0.55).draw()
                            Button(self, self.size[0]*((0.55) + 0.03),
                                       self.size[1]*0.75, f'image//cards//{self.engine.player.hand_2[1][0]}_{self.engine.player.hand_2[1][1]}.png',
                                               0.55, 90).draw()
    
                    else:
                        # without split
                        card_to_draw = 0
                        for card in self.engine.player.hand:
                            Button(self, self.size[0]*((0.45) + 0.03*card_to_draw),
                                   self.size[1]*0.8, f'image//cards//{card[0]}_{card[1]}.png',
                                   0.55).draw()
                            card_to_draw += 1
    
                    # Drawing krupier cards
                    self.krupier_cards = 0 + self.check_krupier
                    for card in self.engine.krupier.hand:
    
                        if self.krupier_cards >= 1:
    
                            Button(self, self.size[0]*((0.45) + 0.03*(self.krupier_cards
                                    - self.check_krupier)), self.size[1]*0.2,
                                   f'image//cards//{card[0]}_{card[1]}.png', 0.55).draw()
                            self.krupier_cards += 1
    
                        elif self.krupier_cards < 1:
    
                            Button(self, self.size[0]*((0.45) + 0.03*self.krupier_cards),
                                   self.size[1]*0.2, 'image//card_reverse.png', 0.55).draw()
                            self.krupier_cards += 1
    
    
                    communicate_cancel = False
                    # Drawing comunicate popup
                    if self.check_split:
    
    
                        if self.communicate == 'won':
                            communicate_cancel = Button(self, self.size[0]*0.35, self.size[1]/2,
                                        'image//won.png', 0.75).draw()
                        if self.communicate == 'lose':
                            communicate_cancel = Button(self, self.size[0]*0.35, self.size[1]/2,
                                        'image//lose.png', 0.75).draw()
                        if self.communicate == 'black_jack':
                            communicate_cancel = Button(self, self.size[0]*0.35, self.size[1]/2,
                                        'image//black_jack.png', 0.75).draw()
                        if self.communicate == 'draw':
                            communicate_cancel = Button(self, self.size[0]*0.35, self.size[1]/2,
                                        'image//draw.png', 0.75).draw()
    
    
                        if self.communicate_2 == 'won':
                            communicate_cancel = Button(self, self.size[0]*0.55, self.size[1]/2,
                                        'image//won.png', 0.75).draw()
                        if self.communicate_2 == 'lose':
                            communicate_cancel = Button(self, self.size[0]*0.55, self.size[1]/2,
                                        'image//lose.png', 0.75).draw()
                        if self.communicate_2 == 'black_jack':
                            communicate_cancel = Button(self, self.size[0]*0.55, self.size[1]/2,
                                        'image//black_jack.png', 0.75).draw()
                        if self.communicate_2 == 'draw':
                            communicate_cancel = Button(self, self.size[0]*0.55, self.size[1]/2,
                                        'image//draw.png', 0.75).draw()
    
                    else:
    
                        if self.communicate == 'won':
                            communicate_cancel = Button(self, self.size[0]/2, self.size[1]/2,
                                        'image//won.png', 0.75).draw()
                        if self.communicate == 'lose':
                            communicate_cancel = Button(self, self.size[0]/2, self.size[1]/2,
                                    'image//lose.png', 0.75).draw()
                        if self.communicate == 'black_jack':
                            communicate_cancel = Button(self, self.size[0]/2, self.size[1]/2,
                                        'image//black_jack.png', 0.75).draw()
                        if self.communicate == 'draw':
                            communicate_cancel = Button(self, self.size[0]/2, self.size[1]/2,
                                        'image//draw.png', 0.75).draw()
    
    
                    # menu
                    if hit_btn:
                        # hit
                        if self.stage == 'card_revers_img':
                            self.engine.hit()
    
                    if stand_btn:
                        # stand
                        if self.stage == 'card_revers_img':
                            self.engine.stand()
    
                    if split_btn:
                        # split
                        if self.stage == 'card_revers_img' and self.check_split is False:
                            if self.engine.player.hand[0][0] == self.engine.player.hand[1][0]:
                                self.engine.split()
                            else:
                                self.engine.split_2()
                                self.engine.stand()
    
                    if double_btn:
                        if self.check_double:
                            self.engine.double(self.walet.bet)
                        elif self.check_double_2:
                            self.engine.double_2(self.walet.bet_2)
    
                    if surrender_btn:
                        if self.stage == 'card_revers_img':
                            self.engine.surrender()
                            self.engine.end_game()
                            self.communicate = ''
                            self.communicate_2 = ''
                            self.check_split = False
                            self.check_double = True
                            self.check_double_2 = True
                            self.stage = 'begin'
    
                    if leave_btn:
                        self.place = 'menu'
    
                    if card_revers_img:
                        if self.stage == 'begin':
                            if self.walet.bet > 0:
                                self.stage = 'card_revers_img'
                                self.check_krupier = 0
                                self.engine.start_game()
    
                    # popup
                    if communicate_cancel:
                        self.communicate = ''
                        self.communicate_2 = ''
    
    
                    # set bet
                    if chips_10:
                        if self.stage == 'begin':
                            self.walet.set_bet(10)
                            self.engine.end_game()
                            self.communicate = ''
                            self.communicate_2 = ''
                            self.check_split = False
                            self.check_double = True
                            self.check_double_2 = True
                            # self.move_chips(self.chips_10_button)
                    if chips_20:
                        if self.stage == 'begin':
                            self.walet.set_bet(20)
                            self.engine.end_game()
                            self.communicate = ''
                            self.communicate_2 = ''
                            self.check_split = False
                            self.check_double = True
                            self.check_double_2 = True
                            # self.move_chips(chips_20)
                    if chips_50:
                        if self.stage == 'begin':
                            self.walet.set_bet(50)
                            self.engine.end_game()
                            self.communicate = ''
                            self.communicate_2 = ''
                            self.check_split = False
                            self.check_double = True
                            self.check_double_2 = True
                            # self.move_chips(chips_50)
                    if chips_100:
                        if self.stage == 'begin':
                            self.walet.set_bet(100)
                            self.engine.end_game()
                            self.communicate = ''
                            self.communicate_2 = ''
                            self.check_split = False
                            self.check_double = True
                            self.check_double_2 = True
                            # self.move_chips(chips_100)
    
    
                    # Draw value of the walet
                    font = pygame.font.SysFont('system', 52)
                    text_surface = font.render(f'Walet: {self.walet.value:.0F}$', True, (0, 0, 0))
                    self.screen.blit(text_surface, dest=(self.size[0]*0.7, self.size[1]*0.65))
    
    
                    # Draw value of the bet
                    if self.check_split:
    
                        font = pygame.font.SysFont('system', 52)
                        text_surface = font.render(f'Bet: {self.walet.bet}$', True, (0, 0, 0))
                        self.screen.blit(text_surface, dest=(self.size[0]*0.7, self.size[1]*0.72))
    
                        font = pygame.font.SysFont('system', 52)
                        text_surface = font.render(f'Bet: {self.walet.bet_2}$', True, (0, 0, 0))
                        self.screen.blit(text_surface, dest=(self.size[0]*0.85, self.size[1]*0.72))
    
                    else:
    
                        font = pygame.font.SysFont('system', 52)
                        text_surface = font.render(f'Bet: {self.walet.bet}$', True, (0, 0, 0))
                        self.screen.blit(text_surface, dest=(self.size[0]*0.7, self.size[1]*0.72))
    
                    if self.walet.value < 10 and self.stage == 'card_revers_img' and \
                    (self.communicate == 'lose' or self.communicate_2 == 'lose'):
    
                        Button(self, self.size[0]/2, self.size[1]/2,
                                        'image//total_lose.png', 2).draw()
                
                self.tps_delta -=1/self.tps_max
            pygame.display.flip()

        pygame.quit


if __name__ == "__main__":
    Game()
    