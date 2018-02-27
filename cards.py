# -*- coding: utf-8 -*-
from const import _Const

#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                  Gokberk Gulgun                     #
#                   Psychic Poker                     #
#                                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################


CONST = _Const()

"""
    Definition Of Cards Class
"""
class Cards(object) :

    """
        init function
        binding card values into numbers
    """
    def __init__(self, card_value, card_type) :

        self.card_value = card_value
        self.card_type = str(card_type).upper()

        self.string_card_value = card_value

        self.numerical_card_value = (CONST.card_values.get(self.card_value) or int(self.card_value))


    def getCardValue(self):
        return self.numerical_card_value

    def getStringCardValue(self):
        return self.card_value


    def getCardType(self):
        return self.card_type


