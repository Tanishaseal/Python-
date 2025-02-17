# Program:40
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Write a sample.py file containing add(), sub(), and mul() with two arguments. 
# Import that sample file into the other file called test.py, 
# and then call those functions from this test file.

# Date: 30.10.2024

from sample import add, sub, mul

num1=int(input(" enter the first number : "))
num2=int(input(" enter the second number : "))

print(f"Addition: {(num1,num2)} = {add(num1,num2)}")
print(f"Subtraction: {(num1,num2)} = {sub(num1,num2)}")
print(f"Multiplication: {(num1,num2)} = {mul(num1,num2)}")