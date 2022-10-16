# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ryan Kethley
# Section:      565
# Assignment:   7.26 LAB: Pig Latin
# Date:         6 October 2022

    
# input from user a string containing multiple words seperated by a single space
UserSentence = input("Enter word(s) to convert to Pig Latin: \n")
UserList = UserSentence.split()

#convert words to pig latin
vowels = ["a", "e", "i", "o", "u", "y"]
def PigLatinize(MyWord):
    if MyWord[0] in vowels:
        return MyWord + "yay"
    elif MyWord[0] not in vowels and MyWord[1] in vowels:
        return MyWord[1:] + MyWord[0] + "ay"
    else:
        return MyWord[2:] + MyWord[0:2] + "ay"

#print both orginal word 
print(f'In Pig Latin,"{UserSentence}" is: ', end="")

#for loop for pig latined word
for x in range(len(UserList)):
    UserList[x] = PigLatinize(UserList[x])
    print(UserList[x], end=" ")