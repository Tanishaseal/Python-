# Program:11
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: WAP to check & print the inputted mobile number into words.
# Date: 6.9.2024
number=input("enter the phone number: ")
word=[]
w = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
if (len(number)==10):
    for i in range(len(number)):
        word.append(w[int(number[i])])
    print (word)
else:
    print ("Number is Invalid ")
    