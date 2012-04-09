from ConfigParser import ConfigParser

from pk.terrain import Terrain, WEIGHT_KEYS
from pk.deck_data import CPK_AVERAGE_DECK
from pk.deck import Deck
from pk.table import Table


def main(config_file):
    forces = load_config(config_file)
    table = build_terrain(forces)
    table.save(config_file+'.txt')


def load_config(config_file):
    cp = ConfigParser()
    cp.read(config_file)
    forces = {}
    for s in cp.sections():
        forces[s] = {}
        for o in cp.options(s):
            forces[s][o] = cp.get(s,o)

    return forces


def build_terrain(forces):
    deck = Deck(CPK_AVERAGE_DECK)
    table = Table()
    for force, data in forces.iteritems():
        weights = dict(((key, data[key]) for key in data if key in WEIGHT_KEYS) )
        table[force] = Terrain(deck, weights)
    return table



if __name__ == '__main__':
    import sys
    import os

    args = sys.argv[1:]
    if len(args) == 0:
        print 'A configuration file must be specified'
        sys.exit(1)

    config_file = os.path.abspath(args[0])
    if not os.path.isfile(config_file):
        print 'Configuration file "%s" not found' % config_file
        sys.exit(1)

    main(config_file)
