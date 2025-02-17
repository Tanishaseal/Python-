# write a Python program to swap the first and last element of the list

list=[]
n=int(input("enter the number of elements you want to add: "))

for i in range(0,n):
    element=int(input())
    list.append(element)
print(" original list is :", list)

list[0] , list[-1]= list[-1], list[0]
print (" list after swapping the first and last element is :", list)