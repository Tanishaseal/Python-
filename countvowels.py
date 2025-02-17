
def countVowels(s):
    count=0
    for i in s:
        if i.lower() in 'aeiou':
            count=count+1    
    return count

def replaceVowels(s):
    newstr=''
    for i in s.split(' '):
        if countVowels(i)==1:
            temp=i
            temp=temp.replace('a','s')
            temp=temp.replace('e','s')
            temp=temp.replace('i','s')
            temp=temp.replace('o','s')
            temp=temp.replace('u','s')
            newstr+=temp
        else:
            newstr+=i
        newstr+=' '
        
    print("the new string is", newstr)

string=input("enter the sentence: ")
print(" the numbers of vowels are ",countVowels(string))
replaceVowels(string)