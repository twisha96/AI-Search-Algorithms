from Queue import PriorityQueue

def manhattan_heuristic(x, y, dim):
	return abs(x - dim)+abs(y - dim)

def euclidian_heuristic(x, y, dim):
	return (x - dim)^2+abs(y - dim)^2

def source_dist(x, y):
	return x+y

def get_path(x, y, maze):
	path = []
	while((x,y)!=(0,0)):
		print((x,y))
		path.insert(0,(x,y))
		(x, y) = maze[x][y].parent
	path.insert(0,(0,0))
	return path

def get_neighbors(maze, x, y, dim, closed_set, fringe):
	print(str(x)+" "+str(y))
	print("In neighbor function: "+str(fringe.qsize()))
	source_distance = source_dist(x,y) 

	if(x-1>=0):
		if(maze[x-1][y].value!=1 and (x-1,y) not in closed_set):
			maze[x-1][y].parent = (x,y)
			priority_value = (source_distance + 1) + manhattan_heuristic(x-1, y, dim)
			fringe.put((priority_value, (x-1, y)))
			print("Left: "+str(fringe.qsize()))
			
	if(x+1<=dim-1):
		if(maze[x+1][y].value!=1 and (x+1,y) not in closed_set):
			maze[x+1][y].parent = (x,y)
			priority_value = (source_distance + 1) + manhattan_heuristic(x+1, y, dim)
			fringe.put((priority_value, (x+1, y)))
			print("Right: "+str(fringe.qsize()))
	
	if(y-1>=0):
		if(maze[x][y-1].value!=1 and (x,y-1) not in closed_set):
			maze[x][y-1].parent = (x,y)
			priority_value = (source_distance + 1) + manhattan_heuristic(x, y-1, dim)
			fringe.put((priority_value, (x, y-1)))
			print("Bottom: "+str(fringe.qsize()))
	
	if(y+1<=dim-1):
		if(maze[x][y+1].value!=1 and (x,y+1) not in closed_set):
			maze[x][y+1].parent = (x,y)
			priority_value = (source_distance + 1) + manhattan_heuristic(x, y+1, dim)
			fringe.put((priority_value, (x, y+1)))
			print("Top: "+str(fringe.qsize()))
	
	return fringe

def a_star_traversal(maze):
	closed_set = set()
	fringe = PriorityQueue()
	fringe.put((0, (0, 0)))

	while(not(fringe.empty())):
		(priority, (x, y)) = fringe.get()
		if((x,y) in closed_set):
			continue
		print(priority, (x,y))
		if((x,y)==(dim-1, dim-1)):
			print "DONE"
			return True
		fringe = get_neighbors(maze, x, y, dim, closed_set, fringe)
		closed_set.add((x,y))
		print("Fringe: "+str(not(fringe.empty())))
		# print(closed_set)
		# print(fringe.qsize())
		print(fringe.queue)

	print "No Solution"
	return False

result = a_star_traversal(maze)
if result:
	path = get_path(dim-1, dim-1, maze)
	print(path)
	print(len(path))


"""
Path for the intersting maze:
[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (6, 3), (6, 4), (5, 4), (5, 5), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (6, 8), (7, 8), (7, 9), (8, 9), (9, 9)]
23
"""