
# Program:42
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Write a Python program that executes an operation on a list and handles an 
# IndexError exception if the index is out of range.

# Date: 30.10.2024

def access_element(lst, index):
    try:
        element = lst[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print(f"IndexError: Index {index} is out of range for the list.")

# Example list
n=int(input("enter the number of elements : "))
my_list=[]
for i in range(0,n):
    ele=int(input(f"enter element number {i}: "))
    my_list.append(ele)
# my_list = [10, 20, 30, 40, 50]
ind=int(input("enter the index: "))
# Test the function with a valid index and an invalid index
access_element(my_list, ind)  # Valid index
# access_element(my_list, 10)  Invalid index
