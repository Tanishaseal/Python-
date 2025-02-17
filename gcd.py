def find_gcd(a,b):
    if b==0:
        return a
    else:
        return find_gcd(b, a % b)

num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
print(f"the gcd of two numbers is: {find_gcd(num1,num2)}")