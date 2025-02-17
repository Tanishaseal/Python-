
# Program:46
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Make a list of four objects of Person type class and print the 
# status of their salary based on maximum salary drawn.

# Date: 30.10.2024

class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def check_salary_status(self, max_salary):
        if self.salary == max_salary:
            print(f"Mr. {self.name} is withdrawing the maximum salary.")
        elif self.salary > 60000:
            print(f"Mr. {self.name} is withdrawing a handsome salary.")
        else:
            print("Sorry! Try to improve yourself.")

# Create a list of Person objects
persons = [
    Person("John", 30, 70000),
    Person("Jane", 28, 60000),
    Person("Doe", 35, 45000),
    Person("Smith", 40, 80000)
]

# Find the maximum salary
max_salary = max(person.salary for person in persons)

# Check and print the salary status of each person
for person in persons:
    person.check_salary_status(max_salary)

