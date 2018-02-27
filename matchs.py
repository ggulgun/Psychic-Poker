
from abc import abstractmethod
from const import _Const

#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                  Gokberk Gulgun                     #
#                   Psychic Poker                     #
#                                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################

CONST = _Const()


class Matchs(object):

    @abstractmethod
    def match(self, hand):
        pass

    @abstractmethod
    def rank(self):
        pass


class StraightFlushHand(Matchs):
    """
    Straight Flush Hand
    """

    def match(self, cards):
        return self.is_straight(cards) and self.is_flush(cards)

    def is_straight(self, cards):
        if cards[1].getCardValue() == (cards[0].getCardValue() + 1) % 15 and cards[2].getCardValue() == (
                cards[0].getCardValue() + 2) % 15 and cards[3].getCardValue() == (cards[0].getCardValue() + 3) % 15 and cards[4].getCardValue() == (cards[0].getCardValue() + 4) % 15:
            return True
        if cards[0].getCardValue() == 1 and cards[1].getCardValue() == (cards[0].getCardValue() + 24) % 15 and cards[2].getCardValue() == (
                cards[1].getCardValue() + 1) % 15 and cards[3].getCardValue() == (cards[1].getCardValue() + 2) % 15 and cards[4].getCardValue() == (cards[1].getCardValue() + 3) % 15 :
            return True
        return False

    def is_flush(self, cards):
        for i in range(1, CONST.get_size_of_hand):
            if cards[i].getCardType() != cards[0].getCardType():
                return False
        return True

    def rank(self):
        return 8



class FourOfKindHand(Matchs):
    """
    Four of a kind
    """
    def match(self, cards):
        for i in range(0, CONST.get_size_of_hand - 3):
            if cards[i].getCardValue() == cards[i + 1].getCardValue() and cards[i].getCardValue() == cards[i + 2].getCardValue() and cards[i].getCardValue() == cards[i + 3].getCardValue():
                return True
        return False

    def rank(self):
        return 7



class FullHouseHand(Matchs):
    """
    Full house
    """
    def match(self, cards):
        if (cards[0].getCardValue() == cards[1].getCardValue() and cards[0].getCardValue() == cards[2].getCardValue()) and (cards[3].getCardValue() == cards[4].getCardValue()):
            return True
        return False

    def rank(self):
        return 6


class FlushHand(Matchs):
    """
    Flush
    """

    def match(self, cards):
        for i in range(1, CONST.get_size_of_hand):
            if cards[i].getCardType() != cards[0].getCardType():
                return False
        return True

    def rank(self):
        return 5


class StraightHand(Matchs):
    """
    Straight
    """

    def match(self, cards):
        if cards[1].getCardValue() == (cards[0].getCardValue() + 1) % 15 and cards[2].getCardValue() == (cards[0].getCardValue() + 2) % 15 and cards[3].getCardValue() == (cards[0].getCardValue() + 3) % 15 and cards[
            4].getCardValue() == (cards[0].getCardValue() + 4) % 15:
            return True
        if cards[0].getCardValue() == 1 and cards[1].getCardValue() == (cards[0].getCardValue() + 24) % 15 and cards[2].getCardValue() == (
                cards[1].getCardValue() + 1) % 15 and cards[3].getCardValue() == (cards[1].getCardValue() + 2) % 15 and cards[4].getCardValue() == (cards[1].getCardValue() + 3) % 15 :
            return True
        return False

    def rank(self):
        return 4


class ThreeOfKindHand(Matchs):
    """
    Three of a kind
    """
    def match(self,cards):
        for i in range(0, CONST.get_size_of_hand - 2):
            if cards[i].getCardValue() == cards[i + 1].getCardValue() and cards[i].getCardValue() == cards[i + 2].getCardValue():
                return True
        return False

    def rank(self):
        return 3


class TwoPairsHand(Matchs):
    """
    Two Pairs
    """

    def match(self,cards):
        for i in range(0, CONST.get_size_of_hand - 1):
            if cards[i].getCardValue() == cards[i + 1].getCardValue():
                for j in range(i + 2, CONST.get_size_of_hand - 1):
                    if cards[j].getCardValue() == cards[j + 1].getCardValue():
                        return True
        return False


    def rank(self):
        return 2



class OnePairHand(Matchs):
    """
    One pair
    """

    def match(self, cards):
        for i in range(0, CONST.get_size_of_hand - 1):
            if cards[i].getCardValue() == cards[i + 1].getCardValue():
                return True
        return False

    def rank(self):
        return 1



matchs = (OnePairHand,
          TwoPairsHand,
          ThreeOfKindHand,StraightHand,FlushHand,FullHouseHand,FourOfKindHand,StraightFlushHand)