import numpy as np
from termcolor import colored

__version__ = '0.1.0'

class conway_gol(object):
    def __init__(self, axis_length, sources):
        _x = [colored('■', 'white') for i in range(axis_length)]
        _y = [_x for i in range(axis_length)]
        self._version = __version__
        self._grid = np.array(_y)
        self._sources = []
        self._random_fill(sources)

    def _random_fill(self, n):
        for i in range(n):
            _x = np.random.randint(self._grid.shape[1])
            _y = np.random.randint(self._grid.shape[0])
            self._grid[_y][_x] = colored('■', 'yellow')
            for square in self._get_neighbours((_x, _y), True):
                self._grid[square[1]][square[0]] = colored('■', 'yellow')
            self._sources.append((_x, _y))

    def __str__(self):
        _out_str = ''
        for i in range(self._grid.shape[1]):
            for j in range(self._grid.shape[0]):
                _out_str += self._grid[i][j]
            _out_str += '\n'
        return _out_str

    def _get_neighbours(self, co_ords, no_diags=False, condition=None):
        _x, _y = co_ords
        _neighbours = [(_x+1,_y), (_x-1,_y),
                       (_x,_y-1), (_x,_y+1)]
        if not no_diags:
            _neighbours += [(_x+1,_y+1), (_x+1, _y-1),
                            (_x-1,_y+1), (_x-1, _y-1)]

        _neighbours = np.array(_neighbours)
        _out = []

        for n in _neighbours:
            try:
                self._grid[n[1]][n[0]]
                if condition:
                    if self._grid[n[1]][n[0]] == condition:
                        _out.append(n)
                else:
                    _out.append(n)
            except IndexError:
                continue

        return _out

    def run(self):
        from time import sleep
        from subprocess import call
        call("clear")
        print(self)
        sleep(0.1)
        call("clear")
        _tmp = np.copy(self._grid)
        while True:
            for j in range(self._grid.shape[1]):
                for i in range(self._grid.shape[0]):
                    if len(self._get_neighbours((i,j), condition=colored('■', 'yellow'))) > 3:
                        _tmp[j][i] = colored('■','white')
                    elif len(self._get_neighbours((i,j), condition=colored('■', 'yellow'))) < 2:
                        _tmp[j][i] = colored('■', 'white')
                    elif len(self._get_neighbours((i,j), condition=colored('■', 'yellow'))) == 3:
                        _tmp[j][i] = colored('■', 'yellow')
                    else:
                        continue
            self._grid = _tmp
            print(self)
            sleep(0.1)
            call("clear")
                    

if __name__ in "__main__":
    x = conway_gol(30,60)
    x._run()
