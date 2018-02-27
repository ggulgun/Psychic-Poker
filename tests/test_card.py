import sys
sys.path.append('../')

from cards import *
import unittest





class TestCard(unittest.TestCase) :

    def test_valid_card_type(self):

        self.assertEquals(Cards(2,"c").getCardType(),Cards(2,"C").getCardType())

        self.assertEquals(Cards(2,"d").getCardType(),Cards(2,"D").getCardType())

        self.assertEquals(Cards(2,"h").getCardType(),Cards(2,"H").getCardType())

        self.assertEquals(Cards(2,"s").getCardType(),Cards(2,"S").getCardType())


    def test_valid_card_value(self):

        self.assertEquals(Cards("A","c").getCardValue(),Cards(1,"C").getCardValue())

        self.assertEquals(Cards("T","c").getCardValue(),Cards(10,"C").getCardValue())

        self.assertEquals(Cards("J","c").getCardValue(),Cards(11,"C").getCardValue())

        self.assertEquals(Cards("Q","c").getCardValue(),Cards(12,"C").getCardValue())

        self.assertEquals(Cards("K","c").getCardValue(),Cards(13,"C").getCardValue())


if __name__ == '__main__':
   unittest.main()

