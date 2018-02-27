

#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                  Gokberk Gulgun                     #
#                   Psychic Poker                     #
#                                                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################

def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)


"""
    Constant variables definition
"""
class _Const(object):
    @constant
    def card_type_nums():
        return 13

    @constant
    def card_values():
        return {'A': 1, 'K': 13,'Q' : 12,'J':11,'T':10}

    @constant
    def card_tonormal_values():
        return {'1': 'A', '13': 'K', '12': 'Q', '11': 'J', '10': 'T','9': '9','8':'8','7':'7','6':'6','5':'5','4':'4','3':'3','2':'2'}

    @constant
    def possible_hands_value():
        return {0:'high-card', 1:'one-pair', 2:'two-pairs', 3:'three-of-a-kind', 4:'straight', 5:'flush', 6:'full-house', 7:'four-of-a-kind', 8:'straight-flush'}

    @constant
    def get_size_of_hand():
        return 5

    @constant
    def card_types_num():
        return 4

    @constant
    def card_types():
        return "CDHS"
