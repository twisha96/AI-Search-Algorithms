import random
from cell import Cell

# returns maze with dimension dim with probability p of a cell being occupied
def get_maze(dim, p):
	maze = []
	for row in xrange(dim):
		maze.append([])
		for col in xrange(dim):
			if p < random.random():
				# occupied cell
				maze[row].append(Cell(1))
			else:
				# empty cell
				maze[row].append(Cell(0))
	# start cell
	maze[0][0] = Cell(2) 
	# goal cell
	maze[dim-1][dim-1] = Cell(3) 
	return maze

dim = 10
p = 0.5
maze = get_maze(dim, p)