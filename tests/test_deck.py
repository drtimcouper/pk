from nose.tools import *

from pk.deck_data import CPK_AVERAGE_DECK
import pk.deck as pkd


class Test_Deck(object):

    def setup(self):
        self.deck = pkd.Deck(CPK_AVERAGE_DECK)

    def test_constructor(self):
        assert_equals(len(self.deck), 33)

    def test_next(self):
        c = self.deck.next()
        assert c in CPK_AVERAGE_DECK, c

    def test_deal_all(self):
        try:
            for c in self.deck:
                print c
        except pkd.EndOfDeckException:
            return
        assert False, 'Failed to raise EndOfDeckException'

