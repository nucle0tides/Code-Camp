"""
	Control Flow
"""

"""
	If/Elif/Else
"""
test_str = "Code Camp"
if len(test_str) < 5: 
	print("I love Code Camp!")
elif len(test_str) < 6: 
	print("I!!! Love!!! Code Camp!!!")
else: 
	print("The length of our test string is {}".format(test_str))


final_percentage = 100
if x > 60 and x < 101: 
	print("hooray, I passed!")

if x < 50 or x > 105: 
	print("I did it!")

"""
	While Loops
"""
num = 10
while num > 0: 
	print(num)
	num = num - 1

"""
	For Loops
"""	

# print even numbers
for i in range(2, 101, 2): 
	print(i)

for i in range(5): 
	print("I'm having a great time at Code Camp!")

lst = [1, 2, 3, 4, 5]

# let's calculate the powers of 2 up to 100
powers = []
for i in range(100):
	powers.append(2 ** x)

# pythonic for loop, don't worry if you don't understand what's happening
# i just think they're 
powers_pythonic = [2 ** x for x in range(100)]