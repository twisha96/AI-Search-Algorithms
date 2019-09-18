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

def dfs_traversal(maze, dim):
	closed_set = set()
	fringe = [(0,0)]
	while(len(fringe) > 0):
		((x,y)) = fringe.pop()
		if((x,y) in closed_set):
			continue
		if((x,y)==(dim-1, dim-1)):
			print "Solution found"
			return True
		fringe = get_neighbors(maze, x, y, dim, closed_set, fringe)
		closed_set.add((x,y))
	print "No Solution"
	return False