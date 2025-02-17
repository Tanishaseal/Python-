# Program:38
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Write a factorial of a number using recursion of a function.

# Date: 30.10.2024

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial is :", result)

