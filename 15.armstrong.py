# Program:15
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: WAP to check if a number is Armstrong or not for a single, double, triple, and quadruple digits from the user choice
# Date: 6.9.2024
number = int(input("enter the number: "))
copy=number
sum=0
size=len(str(number))
while(copy!=0):
    d=copy%10
    sum = sum+ pow(d,size)
    copy //=10
    
if(sum==number):
    print("number is armstrong ")
else:
    print("number is not armstrong ")