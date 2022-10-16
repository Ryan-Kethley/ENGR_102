# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ryan Kethley
# Section:      565
# Assignment:   Lab 6.14 Juggler Sequence
# Date:         4 October 2022

#inputting numbers
int1 = int(input("Enter a positive integer: "))
print("The Juggler sequence starting at", int1, "is: ")
i = 0



while int1 != 1:
    print(int1,',', end='',)
    intremain = int1 % 2
    if intremain == 0:
        newint=int(pow(int1,(1/2)))
    elif intremain != 0:
        newint=int(pow(int1,(3/2)))
    int1=newint
    i+=1
print('1')


print("It took", i,"iterations to reach 1")