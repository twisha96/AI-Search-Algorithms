import maze_runner as mr
import copy
import random
from Queue import PriorityQueue
import numpy as np
from dfs import dfs_traversal

# dim = Dimension of maze, p = probability of the cells being occupied
dim = 20
p = 0.4

# priority queue with fitness (i.e. harndness) associated with each maze
maze_population = PriorityQueue()
population_size = 10  # total population size including parents and children
total_crossovers = 10  # signifies the number of children generated
mutation_rate = 0.01  # signifies the number of cells which are mutated (0, 1 values swapped)
generations = 10

for i in range(population_size):
    while True:  # discard unsolvable mazes
        maze = mr.get_maze(dim, p)

        # use dfs algorithm to generate fringe
        dfs_result, exploration_steps, max_fringe_length, closed_set = dfs_traversal(copy.deepcopy(maze), dim)
        # calculate fitness using the max fringe size
        maze_fitness = -max_fringe_length
        if dfs_result:
            break

    # mr.visualize_maze(maze)
    maze_population.put((maze_fitness, copy.deepcopy(maze)))  # populate population with parents

print "initial population generated"

for generation_count in range(generations):
    for crossover_count in range(total_crossovers):
        while True:  # discard unsolvable mazes
            # choose two parent mazes at random
            parents = random.sample(range(0, population_size), 2)

            # combine the parents in a random way to get the child maze
            parent1_index = parents[0]
            parent2_index = parents[1]
            crossover_point = random.random()
            crossover_column = int(crossover_point * dim)

            parent1 = np.array(copy.deepcopy(maze_population.queue[parent1_index][1]), dtype=object)
            parent1 = parent1[:, :crossover_column]
            parent2 = np.array(copy.deepcopy(maze_population.queue[parent2_index][1]), dtype=object)
            parent2 = parent2[:, crossover_column:]

            child_maze = np.concatenate((parent1, parent2), axis=1)
            child_maze = child_maze.tolist()

            # mutate the child maze using the mutation rate
            mutations = int(mutation_rate * dim * dim)
            for i in range(mutations):
                while True:
                    x = random.randint(0, dim - 1)
                    y = random.randint(0, dim - 1)
                    if not (x == 0 and y == 0) and not (x == dim - 1 and y == dim - 1):
                        break

                child_maze[x][y].value = int(not (child_maze[x][y].value))

            # compute the fitness of each child
            dfs_result, exploration_steps, max_fringe_length, closed_set = dfs_traversal(copy.deepcopy(child_maze), dim)

            # calculate fitness using the max fringe length
            maze_fitness = -max_fringe_length
            # print dfs_result
            if dfs_result:
                break

        # print dfs_result, "checking child before adding it to population"
        # mr.visualize_maze(child_maze)
        maze_population.put((maze_fitness, copy.deepcopy(child_maze)))  # populate maze_population with children

    # create new population using 90% best mazes and 10% worst mazes
    best_mazes_count = int(0.9 * population_size)
    worst_mazes_count = population_size - best_mazes_count
    fitness_average = 0

    new_maze_population = PriorityQueue()

    for count in range(best_mazes_count):
        (fitness, maze) = maze_population.get()
        if count == 0:
            fitness_fittest = fitness
        fitness_average = fitness_average + (fitness - fitness_average) / (count + 1)
        new_maze_population.put((fitness, copy.deepcopy(maze)))

    print "fitness of fittest: ", fitness_fittest
    print "average fitness of population: ", fitness_average
    while maze_population.qsize() > worst_mazes_count:
        maze_population.get()

    for count in range(worst_mazes_count):
        (fitness, maze) = maze_population.get()
        new_maze_population.put((fitness, copy.deepcopy(maze)))  # populate new_maze_population with the new population

    maze_population = new_maze_population

hardest_maze = maze_population.get()  # choose the hardest maze with highest hardness value
print "fitness of the hardest maze: ", hardest_maze[0]
mr.visualize_maze(hardest_maze[1])
