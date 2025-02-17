# Program:13
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: WAP for password Checking – (Conditions are given: - minimum length 
# should be more than 8, at least one Upper, one Lower, and one digit) 
# Date: 6.9.2024
pw=input("enter the password: ")
alpha_ = False
numeric_ = False
upper_ = False
lower_ = False
if (len(pw)>8 ): 
    for ch in pw:
        if ch.islower():
            lower_ = True
        if ch.isupper():
            upper_ = True
        if ch.isnumeric():
            numeric_ = True
        if ch.isalpha():
            alpha_ = True
if lower_ and upper_ and alpha_ and numeric_ :
    print("valid")
else :
    print("invalid")