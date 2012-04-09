from pk.deck import Deck
from pk.terrain_data import LIGHT, MEDIUM, HEAVY, BASELINE, FLANK, CENTER
import random

random.seed()

WEIGHT_KEYS = ('light', 'medium', 'heavy')

class Terrain(object):
    def __init__(self, deck, weights=None):
        self.deck = deck
        if weights is None:
                self.weights = {'light': 1, 'medium': 1, 'heavy': 1}
        else:
                self.weights = weights
        total_weights = sum((float(v) for v in self.weights.itervalues()))
        self.weights = dict((k, float(v)/total_weights) for k,v in self.weights.iteritems())
        self.build()

    def build(self):
        self.cgrid = {}
        for x in xrange(4):
            for y in xrange(2):
               self.cgrid[(x,y)] = self.deck.next()
        self.render()

 # Flank is [(0,1)] and [(3,1)]
 # Center is [(1,1)]  and [(2,1)]
 # Baseline is [(0,0)] ..[(0,3)]
    def select_weight(self):
        p = random.random()
        if p <self.weights['light']:
                return LIGHT
        elif p < self.weights['light'] + self.weights['medium']:
                return MEDIUM
        else:
                return HEAVY

    def render(self):
        self.grid = {}
        for y in xrange(2):
            for x in xrange(4):
                # determine LIGHT/MEDIUM/HEAVY:
                # select the weight dictionary for this cell
                tdict = self.select_weight()

                # determine type:
                if y == 0:
                    ttype = BASELINE
                elif x in (0,3):
                    ttype = FLANK
                else:
                    ttype = CENTER

                self.grid[(x,y)]  = tdict[ttype][self.cgrid[(x,y)]]
