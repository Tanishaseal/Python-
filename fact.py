def fact(num):
    fact=1
    while(num!=0):
        fact=fact*num
        num-=1
        num//10;
    return fact
sum=0
for i in range(1,4):
    sum=sum+(i/ (fact(i)))
print(sum)
 