import math
import copy 
import maze_runner as mr
from Queue import PriorityQueue

# Given a co-ordinate (x,y), calculates the manhattan distance from the destination (dim-1, dim-1)
def manhattan_heuristic(x, y, dim):
	return abs(x - dim)+abs(y - dim)

# Given a co-ordinate (x,y), calculates the euclidian distance from the destination (dim-1, dim-1)
def euclidian_heuristic(x, y, dim):
	return math.sqrt((x - dim)**2+(y - dim)**2)

# Given a co-ordinate (x,y), calculates the length of path traversed to reach (x,y) from source (0, 0)
def source_dist(x, y, maze):
	path = mr.get_path(x, y, maze)
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
def get_neighbors(maze, x, y, dim, heuristic, closed_set, fringe):
	source_distance = source_dist(x, y, maze) 

	# left neighbor
	if(x-1>=0 and maze[x-1][y].value!=1 and not maze[x-1][y].visited): #(x-1,y) not in closed_set
			maze[x-1][y].visited = True
			maze[x-1][y].parent = (x,y)
			if heuristic == "manhattan":
				priority_value = (source_distance + 1) + manhattan_heuristic(x-1, y, dim)
			elif heuristic == "euclidian":
				priority_value = (source_distance + 1) + euclidian_heuristic(x-1, y, dim)
			fringe.put((priority_value, (x-1, y)))
			
	# right neighbor
	if(x+1<=dim-1 and maze[x+1][y].value!=1 and not maze[x+1][y].visited): #(x+1,y) not in closed_set
			maze[x+1][y].visited = True
			maze[x+1][y].parent = (x,y)
			if heuristic == "manhattan":
				priority_value = (source_distance + 1) + manhattan_heuristic(x+1, y, dim)
			elif heuristic == "euclidian":
				priority_value = (source_distance + 1) + euclidian_heuristic(x+1, y, dim)
			fringe.put((priority_value, (x+1, y)))
	
	# bottom neighbor
	if(y-1>=0 and maze[x][y-1].value!=1 and not maze[x][y-1].visited): #(x,y-1) not in closed_set
			maze[x][y-1].visited = True
			maze[x][y-1].parent = (x,y)
			if heuristic == "manhattan":
				priority_value = (source_distance + 1) + manhattan_heuristic(x, y-1, dim)
			elif heuristic == "euclidian":
				priority_value = (source_distance + 1) + euclidian_heuristic(x, y-1, dim)
			fringe.put((priority_value, (x, y-1)))
	
	# top neighbor
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
	
	exploration_steps = 0	
	max_fringe_length = 0
	avg_fringe_length = 0

	while(not(fringe.empty())):
		(priority, (x, y)) = fringe.get()
		exploration_steps+=1
		print(priority, (x,y))
		if((x,y)==(dim-1, dim-1)):
			# print "Solution found"
			closed_set.add((dim-1, dim-1))
			return True, exploration_steps, max_fringe_length, avg_fringe_length, closed_set
		fringe = get_neighbors(maze, x, y, dim, heuristic, closed_set, fringe)
		fringe_len = fringe.qsize()
		if fringe_len>max_fringe_length:
			max_fringe_length = fringe_len
		avg_fringe_length = avg_fringe_length + (fringe_len - avg_fringe_length)/exploration_steps
		closed_set.add((x,y))
		print("Fringe: "+str(not(fringe.empty())))
		print(fringe.queue)

	# print "No Solution"
	return False, exploration_steps, max_fringe_length, avg_fringe_length, closed_set

# Main code
dim = 20
p = 0.2
test_maze = mr.get_maze(dim, p)

maze = copy.deepcopy(test_maze)
manhattan_result, manhattan_steps, manhattan_max_fringe_length, manhattan_avg_fringe_length, manhattan_closed_set = a_star_traversal(maze, "manhattan")
if manhattan_result:
	path = mr.get_path(dim-1, dim-1, maze)
	print(path)
	print(len(path))
	mr.trace_path(maze, path)
else:
	mr.visualize_maze(maze)

maze = copy.deepcopy(test_maze)
euclidian_result, euclidian_steps, euclidian_max_fringe_length, euclidian_avg_fringe_length, euclidian_closed_set = a_star_traversal(maze, "euclidian")
if euclidian_result:
	path = mr.get_path(dim-1, dim-1, maze)
	print(path)
	print(len(path))
	mr.trace_path(maze, path)
else:
	mr.visualize_maze(maze)