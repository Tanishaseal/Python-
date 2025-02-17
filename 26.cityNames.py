# Program:26
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Txt= WAP to solve the following statements from the given list of cities: -
#City_list=[“Kolkata”, “Kasargod”, “Hyderabad”, “Chennai”, “Kalinga”, “Mumbai”, “Koembatore”]
#(i) City names starting with the letter ‘K’.
#(ii) City names containing 6 letters.
#(iii) City names containing more than or equal to 7 letters.
#(iv) City names that start with the letter ‘K’ and also contain 5 letters.
# Date: 28.10.2024


City_list = ["Kolkata", "Kasargod", "Hyderabad", "Chennai", "Kalinga", "Mumbai", "Koembatore"]

cities_starting_with_K = [city for city in City_list if city.startswith('K')]

cities_with_6_letters = [city for city in City_list if len(city) == 6]

cities_with_7_or_more_letters = [city for city in City_list if len(city) >= 7]

cities_starting_with_K_and_5_letters = [city for city in City_list if city.startswith('K') and len(city) == 5]

print("Cities starting with 'K':", cities_starting_with_K)
print("Cities with 6 letters:", cities_with_6_letters)
print("Cities with 7 or more letters:", cities_with_7_or_more_letters)
print("Cities starting with 'K' and containing 5 letters:", cities_starting_with_K_and_5_letters)
