# Program:37
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Write a program to show the use of nested function.

# Date: 30.10.2024

def outer_function():
    outer_var = "I am outer"

    def inner_function():
        inner_var = "I am inner"
        print(inner_var)  # Accessing local variable of inner_function
        print(outer_var)  # Accessing local variable of outer_function

    # Call the nested function
    inner_function()

# Call the outer function
outer_function()

