import maze_runner
import CheckNeighbours_BBFS
from collections import deque
import  static_maze

dim = 10
probability = 0.3
maze = maze_runner.get_maze(dim, probability)
#maze = static_maze.get_static_maze()
result = 0
fringe1 = deque()
fringe2 = deque()
closed1 = []
closed2 = []
fringe1.append((0, 0))
fringe2.append((dim-1, dim-1))
maze[0][0].parent = None
maze[dim-1][dim-1].parent = None

while len(fringe1) != 0 and len(fringe2) != 0:
    current1 = fringe1.popleft()
    m1 = current1[0]
    n1 = current1[1]
    current_cell1 = maze[m1][n1]
    if current1 not in closed1:
        if current_cell1.value != 1:
            intersect1 = CheckNeighbours_BBFS.checkneighbours_bbfs(maze, m1, n1, dim, fringe1, closed1)
            if intersect1 is not None:
                result = 1
                print "Intersecting node:", intersect1
                break
            closed1.append((m1, n1))

    current2 = fringe2.popleft()
    m2 = current2[0]
    n2 = current2[1]
    current_cell2 = maze[m2][n2]
    if current2 not in closed2:
        if current_cell2.value != 1:
            intersect2 = CheckNeighbours_BBFS.checkneighbours_bbfs(maze, m2, n2, dim, fringe2, closed2)
            if intersect2 is not None:
                result = 1
                print "Intersecting node:", intersect2
                break
            closed2.append((m2, n2))
path = []
if result == 0:
    print "No Path Found"
    maze_runner.visualize_maze(maze)
else:
    if intersect1 is not None:
        path = maze_runner.get_path(current1[0], current1[1], maze)
        while intersect1[0] <= dim-1 and intersect1[1] <= dim-1:
            path.append(intersect1)
            if intersect1 == (dim-1, dim-1):
                break
            intersect1 = maze[intersect1[0]][intersect1[1]].parent
    else:
        path = maze_runner.get_path(intersect2[0], intersect2[1], maze)
        while current2[0] <= dim-1 and current2[1] <= dim-1:
            path.append(current2)
            if current2 == (dim-1, dim-1):
                break
            current2 = maze[current2[0]][current2[1]].parent
    print path
    print len(path)
    maze_runner.trace_path(maze, path)
