# Program:33
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Check whether a given key already exists in a dictionary.
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# Date: 30.10.2024

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key=int(input("enter the key to be found in dictionary "))
if key in d:
    print("key is found")
else:
    print("key is not found")