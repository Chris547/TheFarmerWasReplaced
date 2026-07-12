import config

def move_to(x, y):
	move(North)

def planting(entity):
	if entity == Entities.Grass:
		if get_ground_type() != Grounds.Grassland:
			till()

	elif entity == Entities.Bush:
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Bush)

	elif entity == Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		if get_water() < config.water_carrot:
			use_item(Items.Water)