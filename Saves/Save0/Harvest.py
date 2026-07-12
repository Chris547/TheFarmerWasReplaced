import world
import do
import go
import garden
import config

clear()
while True:
	# Set goal
	goal = "create_pumpkins"
	print(goal)

	# Check goals
	while num_items(Items.Pumpkin) < 4000:
		# Execute steps
		# plant 100% pumpkins
		plant(Entities.Pumpkin)
