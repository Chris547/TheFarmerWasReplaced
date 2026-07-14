import log
import config
import go
import world

def tree():
	go.up()
	go.right()
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	print("TREE!")
	go.left()
	go.up()

def put_pumpkin():
	set_ground_type(Grounds.Soil)
	plant(Entities.Pumpkin)
	world.set(get_pos_x(), get_pos_y(), "entity", Entities.Pumpkin)

def set_ground_type(ground_type:Grounds):
	if get_ground_type() != ground_type:
		till()
		world.set(get_pos_x(), get_pos_y(), "ground", Grounds.Soil)
