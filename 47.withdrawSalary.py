
# Program:47
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Allow the user to enter the name, age, and salary of the persons from the 
# keyboard and then print that person who is withdrawing maximum salary. Create the object at runtime.
# Date: 30.10.2024

class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

def get_person_details():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))
    return Person(name, age, salary)

# Create a list to hold Person objects
persons = []

# Get the number of persons to input
num_persons = int(input("How many persons do you want to enter? "))

# Collect details for each person
for _ in range(num_persons):
    person = get_person_details()
    persons.append(person)

# Find the person with the maximum salary
max_salary_person = max(persons, key=lambda p: p.salary)

# Print the details of the person with the maximum salary
print(f"\nPerson with the maximum salary:")
print(f"Name: {max_salary_person.name}")
print(f"Age: {max_salary_person.age}")
print(f"Salary: {max_salary_person.salary}")
