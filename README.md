# Game of Life

*Still under development*

Simulation based on Conway's game of life whereby a set of life sources remain alive or die depending on the population of their surroundings.

## Installation
From within a virtual environment run:
`pip install .`
within the directory.

The package comes with a mini app:
`python app.py`
or the class can be imported:
```
from gameoflife import conway_gol

grid_size        = 10
num_life_sources = 7

conway_gol(grid_size, num_life_sources).run()
```
