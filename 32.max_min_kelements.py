# Program:32
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Find the Maximum and Minimum K elements in Tuple

# Date: 30.10.2024

def max_min_k_elements(tup, K):
    
    sorted_elements = sorted(tup) #ascending
    max_elements = sorted_elements[-K:]
    min_elements = sorted_elements[:K]
    return max_elements, min_elements

my_list = []

K=int(input(" enter the number you want to slice the tuple with"))
for _ in range(K*2):
    element = int(input("Enter a number: "))
    my_list.append(element)
    tup=tuple(my_list)


max_elements, min_elements = max_min_k_elements(tup, K)
print(f"Maximum {K} elements:", max_elements)
print(f"Minimum {K} elements:", min_elements)
print(f"Sorted {K*2} elements:", sorted(tup))