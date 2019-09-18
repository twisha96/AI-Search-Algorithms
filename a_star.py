from Queue import PriorityQueue

def manhattan_heuristic(x, y, dim):
	return abs(x - dim)+abs(y - dim)

def source_dist(x, y):
	return x+y

def get_path():
	path = []
	(x,y)=(dim-1,dim-1)
	while((x,y)!=(0,0)):
    	print((x,y))
    	path.insert(0,(x,y))
    	(x, y) = maze[x][y].parent
    path.insert(0,(0,0))
    return path

def get_neighbors(x, y, closed_set, maze, fringe):
	print(str(x)+" "+str(y))
	print("In neighbor function: "+str(fringe.qsize()))
	source_distance = source_dist(x,y) 

	if(x-1>=0):
		if(maze[x-1][y].value!=1 and (x-1,y) not in closed_set):
			# neighbors.add[(x-1, y)]
			maze[x-1][y].parent = (x,y)
			priority_value = (source_distance + 1) + manhattan_heuristic(x-1, y, dim)
			fringe.put((priority_value, (x-1, y)))
			print("Left: "+str(fringe.qsize()))
			
	if(x+1<=dim-1):
		# print(maze[x+1][y].value==0 and (x+1,y) not in closed_set)
		if(maze[x+1][y].value!=1 and (x+1,y) not in closed_set):
			# neighbors.add[(x+1, y)]
			maze[x+1][y].parent = (x,y)
			priority_value = (source_distance + 1) + manhattan_heuristic(x+1, y, dim)
			fringe.put((priority_value, (x+1, y)))
			print("Right: "+str(fringe.qsize()))
	
	if(y-1>=0):
		if(maze[x][y-1].value!=1 and (x,y-1) not in closed_set):
			# neighbors.add[(x, y-1)]
			maze[x][y-1].parent = (x,y)
			priority_value = (source_distance + 1) + manhattan_heuristic(x, y-1, dim)
			fringe.put((priority_value, (x, y-1)))
			print("Bottom: "+str(fringe.qsize()))
	
	if(y+1<=dim-1):
		# print(maze[x][y+1].value==0 and (x,y+1) not in closed_set)
		if(maze[x][y+1].value!=1 and (x,y+1) not in closed_set):
			# neighbors.add[(x, y+1)]
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
		fringe = get_neighbors(x, y, closed_set, maze, fringe)
		closed_set.add((x,y))
		print("Fringe: "+str(not(fringe.empty())))
		# print(closed_set)
		# print(fringe.qsize())
		print(fringe.queue)

	print "No Solution"
	return False

result = a_star_traversal(maze)
if result:
	path = get_path()
	print(path)
	print(len(path))
