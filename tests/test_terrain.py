from nose.tools import *

import pk.terrain as pkt
import pk.deck as pkd
from pk.deck_data import CPK_AVERAGE_DECK

def test_terrain_grid_constructed_ok():
    deck = pkd.Deck(CPK_AVERAGE_DECK)
    t = pkt.Terrain(deck)
    assert_equals(len(t.grid), 8)

def test_terrain_default_weights_constructed_ok():
    deck = pkd.Deck(CPK_AVERAGE_DECK)
    t = pkt.Terrain(deck)
    assert_almost_equal(t.weights['light'], 1./3)
    assert_almost_equal(t.weights['medium'], 1./3)
    assert_almost_equal(t.weights['heavy'], 1./3)

def test_terrain_weights_constructed_ok():
    deck = pkd.Deck(CPK_AVERAGE_DECK)
    myweights = {'light':1, 'medium': 2, 'heavy': 3}
    t = pkt.Terrain(deck, myweights)
    assert_almost_equal(t.weights['light'], 1./6)
    assert_almost_equal(t.weights['medium'], 1./3)
    assert_almost_equal(t.weights['heavy'], 1./2)

def test_terrain_no_weights():
    deck = pkd.Deck(CPK_AVERAGE_DECK)
    t = pkt.Terrain(deck)
    assert_almost_equal(t.weights['light'], 1./3)
    assert_almost_equal(t.weights['medium'], 1./3)
    assert_almost_equal(t.weights['heavy'], 1./3)

def test_terrain_zero_weights():
    deck = pkd.Deck(CPK_AVERAGE_DECK)
    myweights = {'light':0}
    t = pkt.Terrain(deck, myweights)
    assert_almost_equal(t.weights['light'], 1./3)
    assert_almost_equal(t.weights['medium'], 1./3)
    assert_almost_equal(t.weights['heavy'], 1./3)

