# -*- coding: utf-8 -*-
from cell import Cell
import random
from sets import Set
import math

def get_number_of_neighbors_on_fire(maze, x, y, dim):
	count = 0
	if(x-1>=0 and maze[x-1][y].value == 2):
		count = count + 1
	if(y-1>=0 and maze[x][y-1].value == 2):
		count = count + 1
	if(x+1<=dim-1 and maze[x+1][y].value == 2):
		count = count + 1
	if(y+1<=dim-1 and maze[x][y+1].value == 2):
		count = count + 1
	return count

def get_fire_cells(maze, dim):
	fire_cells = []
	for i in range(dim):
		for j in range(dim):
			if maze[i][j].value == 2:
				fire_cells.append([i, j])
	return fire_cells

def get_candidate_neighbors(maze, x, y, dim, candidate_neighbors):
	if(x-1>=0 and maze[x-1][y].value != 1):
		candidate_neighbors.add((x-1, y))
	if(y-1>=0 and maze[x][y-1].value != 1):
		candidate_neighbors.add((x, y -1))
	if(x+1<=dim-1 and maze[x+1][y].value != 1):
		candidate_neighbors.add((x+1, y))
	if(y+1<=dim-1 and maze[x][y+1].value != 1):
		candidate_neighbors.add((x, y + 1))
	return candidate_neighbors

def spread_fire(maze, dim, q):
	fire_cells = get_fire_cells(maze, dim)
	candidate_neighbors = Set([])
	new_fire_cells = Set([])
	for [x, y] in fire_cells:
		candidate_neighbors = get_candidate_neighbors(maze, x, y, dim, candidate_neighbors)
	for [x, y] in candidate_neighbors:
		k = get_number_of_neighbors_on_fire(maze, x, y, dim)
		probability =  1.0 - math.pow(1 - q, k)
		if random.random() < probability:
			new_fire_cells.add((x, y))
	for [x, y] in new_fire_cells:
		maze[x][y].value = 2
	return maze

def start_fire(maze, dim):
	maze[0][dim - 1] = Cell(2)
	return maze