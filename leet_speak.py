# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ryan Kethley
# Section:      565
# Assignment:   7.26 LAB: Leet Speak
# Date:         13 October 2022

#Input senetence from user
sentence = input("Enter some text: \n")

#Assign variables for each letter using a dictionary
leet = {'a' : '4', 'e' :  '3', 'o' : '0', 's' : '5', 't' : '7'}

sentencelist = list(sentence)
for i in range(len(sentencelist)):
    if sentencelist[i] in leet:
        sentencelist[i] = leet[sentencelist[i]]

print(f'In leet speak, "{sentence}" is: ')
print(''.join(sentencelist))
        
    
    
    



    
