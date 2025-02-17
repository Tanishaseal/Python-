# Program:31
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Row-wise element Addition in Tuple Matrix


# Date: 30.10.2024

rows=int(input("enter the number of rows in matrix :"))
cols=int(input("enter the number of columns in matrix :"))

matrix=[]

for i in range(rows):
    row = []
    print(f"Enter the elements for row {i + 1}:")
    for j in range(cols):
        element = int(input(f"Element {j + 1}: "))
        row.append(element)
    matrix.append(tuple(row))

row_sum = [sum(row) for row in matrix]

print("Matrix: ", matrix)
print("Row-wise sums:", row_sum)
