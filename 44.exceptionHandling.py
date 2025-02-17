
# Program:44
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: A list of number is given here like my_list = [22, 6, 7, 11, 24, 0, 6]. 
# Write a program to find out the probable exceptions and handle those exceptions properly. 
# Date: 30.10.2024

my_list = [22, 6, 7, 11, 24, 0, 6]

def process_list(lst):
    try:
        # Accessing an element at an index that may be out of range
        element = lst[10]
        print(f"Element at index 10: {element}")
    except IndexError:
        print("IndexError: Index 10 is out of range.")

    try:
        # Division by zero
        for num in lst:
            result = 100 / num
            print(f"100 divided by {num} is {result}")
    except ZeroDivisionError:
        print("ZeroDivisionError: Division by zero is not allowed.")

    try:
        # Trying to add a string to the list which may cause a TypeError
        result = lst[0] + "test"
        print(f"Result: {result}")
    except TypeError:
        print("TypeError: Cannot add a string to an integer.")

process_list(my_list)
