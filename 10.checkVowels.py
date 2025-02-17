# Program:10
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: WAP to find the vowels and consonants in a string.
# Date: 5.9.2024

text= input("enter the text: ")
vow=0
con=0
white=text.count(" ")
for ch in text:
    if ch in 'aeiouAEIOU':
        vow+=1
    else:
        con+=1
print(vow)
print(con-white)