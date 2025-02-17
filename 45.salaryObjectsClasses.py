
# Program:45
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Classes and objects, declaring a class Person with attributes name, age, salary 
# and creating an Object and checking the salary status. If the salary is greater than 
# 60000 then print the message “Mr. John is withdrawing handsome salary” else print “Sorry! Try to improve yourself”

# Date: 30.10.2024

class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def check_salary_status(self):
        if self.salary > 60000:
            print(f"Mr. {self.name} is withdrawing handsome salary.")
        else:
            print("Sorry! Try to improve yourself.")

# Creating an object of the Person class
person1 = Person("John", 30, 70000)

# Checking the salary status
person1.check_salary_status()
