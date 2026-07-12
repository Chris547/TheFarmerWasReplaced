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
	while num_items(Items.Pumpkin) < 4000:
		# Execute steps
		# plant 100% pumpkins
		do.planting(Entities.Carrot)
