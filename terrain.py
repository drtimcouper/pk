from pk.deck import Deck
from pk.terrain_data import LIGHT, MEDIUM, HEAVY, BASELINE, FLANK, CENTER
import random


class Terrain(object):
    def __init__(self, deck):
        self.deck = deck

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

    def render(self):
        self.grid = {}
        for y in (1,0):
            for x in xrange(4):
                # determine LIGHT/MEDIUM/HEAVY:
                weight = random.randint(1, 3)
                if weight == 1:
                    tdict = LIGHT
                elif weight == 2:
                    tdict = MEDIUM
                else:
                    tdict = HEAVY
                # determine type:
                if y == 0:
                    ttype = BASELINE

                elif x in (0,3):
                    ttype = FLANK
                else:
                    ttype = CENTER

                self.grid[(x,y)]  = tdict[ttype][self.cgrid[(x,y)]]
