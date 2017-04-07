def exception_test():
	lst = [1, 2, 3, 4, 5, 6, 7]
	try:
		for i in range(len(lst) + 1): 
			print lst[i]
	except Exception as e:
		print("The exception that occurred was: {}".format(e))
	
if __name__ == '__main__':
	exception_test()