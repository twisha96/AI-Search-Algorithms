import pandas as pd
import copy 
import maze_runner
from a_star import a_star_traversal
from BFS import bfs
from dfs import dfs_traversal
from BiDirectionalBFS import bd_bfs

# Main code
dim = 125
p = 0.1
test_maze = maze_runner.get_maze(dim, p)

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
	
	# BFS
	maze = copy.deepcopy(test_maze)
	result_dict = bfs(maze, len(maze))
	path = maze_runner.get_path(dim-1, dim-1, maze)
	df_entry = pd.DataFrame([(len(path), result_dict["total_steps"], result_dict["max_fringe_length"], 
		result_dict["avg_fringe_length"])], columns = column_name_list, index=['BFS']) 
	algo_comparison_df = algo_comparison_df.append(df_entry)

	# DFS
	maze = copy.deepcopy(test_maze)
	result_dict = dfs_traversal(maze, len(maze))
	path = maze_runner.get_path(dim-1, dim-1, maze)
	df_entry = pd.DataFrame([(len(path), result_dict["total_steps"], result_dict["max_fringe_length"], 
		result_dict["avg_fringe_length"])], columns = column_name_list, index=['DFS']) 
	algo_comparison_df = algo_comparison_df.append(df_entry)

	# BD-BFS
	maze = copy.deepcopy(test_maze)
	result_dict = bd_bfs(maze, len(maze))
	path = maze_runner.get_path(dim-1, dim-1, maze)
	df_entry = pd.DataFrame([(result_dict["path_length"], result_dict["total_steps"], result_dict["max_fringe_length"], 
		result_dict["avg_fringe_length"])], columns = column_name_list, index=['BD-BFS']) 
	algo_comparison_df = algo_comparison_df.append(df_entry)

	# a-star with manhattan heuristic
	maze = copy.deepcopy(test_maze)
	result_dict = a_star_traversal(maze, "manhattan")
	path = maze_runner.get_path(dim-1, dim-1, maze)
	df_entry = pd.DataFrame([(len(path), result_dict["total_steps"], result_dict["max_fringe_length"], 
		result_dict["avg_fringe_length"])], columns = column_name_list, index=['astar_manhattan']) 
	algo_comparison_df = algo_comparison_df.append(df_entry)

	# a-star with euclidian heuristic
	maze = copy.deepcopy(test_maze)
	result_dict = a_star_traversal(maze, "euclidian")
	path = maze_runner.get_path(dim-1, dim-1, maze)
	df_entry = pd.DataFrame([(len(path), result_dict["total_steps"], result_dict["max_fringe_length"], 
		result_dict["avg_fringe_length"])], columns = column_name_list, index=['astar_euclidian']) 
	algo_comparison_df = algo_comparison_df.append(df_entry)

	algo_comparison_df.to_csv("algo_comparison_df.csv")
	return algo_comparison_df

algo_comparison_df = compare_algorithms(test_maze)