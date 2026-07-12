import config
import go

def tree():
	go.up()
	go.right()
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	print("TREE!")
	go.left()
	go.up()