# Program:36
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Write a program to show the use of local and global variable in function.

# Date: 30.10.2024

global_var = "I am global"

def my_function():
    # Local variable
    local_var = "I am local"
    
    print(local_var)  
    print(global_var) 

my_function()

print(global_var)
