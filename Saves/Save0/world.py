#TODO: optimize with dictionary

# initialize state to a default grid of grassland tiles
state = []
for x in range(0, get_world_size()):
	state.append([])
	for y in range(0, get_world_size()):
		state[x].append([
			("ground", Grounds.Grassland),
			("entity", Entities.Grass),
			("water", 0)
		])

# get a value
def get(x, y, key):
	for (k, v) in state[x][y]:
		if k == key:
			quick_print("DEBUG: world.get", x, y, k, v)
			return v
	quick_print("ERROR: world.get", x, y, key, "(KEY DOES NOT EXIST)")
	return None

# set a value (key must already exist)
def set(x, y, key, value):
	for (k, v) in state[x][y]:
		if k == key:
			quick_print("DEBUG: world.set", x, y, k, v, value)
			state[x][y].remove((k,v))
			state[x][y].append((k,value))
			return True
	quick_print("ERROR: world.set", x, y, key, value, "(KEY DOES NOT EXIST)")
	return False

# tests
#quick_print("DEBUG: state", state)
#get(0,0,"ground")
#set(0,0,"ground",Grounds.Soil)
#get(0,0,"ground")
#get(5,5,"ground")
#get(6,6,"ground")
#quick_print("DEBUG: state", state)
#quick_print("INFO: world initialized")