class Cell:

	def __init__(cell, value):
		"""
		value = 0 => empty cell
		value = 1 => occupied cell
		value = 2 => start cell
		value = 3 => goal cell
		value = 4 => burning cell
		"""
		cell.value = value
		cell.parent = None
		cell.visited = False