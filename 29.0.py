# Program:29
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: my_list=[1,101,0101,1001,010101,111010100,0000,11111], Write a program in python 
# (i) Wherever '0' is present replace it with 'a'.
# (ii) Wherever '00' is present replace it with '2'.
# (iii) Wherever '000' is present replace it with '3'.
# (iv) Wherever '0000' is present replace it with '4'.


# Date: 28.10.2024


my_list = [1, 101, 101, 1001, 10101, 111010100, 0, 11111]

def replace_zeros(num):
    str_num = str(num)
    str_num = str_num.replace('0000', '4')
    str_num = str_num.replace('000', '3')
    str_num = str_num.replace('00', '2')
    str_num = str_num.replace('0', 'a')
    return str_num

new_list = [replace_zeros(num) for num in my_list]
print(new_list)
