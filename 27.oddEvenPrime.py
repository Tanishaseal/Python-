# Program:27
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Take a list of random numbers like my_list=[5,12,7,9,2,3,16,20,13,17]
#Then segregate even, odd and prime numbers from the list and store into the 
# separate list naming like odd_list appending the odd items into that.

# Date: 28.10.2024

odd_list=[]
even_list=[]
prime_list=[]
my_list=[5,12,7,9,2,3,16,20,13,17]

odd_list = [odd for odd in my_list if(odd%2!=0)]
even_list = [odd for odd in my_list if(odd%2==0)]

for num in my_list:

    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
    
print(" Odd Numbers :", odd_list)
print(" Even Numbers :", even_list)
print("Prime numbers :", prime_list)