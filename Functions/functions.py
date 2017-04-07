"""
	Functions
"""

def calculate_tip(meal_cost, tip_percentage): 
	return meal_cost * (float(tip_percentage) / 100)

def format_names(names): 
	"""
		Given a list of names, format each name to something silly
	"""
	for i in range(len(names)):
		names[i] = "{}{}{}".format(names[i][-1], names[i][0], "z")

	return names

if __name__ == '__main__':
	print(calculate_tip(46.50, 15))