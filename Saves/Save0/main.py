import config
import world
import do
import go
import garden

# NOTE: clear() does not reset watering state to 0.
clear()

while True:
	# Set goal
	#goal = "create_pumpkins"
	#print(goal)

	# Check goals

	# Execute steps
	# plant 100% pumpkins
	for x in range(0, get_world_size()):
		for y in range(0, get_world_size()):
			garden.put_pumpkin()
			go.absolute(x, y)
		
