#TODO: dictionary
want_items = [
	(Items.Hay, 0.5),
	(Items.Wood, 1.0),
	(Items.Carrot, 0.5),
	(Items.Pumpkin, 0.5),
	(Items.Water, 0)
	]

def get_want_item(item):
	for (k, v) in want_items:
		if k == item:
			return v
	return None



# Water Levels
water_carrot = .5

# Planting Pattern
plant_pattern = [
	#Entities.Grass,
	Entities.Bush,
	#Entities.Carrot
	]