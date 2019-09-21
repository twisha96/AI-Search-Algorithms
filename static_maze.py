from cell import Cell

def get_static_maze():
    maze = []

    for row in xrange(10):
        maze.append([])
        for col in xrange(10):
            maze[row].append(Cell(0))

    for row in xrange(0, 10, 4):
        maze[1][row].value = 1
    for row in xrange(0, 10, 3):
        maze[3][row].value = 1
    for row in xrange(3, 10, 2):
        maze[0][row].value = 1
    for row in xrange(0, 10, 5):
        maze[2][row].value = 1
    for row in xrange(2, 10, 2):
        maze[4][row].value = 1
    for row in xrange(1, 10, 7):
        maze[5][row].value = 1
    for row in xrange(2, 10, 2):
        maze[6][row].value = 1
    for row in xrange(3, 10, 2):
        maze[8][row].value = 1
    maze[1][4].value = 0
    maze[2][3].value = 1
    maze[1][3].value = 1
    maze[7][3].value = 1

    maze[0][0].value = 2
    maze[9][9].value = 3
    return maze