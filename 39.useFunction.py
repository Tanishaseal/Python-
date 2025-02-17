# Program:39
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic:my_list=[1222,22034,568101,82130,10101,1001,101010,27612], 
# Write a program in python creating separate functions for each.
# (i) If 2 is repeatedly then print those numbers from the given list.
# (ii) Print the sum of first digit and last digit of the given number.
# (iii) If the length of the number is odd, then multiply and sum of those numbers from the given numbers.
# (iv) print only those number where odd number is '0' found.
# (v) Print the binary number from the number list.

# Date: 30.10.2024

two_repeat=[]
even_list=[]
prime_list=[]
my_list=[1222,22034,568101,82130,10101,1001,101010,27612]

def repea_two(numbers):
    two_repeat = [num for num in my_list if(str(num)).count('2')>1]
    print(two_repeat)

def sumFirstLast(numbers):
    for num in my_list:
        str_num=str(num)
        sum_first_last= int(str_num[0])+int(str_num[-1])
        print(str_num ,":", sum_first_last)

def sumOddLength(numbers):
    sum_odd_length=0
    for num in my_list:
        str_num=str(num)
        if len(str_num)%2!=0:
            sum_odd_length+=num
    print(sum_odd_length)

def oddZeroPosition(numbers):
    for num in my_list:
        str_num=str(num)
        for i in range(len(str_num)):
            if str_num[i]=='0' and ((i+1)%2)!=0: #odd positions are def not divisible by 0, put i=0
                print (num)
   
def binary(numbers):         
    for num in my_list:
        print(num, ":", bin(num)[2:])


print(" numbers with repeated 2 are = ")
repea_two(my_list)

print(" Sum of first and last digits of = ")
sumFirstLast(my_list)

print(" Sum of odd length = ")
sumOddLength(my_list)

print(" Number where odd number is '0' found = ")
oddZeroPosition(my_list)

print(" Binary number = ")
binary(my_list)