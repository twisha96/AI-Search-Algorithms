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
			maze = get_maze(dim, p)
			totaltries = totaltries + 1
			startTime = time.time()
			# bfs_result = bfs_traversal(maze, dim)
			result, max_fringe_length, avg_fringe_length, manhattan_closed_set = a_star_traversal(maze, "manhattan")
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
def generate_comparison_plot():
	# dim_list = [10, 50, 100, 150, 200, 250]
	# p_list = [0.1, 0.125, 0.15, 0.175, 0.20, 0.225, 0.25, 0.275, 0.30, 0.325, 0.35, 0.375, 0.40]
	dim_list = [10,15,20]
	p_list = [0.1, 0.2]
	df = pd.DataFrame(columns=p_list, index=dim_list)
	
	for ind, dim in enumerate(dim_list):
		run_time_list = []
		for p in p_list:
			run_time, tries = get_avg_times_and_total_tries(dim, p)
			run_time_list.append(run_time)
		df.iloc[ind] = pd.Series(run_time_list, index=df.columns)

	colors = ['blue', 'red', 'green', 'yellow', 'black']
	plt.ylabel("Execution time for discovering and solving 100 mazes")
	plt.xlabel("P")
	plt.title("Total execution time versus P")
	for i in range(df.shape[0]):
		plt.plot(df.iloc[i].index, df.iloc[i].values, label="dim=%d"%(dim_list[i]), marker='o', color=colors[i])
	plt.legend()
	plt.show()

	df_transpose = df.transpose()
	for i in range(df_transpose.shape[0]):
		plt.plot(df_transpose.iloc[i].index, df_transpose.iloc[i].values, 
			label="p=%f"%(p_list[i]), marker='o', color=colors[i])
	plt.legend()
	plt.show()

# Gets the solvability in % for a particular dim and range of p values
def get_solvability(dim, p_array):
	for prob in p_array:
		totaltries = get_avg_times_and_total_tries(dim, prob, mainstart_time)
		print "Solvability with p = " + str(prob) + " = " + str(100*100.0/totaltries)

# Plots Success rate versus P value graph to obtain the P0 value
def get_po_value():
	p_values = [0.1, 0.125, 0.15, 0.175, 0.20, 0.225, 0.25, 0.275, 0.30, 0.325, 0.35, 0.375, 0.40]
	solvabilities = [97.09, 94.34, 92.59, 91.74, 81.97, 74.07, 64.52, 60.61, 54.64, 36.50, 26.39, 11.53, 1.73]
	p_value_interp = scipy.interpolate.interp1d(solvabilities, p_values)
	p0 = p_value_interp(50)
	plt.plot(p_values, solvabilities)
	plt.annotate("P0 = " + str(round(p0, 3)) + " (success rate = 50%)",
	     xy=(p0, 50), xytext=(p0 - 0.1, p0 - 0.04),
	     arrowprops=dict(facecolor='black', shrink=0.005),)
	plt.ylabel("Success rate in %")
	plt.xlabel("P value")
	plt.title("Success rate versus probability")
	plt.show()

mainstart_time = time.time()
'''
Values of p tried: [0.25, 0.3, 0.35, 0.4]
Values of dim tried: [60, 80, 120, 170, 240]
get_avg_times_and_total_tries(dim, p, mainstart_time)
generate_comparison_plot - for comparison between each of the dims
chosen dim: 120
'''
dim = 120
'''
p_array = [0.1, 0.125, 0.15, 0.175, 0.20, 0.225, 0.25, 0.275, 0.30, 0.325, 0.35, 0.375, 0.40]
get_solvability(dim, p_array)
get_po_value()
'''