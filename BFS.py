from collections import deque
import maze_runner
from CheckNeighbours import CheckNeighours

dim = 20
probability = 0.1

result = 0
closed = []
fringe = deque()
path = []
maze = maze_runner.get_maze(dim, probability)

fringe.append((0, 0))
while(len(fringe)!=0):
    current = fringe.popleft()
    m = current[0]
    n = current[1]
    current_cell = maze[m][n]
    if current not in closed:
        if current_cell.value == 3:
            result = 1
            break
        else:
            if current_cell.value != 1:
                checkneighbours = CheckNeighours()
                checkneighbours.check_neighbours(maze, dim, m, n, current_cell, fringe, closed)
            closed.append(current)

if result == 0:
    print "No Path Found"
    maze_runner.visualize_maze(maze)
else:
    path = maze_runner.get_path(m, n, maze)
    print path
    maze_runner.trace_path(maze, path)

