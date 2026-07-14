def absolute(x:int, y:int):
	relative(x - get_pos_x(), y - get_pos_y())

def relative(x:int, y:int):
	if x > 0:
		for n in range(0, x, 1):
			move(East)
	elif x < 0:
		for n in range(0, x, -1):
			move(West)
	if y > 0:
		for n in range(0, y, 1):
			move(North)
	elif y < 0:
		for n in range(0, y, -1):
			move(South)

def up(num = 1):
	for n in range(num):
		move(North)

def down(num = 1):
	for n in range(num):
		move(South)

def left(num = 1):
	for n in range(num):
		move(West)

def right(num = 1):
	for n in range(num):
		move(East)