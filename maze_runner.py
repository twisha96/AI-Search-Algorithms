import random
from cell import Cell

# import the visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt

# returns maze with dimension dim with probability p of a cell being occupied
def get_maze(dim, p):
	maze = []

	for row in xrange(dim):
		maze.append([])
		for col in xrange(dim):
			if random.random()<p:
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


def get_path(x, y, maze):
	path = []
	while((x,y)!=(0,0)):
		print((x,y))
		path.insert(0,(x,y))
		(x, y) = maze[x][y].parent
	path.insert(0,(0,0))
	return path


def visualize_maze(maze):
	basic_maze = []
	dim = len(maze)
	for i in range(len(maze)):
		basic_maze.append([])
		for j in range(len(maze[0])):
			basic_maze[i].append(maze[i][j].value)

	basic_maze[0][0]=0
	basic_maze[dim-1][dim-1]=0

	ax = sns.heatmap(basic_maze, cmap="Blues", cbar=False, linewidths=.1, linecolor="Black")
	plt.show()

def trace_path(maze, path):
	basic_maze = []
	for i in range(len(maze)):
		basic_maze.append([])
		for j in range(len(maze[0])):
			basic_maze[i].append(maze[i][j].value)

	for i in range(len(path)):
		coordinates = path[i]
		basic_maze[coordinates[0]][coordinates[1]] = 0.5

	ax = sns.heatmap(basic_maze, cmap="Blues", cbar=False, linewidths=.1, linecolor="Black")
	plt.show()
