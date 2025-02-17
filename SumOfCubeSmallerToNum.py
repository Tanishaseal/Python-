# Write a Python function that takes a positive integer and returns
# the sum of the cube of all positive integers smaller than the specified number.

n=int(input("enter a number: "))
sum=0
n-=1
while n>0:
    sum+=n*n*n
    n-=1
print(sum)