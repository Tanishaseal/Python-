# Program:41
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Write a module defining with the functions of a factorial, Armstrong and perfect number 
# and then import that file into another file. Fine the factorial, Armstrong, and perfect number 
# using the menu driven program.

# Date: 30.10.2024


from module2 import factorial, armstrong, perfect

def menu():
    print("Choose an option:")
    print("1. Find Factorial")
    print("2. Check Armstrong Number")
    print("3. Check Perfect Number")
    print("4. Exit")

while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        print(f"Factorial of {num} is {factorial(num)}")
    elif choice == 2:
        num = int(input("Enter a number: "))
        if armstrong(num):
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
    elif choice == 3:
        num = int(input("Enter a number: "))
        if perfect(num):
            print(f"{num} is a Perfect number.")
        else:
            print(f"{num} is not a Perfect number.")
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
