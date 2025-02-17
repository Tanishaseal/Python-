n=int(input("enter the number of elements you want to add in the list "))
list=[]
for i in range(n):
    ele = input(f"Enter value {i+1}: ")
    list.append(ele)
print("the list is=", list)
copy=list.copy()
copy.reverse() 
print("the reversed list is=", copy)
if list == copy:
    print("list is palindrome")
else:
    print("list is not palindrome")