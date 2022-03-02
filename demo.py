import time
"""
a = 2
b = 2
c = a + b
print(a + b)
print(c)
c+=1
print(c)
print()   #prints a blank line
time.sleep(5)
# Variables and input strings
apples = input("How many apples are we using today? ")
oranges = 3
apples = oranges 
print("We have " + str(apples)+ " Apples here today")
print()   #prints a blank line
time.sleep(5)
# Lists
myAnimals = ["cat", "horse", "cat"]  
print(myAnimals)
print(type(myAnimals))
print()   #prints a blank line
time.sleep(5)
# For Loops
for item in myAnimals:
    print("{} is of the data type {}".format(item,type(item)))
myAnimals.append("unicorn")
print(myAnimals.count("cat"))
print()   #prints a blank line
time.sleep(5)
# While Loops
counter = 0
while counter <= 4:
    print("I love looping" + str(counter))
    counter+=1
print("done looping at counter = "+ str(counter))
print()   #prints a blank line
time.sleep(5)
# Dictionaries
myAnimalNames = {"cat1":"Alto", "horse":"Leo", "cat2":"Sopranino", "dog":"Otty"}
for key, value in myAnimalNames.items():
    print(key, value)
print()   #prints a blank line
time.sleep(5)
# If 
horses = 2
if horses <=1:
    print("You need MORE horses!")
elif horses <=2:
    print("You should consider having more horses")
else:
    print("Consider buying another horse")
"""

"""
# Functions Demo
# Function no args - no return
print("Function no args - no return")
a = 1
b = 2
def demo():
    a+b
demo

#
"""

"""
#
a=1
b=2
c=3
def demo2():
    y=a+b+c
demo2
"""
"""
# takes arguments and returns something
def demo4(x):
    y=x+3
    return(y)
print(demo4(4))
#
"""

"""
z = int(input("Please enter a number: "))
def demo5(x):
    y=x+3
    return(y)
print(demo5(z))
"""

"""
# Modules and Libs Demo
import math
absolute = -5.999 
floor_test = 198.42
sq_rt = 6
result1 = math.fabs(absolute) 
result2 = math.floor(floor_test)
result3 = math.sqrt(sq_rt)
print(result1, " is the absolute value of ", absolute) 
print(result2, " is the floor of ", floor_test)
print(result3, " is the SQ Root of ", sq_rt)
"""

"""
# Write to files Demo
print("Here is my life story: \n")
f1 = open("myLifeStory.txt", "w+")
for i in range(10):
     f1.write("This is line %d\r\n" % (i+1))
print(f1.read())
f1.close()
"""

"""
# Exceptions - import error
def div_by_zero(number):
    try:
        value = 5 / number
    except ZeroDivisionError:
        print('Div by Zero is not possible')
        value = None 
    return value
print(div_by_zero(2))
print(div_by_zero(0))
"""

"""
# importing os module
import os

# Get the list of all files and directories
# in the root directory
path = "/"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# print the list
print(dir_list)

# another os example
print("Current OS User: ")
os.system("whoami")
"""

"""
# Jason demo

import json
filename = 'userName.json'
name = ''
try:
    with open(filename, 'r') as r:
        name = json.load(r)
except IOError:
    print("First-time login")
if name != "": 
    print("Welcome back, " + name + "!")
else: 
    name = input("Hello! What's your name? ") 
    print("Welcome, " + name + "!")
""" 

"""
# Create user file 
# Save the user's name to the history file 
try:
    with open(filename, 'w') as f: 
        json.dump(name, f)
except IOError: 
    print("There was a problem writing to the history file.")
"""

"""
# Lists in Lists
# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

"""
