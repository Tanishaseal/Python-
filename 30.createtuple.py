# Program:30
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Create a list of tuples from given list having number and its cube in each tuple.


# Date: 30.10.2024

my_list = []
num_elements = int(input("How many elements do you want to add to the list? "))

for _ in range(num_elements):
    element = int(input("Enter a number: "))
    my_list.append(element)

result = [(num, num**3) for num in my_list]
result=tuple(result)

print("List of tuples (number, cube):", result)
