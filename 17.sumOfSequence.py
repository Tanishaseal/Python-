# Program:17
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Program to find sum of sequence (1/1!)+(2/2!)+(3/3!)+...+(n/n!).
# Date: 26.10.2024
number=int(input("enter the number: "))
print ("the sum of series is = ")
fact=1
sum=0
for i in range(1,number+1):
    fact*=i
    sum=sum+(i/fact)
print (sum)