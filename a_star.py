import math
import copy 
import maze_runner
from Queue import PriorityQueue
import pdb

# Given a co-ordinate (x,y), calculates the manhattan distance from the destination (dim-1, dim-1)
def manhattan_heuristic(x, y, dim):
	return abs(x - dim)+abs(y - dim)

# Given a co-ordinate (x,y), calculates the euclidian distance from the destination (dim-1, dim-1)
def euclidian_heuristic(x, y, dim):
	return math.sqrt((x - dim)**2+(y - dim)**2)

# Given a co-ordinate (x,y), calculates the length of path traversed to reach (x,y) from source (0, 0)
def source_dist(x, y, maze):
	path = maze_runner.get_path(x, y, maze)
	return len(path)

"""
checks for valid neighbours which are not yet explored by any other cell 
i.e. it is neither in the fringe nor in the closed set
and adds them to the fringe based on a priority. 
Priority for each cell is calculated using two functions:
1. f(x): distance traversed from source to point (x,y) 
2. h(x): heuristic function that estimates the distance from (x,y) to destination
Fringe is implemented using a Priority Queue. 
The order of exploration of cells does not matter as the fringe
is sorted based on the priority assigned the cell.
"""
def get_neighbors(maze, x, y, dim, heuristic, fringe):
	source_distance = source_dist(x, y, maze) 
	if(x-1>=0 and maze[x-1][y].value!=1 and not maze[x-1][y].visited): #(x-1,y) not in closed_set
			maze[x-1][y].visited = True
			maze[x-1][y].parent = (x,y)
			if heuristic == "manhattan":
				priority_value = (source_distance + 1) + manhattan_heuristic(x-1, y, dim)
			elif heuristic == "euclidian":
				priority_value = (source_distance + 1) + euclidian_heuristic(x-1, y, dim)
			fringe.put((priority_value, (x-1, y)))
			
	# bottom neighbor
	if(x+1<=dim-1 and maze[x+1][y].value!=1 and not maze[x+1][y].visited): #(x+1,y) not in closed_set
			maze[x+1][y].visited = True
			maze[x+1][y].parent = (x,y)
			if heuristic == "manhattan":
				priority_value = (source_distance + 1) + manhattan_heuristic(x+1, y, dim)
			elif heuristic == "euclidian":
				priority_value = (source_distance + 1) + euclidian_heuristic(x+1, y, dim)
			fringe.put((priority_value, (x+1, y)))
	
	# left neighbor
	if(y-1>=0 and maze[x][y-1].value!=1 and not maze[x][y-1].visited): #(x,y-1) not in closed_set
			maze[x][y-1].visited = True
			maze[x][y-1].parent = (x,y)
			if heuristic == "manhattan":
				priority_value = (source_distance + 1) + manhattan_heuristic(x, y-1, dim)
			elif heuristic == "euclidian":
				priority_value = (source_distance + 1) + euclidian_heuristic(x, y-1, dim)
			fringe.put((priority_value, (x, y-1)))
	
	# right neighbor
	if(y+1<=dim-1 and maze[x][y+1].value!=1 and not maze[x][y+1].visited): #(x,y+1) not in closed_set)
			maze[x][y+1].visited = True
			maze[x][y+1].parent = (x,y)
			if heuristic == "manhattan":
				priority_value = (source_distance + 1) + manhattan_heuristic(x, y+1, dim)
			elif heuristic == "euclidian":
				priority_value = (source_distance + 1) + euclidian_heuristic(x, y+1, dim)
			fringe.put((priority_value, (x, y+1)))
	
	return fringe

# traverses the graph using A* algorithm given a heuristic
"""
parameters: maze, heuristic
return values: boolean representing solvability of maze, 
			   max fringe size, average fringe size,
			   closed set
"""
def a_star_traversal(maze, heuristic):
	closed_set = set()
	fringe = PriorityQueue()
	fringe.put((0, (0, 0)))
	dim = len(maze)

	exploration_steps = 0	
	max_fringe_length = 0
	avg_fringe_length = 0

	while(not(fringe.empty())):
		(priority, (x, y)) = fringe.get()
		exploration_steps+=1
	
		if((x,y)==(dim-1, dim-1)):
			# print "Solution found"
			closed_set.add((dim-1, dim-1))
			result_dict = {
				"is_solvable": True, 
				"total_steps": exploration_steps, 
				"max_fringe_length": max_fringe_length, 
				"avg_fringe_length": avg_fringe_length, 
				"closed_set": closed_set}
			return result_dict

		fringe = get_neighbors(maze, x, y, dim, heuristic, fringe)
		fringe_len = fringe.qsize()
		if fringe_len>max_fringe_length:
			max_fringe_length = fringe_len
		avg_fringe_length = avg_fringe_length + (fringe_len - avg_fringe_length)/exploration_steps
		closed_set.add((x,y))

	# print "No Solution"
	result_dict = {
		"is_solvable": False, 
		"total_steps": exploration_steps, 
		"max_fringe_length": max_fringe_length, 
		"avg_fringe_length": avg_fringe_length, 
		"closed_set": closed_set}
	return result_dict

def test_a_star(dim = 20, p = 0.2):

	test_maze = maze_runner.get_maze(dim, p)

	# a-star with manhattan heuristic
	maze = copy.deepcopy(test_maze)
	manhattan_result_dict = a_star_traversal(maze, "manhattan")
	
	if manhattan_result_dict["is_solvable"]:
		path = maze_runner.get_path(dim-1, dim-1, maze)
		print "Path", path
		print "Length of path: ", len(path)
		maze_runner.trace_path(maze, path)
	else:
		maze_runner.visualize_maze(maze)

	# a-star with euclidian heuristic
	maze = copy.deepcopy(test_maze)
	euclidian_result_dict = a_star_traversal(maze, "euclidian")
	
	if euclidian_result_dict["is_solvable"]:
		path = maze_runner.get_path(dim-1, dim-1, maze)
		print "Path", path
		print "Length of path: ", len(path)
		maze_runner.trace_path(maze, path)
	else:
		maze_runner.visualize_maze(maze)
