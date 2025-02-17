# Python program to check whether the string is Symmetrical or Palindrome

def symmetry(s):
    l=len(s)
    mid=l/2
    if l%2==0:
        return s[:mid]==s[mid:]
    else:
        return s[:mid]==s[mid+1:]   

def palindrome(s):
    return s==s[::-1]
    
string=input("enter the sentence: ")
if symmetry(string):
    print(" the string is symmetric")
else:
    print(" the string is not symmetric")

if palindrome(string):
    print(" the string is symmetric")
else:
    print(" the string is not symmetric")