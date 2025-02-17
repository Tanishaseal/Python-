# Program:19
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Consider the list like: Details = [[19, 'Itika', 'Jaipur'], [16, 'Aman', 'Patna'], 
# [20, ‘Jaya’, ‘Kolkata’],[16,’Heba’, ‘Chandigarh’]]. Print those names who are eligible to give their vote.
# Date: 26.10.2024


Details=[
    [19, 'Itika', 'Jaipur'], 
    [16, 'Aman', 'Patna'], 
    [20, 'Jaya', 'Kolkata'],
    [16,'Heba', 'Chandigarh'] ]
voters = []
for person in Details:
    if person[0]>=18:
        voters.append(person[1])
print(voters)