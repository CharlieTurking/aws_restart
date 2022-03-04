"""
Prime numbers
"""
startNumber = input("Please enter the start number: ")
endNumber = input("Please enter the stop number: ")

print("Prime numbers between", int(startNumber), "and", int(endNumber), "are:")

for num in range(int(startNumber), int(endNumber) + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
