# Program:35
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# Date: 30.10.2024

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

combine_d=d1.copy()

for key, value in d2.items():
    if key in combine_d:
        combine_d[key]+=value
        
    else:
        combine_d[key]=value
        
print(combine_d)