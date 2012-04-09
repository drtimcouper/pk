"""This holds the classes relating to cards
"""

import random
from pk.deck_data import AVERAGE_DECK


class EndOfDeckException(Exception):
    pass


class Deck(object):

    def __init__(self, deck_dict=AVERAGE_DECK):
        self.cards = []
        self.iter = -1
        for c, n in deck_dict.iteritems():
            for i in xrange(n):
                self.cards.append(c)
        self.shuffle()

    def shuffle(self) :
        """create the shufflelist of the integers which define the set of cards
        """
        random.shuffle(self.cards)

    def __iter__(self) :
        self.iter = -1
        return self

    def next(self):
        self.iter += 1
        if self.iter >= len(self.cards):
            raise EndOfDeckException
        return self.cards[self.iter]

    def __len__(self):
        return len(self.cards)
