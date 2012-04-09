import os.path

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

