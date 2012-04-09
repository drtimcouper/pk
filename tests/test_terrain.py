from nose.tools import *

import pk.terrain as pkt
import pk.deck as pkd

def test_terrain():
    deck = pkd.Deck()
    t = pkt.Terrain(deck)
    assert_equals(len(t.grid), 8)
