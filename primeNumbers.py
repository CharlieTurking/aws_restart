"""
Prime numbers
"""
import subprocess

command="touch"
commandArgument="./mygit/primenumbers.txt"
subprocess.run([command,commandArgument])

with open('./mygit/primenumbers.txt', 'w') as fh:
    fh.write('These are the prime numbers \n')
startNumber = input("Please enter the start number: ")
endNumber = input("Please enter the stop number: ")

print("Prime numbers between", startNumber, "and", endNumber, "are:")
prime=[] 
for num in range(int(startNumber), int(endNumber) + 1):
#   print(num)
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           prime.append(num)
           print(num, "is a prime number")

with open('./mygit/primenumbers.txt', 'a') as fh:
    for items in prime:
        fh.write(str(items) + '\n')
print(prime)