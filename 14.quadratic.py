# Program:14
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: WAP to find the roots of a quadratic equation – (Roots for greater, equal and imaginary)
# Date: 6.9.2024
import cmath 

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b + cmath.sqrt(discriminant)) / (2*a)
    return root1, root2

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("The value of 'a' should not be 0 for a quadratic equation.")
else:
    root1, root2 = find_roots(a, b, c)
    print(f"The roots of the quadratic equation are: {root1} and {root2}")
