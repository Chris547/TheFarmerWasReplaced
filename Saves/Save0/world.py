import log

#TODO: optimize with dictionary
#TODO: or optimize into multiple indexed columns instead an indexed list of tuples.

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
def get(x:int, y:int, key:string):
	for (k, v) in state[x][y]:
		if k == key:
			log.debug("world.get", (x, y, k, v))
			return v
	log.error("world.get", ("KEY DOES NOT EXIST", x, y, key))
	return None

# set a value (key must already exist)
def set(x:int, y:int, key:string, value:Any):
	for (k, v) in state[x][y]:
		if k == key:
			state[x][y].remove((k,v))
			state[x][y].append((k,value))
			log.debug("world.set", (x, y, k, v, value))
			return True
	log.error("world.set", ("KEY DOES NOT EXIST", x, y, key, value))
	return False

# tests
#log.debug("world.state", state)
#get(0,0,"ground")
#set(0,0,"ground",Grounds.Soil)
#get(0,0,"ground")
#get(5,5,"ground")
#get(6,6,"ground")
#log.debug("world.state", state)
#log.info("world", "initialized")