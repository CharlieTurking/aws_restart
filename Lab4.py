# 1  - 45 mins
# [] = list = mutable (can be changed)
myFruitList = ["apple", "banana", "cherry"]  
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
#
myFruitList[2] = "orange"
print(myFruitList)
# 2
# () = touple = immutable (cannot be changed)
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
# 3
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
#
# print(str(myValue) + " is of the data type " + str(type(myValue)))
print("Akuas favorite fruit is " + myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])