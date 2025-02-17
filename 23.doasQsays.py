# Program:23
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: txt="welcome to python lab". Write a program in python to print the 
# number of vowels in txt, change into uppercase, lowercase, camelCase and snake case.
# Date: 26.10.2024


txt= "welcome to python lab"

upper_txt=txt.upper()
lower_txt=txt.lower()
words = txt.split()
camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
snake_case= txt.replace(' ','_')

print("Upper Case: ",upper_txt)
print("Lower Case: ",lower_txt)
print("CamelCase: ",camel_case)
print("SnakeCase: ",snake_case)
