# Program:25
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Txt= “I love my mother land India”
#Covert the text into list, then find the vowels for each word and display it.

# Date: 28.10.2024

vowels="aeiouAEIOU"
txt= "I love my mother land India"
list = txt.split()

for word in list:
    vowels_in_word= [char for char in word if char in vowels] # for char in list:
                                                        #  if char in vowels:
                                                        #   vowes_in_word=char

    print(f"{word}: {vowels_in_word}")