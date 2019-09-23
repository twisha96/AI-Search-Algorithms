from maze_runner import get_maze
from bfs_2 import bfs_traversal
import time
import matplotlib.pyplot as plt
import pandas as pd
import scipy.interpolate
from a_star import a_star_traversal

''' 
Returns the average execution time for bfs traversals and
also the total number of tries to get 100 success cases
'''
def get_avg_times_and_total_tries(dim, p):
	total_time = 0
	avg_time = 0.0
	success_count = 0
	max_avg_time = 0
	totaltries = 0

	for i in xrange(0, 1):
		while(True):
			test_maze = get_maze(dim, p)
			totaltries = totaltries + 1
			startTime = time.time()
			# bfs_result = bfs_traversal(maze, dim)
			result, steps, max_fringe_length, avg_fringe_length, manhattan_closed_set = a_star_traversal(test_maze, "manhattan")
			end_time = time.time()
			if result:
				time_taken = end_time - startTime 
				avg_time = (avg_time*success_count+(time_taken))/(success_count + 1)
				total_time += time_taken
				success_count = success_count + 1
				print "Success count: " + str(success_count)
				break	
		
	return total_time, totaltries

# Plots the total time taken to complete 100 success cases versus P value for different dimensions 
def generate_comparison_plot(dim_list, p_list):
	runtime_df = pd.DataFrame(columns=p_list, index=dim_list)
	totaltries_df = pd.DataFrame(columns=p_list, index=dim_list)

	for ind, dim in enumerate(dim_list):
		run_time_list = []
		totaltries_list = []

		for p in p_list:
			run_time, totaltries = get_avg_times_and_total_tries(dim, p)
			run_time_list.append(run_time)
			totaltries_list.append(totaltries)

		runtime_df.iloc[ind] = pd.Series(run_time_list, index=runtime_df.columns)
		totaltries_df.iloc[ind] = pd.Series(totaltries_list, index=totaltries_df.columns)

	colors = ['blue', 'red', 'green', 'yellow', 'black']
	plt.ylabel("Execution time for discovering and solving 100 mazes")
	plt.xlabel("P")
	plt.title("Total execution time versus P")
	for i in range(runtime_df.shape[0]):
		plt.plot(runtime_df.iloc[i].index, runtime_df.iloc[i].values, label="dim=%d"%(dim_list[i]), marker='o', color=colors[i])
	plt.legend()
	plt.show()

	runtime_df_transpose = runtime_df.transpose()
	for i in range(runtime_df_transpose.shape[0]):
		plt.plot(runtime_df_transpose.iloc[i].index, runtime_df_transpose.iloc[i].values, 
			label="p=%f"%(p_list[i]), marker='o', color=colors[i])
	plt.legend()
	plt.show()

	return runtime_df, totaltries_df

# Gets the solvability in % for a particular dim and range of p values
def get_solvability(dim, p):
	total_time, totaltries = get_avg_times_and_total_tries(dim, prob)
	print "Solvability with p = " + str(prob) + " = " + str(100*100.0/totaltries)

# Main

# dim_list = [10, 50, 100, 150, 200, 250]
# p_list = [0.1, 0.125, 0.15, 0.175, 0.20, 0.225, 0.25, 0.275, 0.30, 0.325, 0.35, 0.375, 0.40]
dim_list = [10]
p_list = [0.1]
runtime_df, totaltries_df = generate_comparison_plot(dim_list, p_list)
runtime_df.to_csv("rutime_df.csv")
totaltries_df.to_csv("totaltries_df.csv")

totaltries_df = pd.read_csv("totaltries_df.csv") 
solvabilty_df = pd.DataFrame(columns=p_list, index=dim_list)
for dim in dim_list:
	tries_list = []
	for p in p_list:
		tries_list.append(totaltries_df.iloc[dim][p])
	solvability_df.loc[dim] = pd.Series(totaltries_list, index=totaltries_df.columns)

