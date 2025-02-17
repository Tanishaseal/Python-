# Program:15
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Write a program in python to convert binary to decimal.
# Date: 6.9.2024
binary = input("enter the binary number: ")
decimal=place=0
for i in reversed(binary):
    decimal = decimal + int(i)*pow(2,place)
    place+=1
print (decimal)