# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    print("N is set to" + str(n))
    sum = sum + i
    print("Sum is now at " + str(sum))
    i = i+1    # update counter
    print("i is now at " + str(i))

# print the sum
print("The sum is", sum)