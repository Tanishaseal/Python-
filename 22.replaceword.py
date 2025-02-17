# Program:22
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Write a paragraph about India and use the word India repeatedly. Then, replace 
# the word India by the value “Bharat” and count the number of times appeared as Bharat
# Date: 26.10.2024


sentence=input("enter a paragraph about India: ")
sent=sentence.lower()
new_sent=sent.replace("india","Bharat")
count_Bharat=new_sent.count("Bharat")
print(new_sent)
print(count_Bharat)