import math
import maze_runner as mr
from Queue import PriorityQueue

def manhattan_heuristic(x, y, dim):
	return abs(x - dim)+abs(y - dim)

def euclidian_heuristic(x, y, dim):
	return math.sqrt((x - dim)**2+(y - dim)**2)

def source_dist(x, y, maze):
	path = mr.get_path(x, y, maze)
	return len(path)

def get_neighbors(maze, x, y, dim, heuristic, closed_set, fringe):
	source_distance = source_dist(x, y, maze) 

	if(x-1>=0 and maze[x-1][y].value!=1 and not maze[x-1][y].visited): #(x-1,y) not in closed_set
			maze[x-1][y].visited = True
			maze[x-1][y].parent = (x,y)
			if heuristic == "manhattan":
				priority_value = (source_distance + 1) + manhattan_heuristic(x-1, y, dim)
			elif heuristic == "euclidian":
				priority_value = (source_distance + 1) + euclidian_heuristic(x-1, y, dim)
			fringe.put((priority_value, (x-1, y)))
			
	if(x+1<=dim-1 and maze[x+1][y].value!=1 and not maze[x+1][y].visited): #(x+1,y) not in closed_set
			maze[x+1][y].visited = True
			maze[x+1][y].parent = (x,y)
			if heuristic == "manhattan":
				priority_value = (source_distance + 1) + manhattan_heuristic(x+1, y, dim)
			elif heuristic == "euclidian":
				priority_value = (source_distance + 1) + euclidian_heuristic(x+1, y, dim)
			fringe.put((priority_value, (x+1, y)))
	
	if(y-1>=0 and maze[x][y-1].value!=1 and not maze[x][y-1].visited): #(x,y-1) not in closed_set
			maze[x][y-1].visited = True
			maze[x][y-1].parent = (x,y)
			if heuristic == "manhattan":
				priority_value = (source_distance + 1) + manhattan_heuristic(x, y-1, dim)
			elif heuristic == "euclidian":
				priority_value = (source_distance + 1) + euclidian_heuristic(x, y-1, dim)
			fringe.put((priority_value, (x, y-1)))
	
	if(y+1<=dim-1 and maze[x][y+1].value!=1 and not maze[x][y+1].visited): #(x,y+1) not in closed_set)
			maze[x][y+1].visited = True
			maze[x][y+1].parent = (x,y)
			if heuristic == "manhattan":
				priority_value = (source_distance + 1) + manhattan_heuristic(x, y+1, dim)
			elif heuristic == "euclidian":
				priority_value = (source_distance + 1) + euclidian_heuristic(x, y+1, dim)
			fringe.put((priority_value, (x, y+1)))
	
	return fringe

def a_star_traversal(maze, heuristic):
	closed_set = set()
	fringe = PriorityQueue()
	fringe.put((0, (0, 0)))

	while(not(fringe.empty())):
		(priority, (x, y)) = fringe.get()
		# if((x,y) in closed_set):
		# 	continue
		print(priority, (x,y))
		if((x,y)==(dim-1, dim-1)):
			print "DONE"
			return True
		fringe = get_neighbors(maze, x, y, dim, heuristic, closed_set, fringe)
		closed_set.add((x,y))
		print("Fringe: "+str(not(fringe.empty())))
		# print(closed_set)
		# print(fringe.qsize())
		print(fringe.queue)

	print "No Solution"
	return False

# Main code
dim = 10
p = 0.2
maze = mr.get_maze(dim, p)
# mr.visualize_maze(maze)

result = a_star_traversal(maze, "manhattan")
if result:
	path = mr.get_path(dim-1, dim-1, maze)
	print(path)
	print(len(path))
	mr.trace_path(maze, path)
else:
	mr.visualize_maze(maze)