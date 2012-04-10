
import random
from ConfigParser import ConfigParser

from pk.deck import Deck
from pk.terrain_data import LIGHT, MEDIUM, HEAVY, BASELINE, FLANK, CENTER
from pk.deck_data import CPK_AVERAGE_DECK

FORCE_DEFAULTS = ['Blue', 'Red']

class Terrain(object):
    def __init__(self, deck, weights=None):
        self.deck = deck
        self.weights = self.calc_weights(weights)
        self.build()

    def calc_weights(self, weights):

        if weights is None:
            return {'light': 1./3, 'medium': 1./3, 'heavy': 1./3}

        total_weights = sum((float(v) for v in weights.itervalues()))

        if total_weights == 0:
            return {'light': 1./3, 'medium': 1./3, 'heavy': 1./3}
        else:
            return dict((k, float(v)/total_weights) for k,v in weights.iteritems())

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

# -------

CELL_WIDTH = 25
LINE_WIDTH = (CELL_WIDTH*4 + 5)
DASH_LINE = '-'*LINE_WIDTH + '\n'
BLANK_LINE = '|' + ' '*CELL_WIDTH
BLANK_LINE = BLANK_LINE*4 + '|\n'

top = DASH_LINE+ BLANK_LINE*2
bottom = BLANK_LINE*2

class Table(dict):

    def organise(self, force, first):
        """arrange the grid correctly into one big grid
        """
        grid = self[force].grid
        keys = grid.keys()
        if first:
            # we want y=0 followed by y=1
            order = [(y,x, grid[(x,y)]) for (x,y) in keys]
        else:
            # we want y=1 followed by y=0
             order = [(3-y,x,grid[(x,y)] )for (x,y) in keys]

        order.sort()
        nice = {}
        for y, x,  text in order:
            try:
                nice[y].append(text)
            except KeyError:
                nice[y] = [text]

        return nice

    def save(self, fn):
        """writes the pictoral representation of thte terrain objects held in the
        dictionary as a text form"""

        with open(fn, 'w') as f:
            first = True
            for force in self.iterkeys():
                if first:
                    f.write(fit(force, LINE_WIDTH))
                    f.write('\n')
                nicegrid = self.organise(force, first)
                keys = sorted(nicegrid.keys())
                for  k in keys:
                    v = nicegrid[k]
                    f.write(top)
                    for w in v:
                        f.write(line(str(w),CELL_WIDTH))
                    f.write('|\n')
                    f.write(bottom)

                if not first:
                    f.write(DASH_LINE)
                    f.write(fit(force,LINE_WIDTH))
                    f.write('\n')

                first = False

        print 'File "%s" created' % os.path.abspath(fn)

def line(word, n):
    return '|' + fit(word, n)


def fit(word, n):
    if len(word)<=n:
        s =  (n - len(word))/2
        filled = ' '*s + word + ' '*s
        while len(filled) < n:
            filled += ' '
        return filled
    else:
        return word[:n]


def main(config_file):
    forces, terrain = load_config(config_file)

    while len(forces) < 2:
        forces[FORCE_DEFAULTS.pop()] = {}

    table = build_terrain(forces, terrain)
    if config_file is None:
       config_file = 'no_config'

    output_file = config_file + '.txt'
    table.save(output_file)

def load_config(config_file):

    forces = {}
    terrain = {}

    if config_file is not None:
        cp = ConfigParser()
        cp.read(config_file)
        for s in cp.sections():
            if s == 'terrain':
                for o in cp.options(s):
                    terrain[o] = cp.get(s,o)
            else:
                forces[s] = {}
                for o in cp.options(s):
                    forces[s][o] = cp.get(s,o)

    return forces, terrain


def build_terrain(forces, terrain):
    deck = Deck(CPK_AVERAGE_DECK)
    table = Table()
    weights = {'light': 0, 'medium': 0, 'heavy': 0}
    for ttype, value in terrain.iteritems():
        if ttype in weights:
            weights.update({ttype: value})
        else:
            raise ValueError('Invalid terrain type specified: "%s"' % ttype)

    for force, data in forces.iteritems():
        table[force] = Terrain(deck, weights)
    return table


if __name__ == '__main__':
    import sys
    import os

    args = sys.argv[1:]
    if len(args) == 0:
        config_file = None

    else:
        config_file = os.path.abspath(args[0])
        if not os.path.isfile(config_file):
            print 'Configuration file "%s" not found' % config_file
            sys.exit(1)

    random.seed()
    main(config_file)
