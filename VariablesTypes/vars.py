"""
	Variables && Types && Useful Methods
"""

"""
	Numbers 
"""

# store the int 10 in a 
a = 10

# store the float 5.0 in b
b = 5.0 

# let's add two numbers together 
c = a + b # 15.0

"""
	Strings  
"""

# let's create a string 
first_name = "Gabby"
last_name = "Ortman"

# let's get my initials
initials = first_name[0] + '.' + last_name[0]

# get first four characters from my name
first_name[:4]

# get 'abb' out of 'Gabby'
first_name[1:4]

# format my name as last, first
full_name = "{}, {}".format(last_name, first_name)

# get length of strings 
len(full_name)

# make my name all upppercase 
full_name.upper()

# make my first name all lowercase 
first_name.lower()

"""
	Lists 
"""

#let's create some lists 
class_schedule = [101, 227, 212, 167, 110]
pets = ["Cosmo", "Allie", "Foley", "Smalls", "Pip"]

# let's add a new pet 
pets.append("Watson")

# first element in pets list
pets[0]

#last element in pets list 
pets[-1]

# pop last element in list 
pets.pop() 

# get the length of a list 
len(pets)

"""
	Dictionaries 
"""
gradebook = {
	"Gabby" : [100, 20, 25, 70, 90],
	"Betsy" : [100, 100, 100, 100, 100],
	"Ashley" : [100, 90, 95, 98, 100]
}

# get a key's values 
gabbys_grades = gradebook["Gabby"]

# add a new key, value pair 
gradebook["Cosmo"] = [100, 20, 30, 100, 67]
