
# Program:43
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Write a Python program that prompts the user to input two numbers and 
# raises a TypeError exception if the inputs are not numerical.

# Date: 30.10.2024

def get_number(prompt):
    value = input(prompt)
    if not value.replace('.', '', 1).isdigit():
        raise TypeError(f"Value '{value}' is not a valid number.")
    return float(value)

try:
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    print(f"The numbers you entered are {num1} and {num2}.")
except TypeError as e:
    print(e)

