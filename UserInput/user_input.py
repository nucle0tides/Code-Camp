"""
	User Input
"""
name = input()
total_sale = float(input())
sales_tax = float(input())

plus_tax = total_sale + (total_sale * (sales_tax / 100))
print("{}, your total today, including tax, is {}".format(name, plus_tax))