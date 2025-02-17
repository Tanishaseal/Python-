# Program:24
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: txt=WAP to convert the string as Uppers, Lower, Camel case taking the input from the user.
# Date: 28.10.2024


txt= input("enter a sentence from the user= ")

upper_txt=txt.upper()
lower_txt=txt.lower()
words = txt.split()
camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
snake_case= txt.replace(' ','_')

print("Upper Case: ",upper_txt)
print("Lower Case: ",lower_txt)
print("CamelCase: ",camel_case)
print("SnakeCase: ",snake_case)
