# Program:41
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Write a module defining with the functions of a factorial, Armstrong and perfect number 
# and then import that file into another file. Fine the factorial, Armstrong, and perfect number 
# using the menu driven program.

# Date: 30.10.2024

def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num-1)

def armstrong(num):
    sum_digits= 0
    str_num=str(num)
    n = len(str_num)
    for digit in str_num:
        sum_digits+=pow(int(digit),n) 
    return num==sum_digits


def perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)