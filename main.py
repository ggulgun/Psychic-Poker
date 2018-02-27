# -*- coding: utf-8 -*-

from file_parser import FileParse
from const import _Const
from poker_machine import PokerMachine


#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                  Gokberk Gulgun                     #
#                   Psychic Poker                     #
#                                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################

CONST = _Const()


"""
    Psychic Poker class :
    Main class

"""
class PsychicPoker(object):


    def __init__(self, file):
        """!@brief File parsing operation
            @param file  File of the input
        """
        self.fileParser = FileParse(file)

    def compute_player_best_hand(self):
        """!@brief Computing best player hand
        """
        gamble_cards_list = self.fileParser.read_gamble_cards()
        for gamble in gamble_cards_list:
            non_edited_current_hand = gamble[0:5]
            non_edited_current_deck = gamble[5:10]
            current_hand = gamble[0:5]
            current_deck = gamble[5:10]
            machine = PokerMachine(current_hand, current_deck)
            machine.calculate_best_choose()
            self.print_result(machine,non_edited_current_hand,non_edited_current_deck)



    def print_result(self,machine,current_hand,current_deck):
        """!@brief Result Printing
        """
        print "Hand %s Deck %s Best Hand %s (%s) " % (machine.to_string(current_hand), machine.to_string(current_deck),
                                                      machine.to_string(machine.getChoosableHand()),
                                                      CONST.possible_hands_value[machine.getChoosableHandValue()])



if __name__ == "__main__":
    psychic_poker = PsychicPoker('poker_input')
    psychic_poker.compute_player_best_hand()
