from cards import Cards

#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                  Gokberk Gulgun                     #
#                   Psychic Poker                     #
#                                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################

class FileParse (object) :

    def __init__(self, file):
        """!@brief Create File object
        """
        self.file = file
        self.file_handler = ''

    def open_file(self):
        """!@brief Open file
        """
        self.file_handler = open(self.file, 'r')

    def read_gamble_cards(self):
        """!@brief Reading poker cards
        """
        self.open_file()
        gambles = []
        for line in self.file_handler:
            cards = self.read_cards(line)
            gambles.append(cards)
        return gambles

    def read_cards(self, line):
        """!@brief Create card objects according to current desk and current hand values
        """
        line_split = line.split(" ")
        cards = []
        for card in line_split:
            simple_card = (Cards(card[0],card[1]))
            cards.append(simple_card)
        return cards