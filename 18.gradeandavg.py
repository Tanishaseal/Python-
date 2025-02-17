# Program:18
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: WAP to find the average and grade for the student and display the 
# appropriate message based on their average marks. Consider 5 subjects.
# Date: 26.10.2024

def avgandgrade(marks):
    total=sum(marks)
    average=total/len(marks)
    
    if average>=90:
        grade='A'
    elif average>=80 and average<90:
        grade='B'
    elif average>=70 and average<80:
        grade='C'
    elif average>=60 and average<70:
        grade='D'
    elif average>=50 and average<60:
        grade='E'
    else:
        grade='F'
        
    return average, grade

marks=[]

for i in range(1,6):
    mark=float(input(f" enter the marks for subject {i} : "))
    marks.append(mark)
    
average, grade= avgandgrade(marks)

print("\n--- Student Result ---")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
