from maze_runner import get_maze
from fire import start_fire
from fire import spread_fire
from maze_runner import get_path
from maze_runner import trace_path

def get_neighbors(maze, x, y, dim, closed_set, fringe):
	if(x-1>=0):
		if(maze[x-1][y].value!=1 and (x-1,y) not in closed_set):
			maze[x-1][y].parent = (x,y)
			fringe.append((x-1, y))
	if(y-1>=0):
		if(maze[x][y-1].value!=1 and (x,y-1) not in closed_set):
			maze[x][y-1].parent = (x,y)
			fringe.append((x, y-1))
	if(x+1<=dim-1):
		if(maze[x+1][y].value!=1 and (x+1,y) not in closed_set):
			maze[x+1][y].parent = (x,y)
			fringe.append((x+1, y))		
	if(y+1<=dim-1):
		if(maze[x][y+1].value!=1 and (x,y+1) not in closed_set):
			maze[x][y+1].parent = (x,y)
			fringe.append((x, y+1))	
	return fringe

def bfs_traversal(maze, dim):
	closed_set = set()
	fringe = [(0,0)]
	while(len(fringe) > 0):
		((x,y)) = fringe.pop(0)
		if((x,y) in closed_set):
			continue
		if((x,y)==(dim-1, dim-1)):
			print "Solution found"
			return True
		fringe = get_neighbors(maze, x, y, dim, closed_set, fringe)
		closed_set.add((x,y))
	print "No Solution"
	return False

def bfs_traversal_with_fire(maze, dim, q):
	closed_set = set()
	fringe = [(0,0)]
	no_of_steps = 0
	while(len(fringe) > 0):
		((x,y)) = fringe.pop(0)
		if((x,y) in closed_set):
			continue
		no_of_steps = no_of_steps + 1
		if((x,y)==(dim-1, dim-1)):
			return no_of_steps
		fringe = get_neighbors(maze, x, y, dim, closed_set, fringe)
		closed_set.add((x,y))
	return -1


dim = 10
p = 0.1
q = 0.02
maze = get_maze(dim, p)
fire_maze = [row[:] for row in maze]
total_steps =  bfs_traversal_with_fire(maze, dim, q)
print "Number of steps: " + str(total_steps)
if total_steps > 0:
	path = get_path(dim-1, dim-1, maze)
	trace_path(maze, path)
	current_step = 0
	fire_maze = start_fire(fire_maze, dim)
	while (current_step < total_steps):
		fire_maze = spread_fire(fire_maze, dim, q)
		current_step = current_step + 1
	final_maze = [row[:] for row in fire_maze]
	trace_path(final_maze, path)
	for i in range(dim):
		for j in range(dim):
			if (fire_maze[i][j].value == 2 and (i, j) in path):
				print "Fail"
				exit()
	print "Success"