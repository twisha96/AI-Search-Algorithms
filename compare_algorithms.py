import pandas as pd
import copy 
import maze_runner as mr
from a_star import a_star_traversal

# Main code
dim = 20
p = 0.2
test_maze = mr.get_maze(dim, p)

'''
Given a maze, this function compares the different search algorithms based on:
1. Length of path from source to destination
2. Number of steps or the number of cells explored while finding the path
3. Maximum fringe size before reaching destination
4. Average fringe size while finding the path
'''
def compare_algorithms(test_maze):
	column_name_list = ['path_length', 'exploration_steps', 'max_fringe_size', 'avg_fringe_size']
	algo_comparison_df = pd.DataFrame(columns=column_name_list)
	
	# a-star with manhattan heuristic
	maze = copy.deepcopy(test_maze)
	result, exploration_steps, max_fringe_length, avg_fringe_length, closed_set = \
		a_star_traversal(maze, "manhattan")
	df_entry = pd.DataFrame([(exploration_steps, max_fringe_length, avg_fringe_length)], columns = column_name_list, index=['astar_manhattan']) 
	algo_comparison_df = algo_comparison_df.append(df_entry)

	# a-star with euclidian heuristic
	maze = copy.deepcopy(test_maze)
	result, exploration_steps, max_fringe_length, avg_fringe_length, closed_set = \
		a_star_traversal(maze, "euclidian")
	df_entry = pd.DataFrame([(exploration_steps, max_fringe_length, avg_fringe_length)], columns = column_name_list, index=['astar_euclidian']) 
	algo_comparison_df.append(df_entry)

	algo_comparison_df.to_csv("algo_comparison_df.csv")
	return algo_comparison_df

