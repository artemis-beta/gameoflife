from gameoflife import conway_gol

_intro = '''
{b}
    Game of Life Simulation
             v{v}
{b}
'''.format(b='='*30, v=conway_gol(0,0)._version)


print(_intro)
grid_size = input('Enter Grid Axis Size: ')
n_source  = input('Enter Number of Sources: ')

conway_gol(int(grid_size), int(n_source)).run()
