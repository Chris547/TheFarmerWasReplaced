import config
import log
import world

def planting(entity):
	x = get_pos_x()
	y = get_pos_y()
	
	if get_entity_type() == entity:
		log.warn("do.planting", (entity, x, y, "ALREADY EXISTS"))
		return False
	
	harvest()
	world.set(x, y, "entity", get_entity_type())

	if entity == Entities.Grass:
		if get_ground_type() != Grounds.Grassland:
			till()
			world.set(x, y, "ground", get_ground_type())
			world.set(x, y, "entity", get_entity_type())

	elif entity == Entities.Bush:
		if get_ground_type() != Grounds.Grassland:
			till()
			world.set(x, y, "ground", get_ground_type())
			world.set(x, y, "entity", get_entity_type())
		if plant(Entities.Bush):
			world.set(x, y, "entity", get_entity_type())

	elif entity == Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()
			world.set(x, y, "ground", Grounds.Soil)
			world.set(x, y, "entity", get_entity_type())
		if plant(Entities.Carrot):
			world.set(x, y, "entity", get_entity_type())
		if get_water() < config.water_carrot:
			use_item(Items.Water)
			world.set(x, y, "water", get_water())
