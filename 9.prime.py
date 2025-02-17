# Program:7
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: WAP to check set of Prime numbers from the given range as input from the user.
# Date: 5.9.2024
a=int(input("enter the starting range "))
b=int(input("enter the ending number "))
print(" the prime numbers are: ")
for n in range(a,b+1):
    if(n>1):
        for i in range(2,n):
            if (n%2)==0:
                break
            else:
                print(n)
                break