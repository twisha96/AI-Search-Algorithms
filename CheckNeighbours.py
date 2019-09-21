class CheckNeighours():
    def check_neighbours(self, maze, dim, m, n, fringe, closed):
        if m - 1 >= 0 and maze[m-1][n].value != 1 and not maze[m-1][n].visited and (m - 1, n) not in closed:
            fringe.append((m - 1, n))
            maze[m-1][n].visited = True
            maze[m - 1][n].parent = (m, n)
        if n + 1 < dim and maze[m][n+1].value != 1 and not maze[m][n+1].visited and (m, n + 1) not in closed:
            fringe.append((m, n + 1))
            maze[m][n+1].visited = True
            maze[m][n + 1].parent = (m, n)
        if m + 1 < dim and maze[m+1][n].value != 1 and not maze[m+1][n].visited and (m + 1, n) not in closed:
            fringe.append((m + 1, n))
            maze[m+1][n].visited = True
            maze[m + 1][n].parent = (m, n)
        if n - 1 >= 0 and maze[m][n-1].value != 1 and not maze[m][n-1].visited and (m, n - 1) not in closed:
            fringe.append((m, n - 1))
            maze[m][n-1].visited = True
            maze[m][n - 1].parent = (m, n)
