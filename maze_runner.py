import random
from cell import Cell

# returns maze with dimension dim with probability p of a cell being occupied
def get_maze(dim, p):
	maze = []
	basic_maze = []

	for row in xrange(dim):
		maze.append([])
		basic_maze.append([])
		for col in xrange(dim):
			if random.random()<p:
				# occupied cell
				maze[row].append(Cell(1))
				basic_maze[row].append(1) 
			else:
				# empty cell
				maze[row].append(Cell(0))
				basic_maze[row].append(0) 

	# start cell
	maze[0][0] = Cell(2) 
	basic_maze[0][0] = 0
	# goal cell
	maze[dim-1][dim-1] = Cell(3) 
	basic_maze[dim-1][dim-1] = 0
	return maze, basic_maze

dim = 10
p = 0.3
maze, basic_maze = get_maze(dim, p)

import seaborn as sns
import matplotlib.pyplot as plt
ax = sns.heatmap(basic_maze, cmap="Blues", cbar=False, linewidths=.1, linecolor="Black")
plt.show()

# import matplotlib as mpl
# from matplotlib import pyplot
# import numpy as np

# bounds=[-1, 2]
# cmap = mpl.colors.ListedColormap(['white','black'])
# norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# # tell imshow about color map so that only set colors are used
# img = pyplot.imshow(basic_maze,interpolation='nearest',
#                     cmap=cmap, norm=norm)

# pyplot.show()