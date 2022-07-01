"""
game black jack module. It is used to count the user's money
"""

class Walet():
    """ Class used to count the user's money, and manage it """


    def __init__(self):
        self.value = 10000
        self.bet = 0
        self.bet_2 = 0


    def add_value(self, add):
        """
        it is used to add money to walet

        Parameters
        ----------
        add : amount of bet money to add to walet (INT)
        """

        self.value += add
        self.bet = 0


    def add_value_2(self, add):
        """
        it is used to add money to walet

        Parameters
        ----------
        add : amount of bet_2 money to add to walet (INT)
        """

        self.value += add
        self.bet_2 = 0


    def set_bet(self, bet):
        """
        it is used to create bet and reduce the value of walet

        Parameters
        ----------
        bet : amount to increase bet (INT)

        Returns
        -------
        bool if user dont have enough money for bet - FALSE

        """

        if self.value >= bet:
            self.value -= bet
            self.bet += bet
        else:
            return False
        return None

    def set_bet_2(self, bet):
        """
        it is used to create bet and reduce the value of walet

        Parameters
        ----------
        bet : amount to increase bet_2 (INT)

        Returns
        -------
        bool if user dont have enough money for bet_2 - FALSE

        """

        if self.value >= bet:
            self.value -= bet
            self.bet_2 += bet
        else:
            return False
        return None
