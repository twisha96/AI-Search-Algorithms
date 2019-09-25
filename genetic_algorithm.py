import maze_runner
import copy
import random
from Queue import PriorityQueue
import numpy as np
from a_star import a_star_traversal
import pdb

def test_population(new_maze_population):
	print "--------------------"
	print "Population Solvability Check"
	for curr_maze_count in range(new_maze_population.qsize()):
		curr_maze = new_maze_population.queue[curr_maze_count]
		curr_maze_result_dict = \
			a_star_traversal(copy.deepcopy(curr_maze[1]), "manhattan")
		if not curr_maze_result_dict["is_solvable"]:
			print "ERROR!!!"
			maze_runner.visualize_maze(copy.deepcopy(curr_maze[1]))
		print curr_maze_result_dict["is_solvable"]
	print "--------------------"

# Main code
dim = 15
p = 0.3

# priority queue with fitness (i.e. hardness) associated with each maze
maze_population = PriorityQueue()
population_size = 50
total_crossovers = 50
mutation_rate = 0
generations = 10

for i in range(population_size):
	while True:
		maze = maze_runner.get_maze(dim, p)
		
		# find path using a_star
		result_dict = a_star_traversal(copy.deepcopy(maze), "manhattan")
		
		# calculate fitness using the max number of nodes explored
		maze_fitness = -result_dict["total_steps"]
		if result_dict["is_solvable"]:
			break

	maze_population.put((maze_fitness, copy.deepcopy(maze)))

print "initial population generated"

for generation_count in range(generations):
	for crossover_count in range(total_crossovers):

		# keep generating child mazes until we find a solvable one
		while True:
			# choose two parent mazes at random from the population
			parents = random.sample(range(0, population_size), 2)

			# combine the parents in some way to get the child maze
			parent1_index = parents[0]
			parent2_index = parents[1]

			# choose a cross over point randomly
			crossover_point = random.random()
			crossover_column = int(crossover_point*dim)

			# calculate contribution of both parents
			parent1 = np.array(copy.deepcopy(maze_population.queue[parent1_index][1]), dtype=object)
			parent1 = parent1[:, :crossover_column]
			parent2 = np.array(copy.deepcopy(maze_population.queue[parent2_index][1]), dtype=object)
			parent2 = parent2[:, crossover_column:]

			# create child maze by combining the parents
			child_maze = np.concatenate((parent1, parent2), axis=1)
			child_maze = child_maze.tolist()

			# mutate the child maze
			mutations = int(mutation_rate*dim*dim)
			for i in range(mutations):
				while True:
					x = random.randint(0, dim-1)
					y = random.randint(0, dim-1)
					if not (x==0 and y==0) and not (x==dim-1 and y==dim-1):
						break

				child_maze[x][y].value = int(not(child_maze[x][y].value))
			# print "Mutation Successful"

			# compute the fitness of each child
			child_result_dict = \
				a_star_traversal(copy.deepcopy(child_maze), "manhattan")
			
			# calculate fitness using the max number of nodes explored
			maze_fitness = -child_result_dict["total_steps"]
		
			if child_result_dict["is_solvable"]:
				break
		
		maze_population.put((maze_fitness, copy.deepcopy(child_maze)))

	# create new population using 90% best mazes and 10% worst mazes
	best_mazes_count = int(0.9*population_size)
	worst_mazes_count = population_size - best_mazes_count
	fitness_average = 0

	new_maze_population = PriorityQueue()

	for count in range(best_mazes_count):
		(fitness, maze) = maze_population.get()
		if count==0:
			fitness_fittest = fitness
		fitness_average = fitness_average + (fitness - fitness_average)/(count+1)
		new_maze_population.put((fitness, copy.deepcopy(maze)))

	print "fitness of fittest: ", fitness_fittest
	print "average fitness of population: ", fitness_average
	while maze_population.qsize()>worst_mazes_count:
		maze_population.get()

	for count in range(worst_mazes_count):
		(fitness, maze) = maze_population.get()
		new_maze_population.put((fitness, copy.deepcopy(maze)))
	
	maze_population = new_maze_population

			
hardest_maze = maze_population.get()
print "fitness of the hardest maze: ", hardest_maze[0]
pdb.set_trace()
maze_runner.visualize_maze(hardest_maze[1])
hardest_maze_result_dict = a_star_traversal(copy.deepcopy(hardest_maze[1]), "manhattan")
maze_runner.visualize_explored_cells(hardest_maze[1], hardest_maze_result_dict["closed_set"])
