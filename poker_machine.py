from cards import Cards
from const import _Const
from  matchs import *


#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                  Gokberk Gulgun                     #
#                   Psychic Poker                     #
#                                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################


CONST = _Const()

"""
    Poker Machine class :
    Game Class

"""
class PokerMachine(object):


    def __init__(self, hand_cards, desk_cards):
        """!@brief Creates PokerMachine Element
            @param hand_cards Current User Cards
            @param desk_cards Current Desk Cards
        """

        self.hand_value = 0
        self.hand_cards = hand_cards
        self.desk_cards = desk_cards
        self.choosable_hand = []

    def to_string(self, cards):
        """!@brief Result printing
            @param cards Cards Object
        """
        output = ''
        for card in cards:
            output = output + (CONST.card_tonormal_values.get(str(card.getCardValue()))) + card.getCardType() + " "
        return output


    def sortByValue(self,deck):
        """!@brief Sorting cards
            @param deck current_deck
        """
        deck.sort(key=lambda val: val.numerical_card_value, reverse=False)


    def getChoosableHand(self):
        """!@brief Returns choosable hand
        """
        return self.choosable_hand

    def getChoosableHandValue(self):
        """!@brief Biggest hand value in deck
        """
        return self.hand_value



    def calculate_best_choose(self):
        """!@brief Calculation best choose in deck
        """

        self.sortByValue(self.hand_cards)

        resource_hand = [Cards(0, 0) for x in range(0, CONST.get_size_of_hand)]

        for i in range(0, CONST.get_size_of_hand):
            desk_card = Cards(self.desk_cards[i].getCardValue(), self.desk_cards[i].getCardType())
            resource_hand[i] = desk_card
            self.calculateHandValues(resource_hand,i+1,0)


    def createFoundHand(self,resource):
        """!@brief Creation of found hand
        """
        found_hand = []
        for currentHandItem in range(0, CONST.get_size_of_hand):
            found_hand.append(resource[currentHandItem])

        self.sortByValue(found_hand)
        return found_hand


    def calculateHandValues(self,resource,startPosition,endPosition):
        """!@brief Calculation hand values by poker rules
        """
        if startPosition == 5:
            found_hand = self.createFoundHand(resource)
            if StraightFlushHand().match(found_hand) and self.hand_value < StraightFlushHand().rank() :
                self.hand_value = StraightFlushHand().rank()
                self.choosable_hand = found_hand
            elif FourOfKindHand().match(found_hand) and self.hand_value < FourOfKindHand().rank() :
                self.hand_value = FourOfKindHand().rank()
                self.choosable_hand = found_hand
            elif FullHouseHand().match(found_hand) and self.hand_value < FullHouseHand().rank() :
                self.hand_value = FullHouseHand().rank()
                self.choosable_hand = found_hand
            elif FlushHand().match(found_hand) and self.hand_value < FlushHand().rank() :
                self.hand_value = FlushHand().rank()
                self.choosable_hand = found_hand
            elif StraightHand().match(found_hand) and self.hand_value < StraightHand().rank() :
                self.hand_value = StraightHand().rank()
                self.choosable_hand = found_hand
            elif ThreeOfKindHand().match(found_hand) and self.hand_value < ThreeOfKindHand().rank() :
                self.hand_value = ThreeOfKindHand().rank()
                self.choosable_hand = found_hand
            elif TwoPairsHand().match(found_hand) and self.hand_value < TwoPairsHand().rank() :
                self.hand_value = TwoPairsHand().rank()
                self.choosable_hand = found_hand
            elif OnePairHand().match(found_hand) and self.hand_value < OnePairHand().rank() :
                self.hand_value = OnePairHand().rank()
                self.choosable_hand = found_hand
            return

        for i in range(endPosition, CONST.get_size_of_hand):
            resource[startPosition] = self.hand_cards[i]
            self.calculateHandValues(resource, startPosition + 1, i + 1)
        return



