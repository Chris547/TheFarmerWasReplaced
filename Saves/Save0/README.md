# What is this mess?
I started out brute forcing my way to some of the basic unlocks.  Now I'm beginning to transition toward a set of reusable components.  I lack the dictionary unlock, so I made my own simple implementation using lists of tuples and helper functions that I'll swap out later to make the same structures more efficient.

## go.py
- `absolute(x, y)`
    - Move from anywhere to the tile with absolute x/y world coordinates.
- `relative(x, y)`
    - Move x/y number of tiles relative to current position.  Positive x/y moves right/up.  Negative x/y moves left/down.

## world.py
- `state[x][y][(k, v)]`
    - Represents the state of various properties of the game world as a list of lists of lists of tuples.
- `get(x, y, key)`
    - Helper function to provide dictionary-like read access to the key-value tuples.
- `set(x, y, key, value)`
    - Helper function to provide dictionary-like write access to the key-value tuples.