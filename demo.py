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
def demo(x):
    y=x+3
    return(y)
print(demo(4))
#
z = int(input("Please enter a number: "))
def demo1(x):
    y=x+3
    return(y)
print(demo1(z))
#
a=1
b=2
c=3
def demo2():
    y=a+b+c
demo
# Modules and Libs Demo
import math
absolute = -5.999 
floor_test = 198.42
result1 = math.fabs(absolute) 
result2 = math.floor(floor_test)
print(result1, " is the absolute value of ", absolute) 
print(result2, " is the floor of ", floor_test)
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
def logUserAge(age):
    assert age >= 0, "Invalid Age given"
logUserAge(-1)
print("ok age given")
"""
 var = "Double Value"
    sumvalue = var + 4

def doSomeThing(valuetocheck):
if valuetocheck > 4: print("bad indent")
"""
