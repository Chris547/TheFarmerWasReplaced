# What is this mess?
I started out brute forcing my way to some of the basic unlocks.  Now I'm beginning to transition toward a set of reusable components.  I lack the dictionary unlock, so I made my own simple implementation using lists of tuples and helper functions that I'll swap out later to make the same structures more efficient.

## world.py
- `state[x][y][(k,v)]`
  Represents the state of various properties of the game world as a list of lists of lists of tuples.
- `get(x,y,key)`
  Helper function to provide dictionary-like read access to the key-value tuples.
- `set(x,y,key,value)`
  Helper function to provide dictionary-like write access to the key-value tuples.