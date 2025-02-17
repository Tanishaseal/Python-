# Program:34
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Remove duplicates from Dictionary.


# Date: 30.10.2024

d1 = {1: 50, 2: 20, 3: 30, 4: 40, 5: 50, 6: 30}
d2={}

for key, value in d1.items():
    if value not in d2.values():
        d2[key]=value
print(d2)
