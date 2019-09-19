def checkneighbours_bbfs(maze, m, n, dim, current_cell, fringe, closed):

    intersect = None

    if m-1 >= 0 and maze[m-1][n].value != 1 and (m-1, n) not in closed and (m-1, n) not in fringe:
        if maze[m-1][n].parent is not None:
            intersect = (m-1, n)
        else:
            fringe.append((m-1, n))
            maze[m-1][n].parent = (m, n)
    if n+1 < dim and maze[m][n+1].value != 1 and (m, n+1) not in closed and (m, n+1) not in fringe:
        if maze[m][n+1].parent is not None:
            intersect = (m, n+1)
        else:
            fringe.append((m, n+1))
            maze[m][n+1].parent = (m, n)
    if m+1 < dim and maze[m+1][n].value != 1 and (m+1, n) not in closed and (m+1, n) not in fringe:
        if maze[m+1][n].parent is not None:
            intersect = (m+1, n)
        else:
            fringe.append((m+1, n))
            maze[m+1][n].parent = (m, n)
    if n-1 >= 0 and maze[m][n-1].value != 1 and (m, n-1) not in closed and (m, n-1) not in fringe:
        if maze[m][n-1].parent is not None:
            intersect = (m, n-1)
        else:
            fringe.append((m, n-1))
            maze[m][n-1].parent = (m, n)

    return intersect
