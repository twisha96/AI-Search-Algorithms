from maze_runner import get_maze
from dfs import dfs_traversal
from maze_runner import get_path
from maze_runner import trace_path

dim = 10
p = 0.3
maze = get_maze(dim, p)



result = dfs_traversal(maze, dim)



if result:
	path = get_path(dim-1, dim-1, maze)
	print "Path length: " + str((len(path)))
	trace_path(maze, path)