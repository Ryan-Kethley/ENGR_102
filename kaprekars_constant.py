# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ryan Kethley
# Section:      565
# Assignment:   7.28 LAB: Kaprekar's Constant
# Date:         13 October 2022

#enter a number 
number = input("Enter a four-digit integer: ")
num = number
finallist = []
digits = ["1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "0000"]
count = 0
if number in digits:
    while number != '0':
        numberList1 = list(number)
        numberList2 = list(number)
        numberList1.sort()
        LtoG = numberList1
        numberList2.sort(reverse = True)
        GtoL = numberList2
        GtoLstring = ''.join(GtoL)
        LtoGstring = ''.join(LtoG)
        GtoLint = int(GtoLstring)
        LtoGint = int(LtoGstring)
        finallist.append(number + ' > ')
        number = GtoLint - LtoGint
        number = str(number)
        count += 1
else:
    while number != "6174":
        finallist.append(number + ' > ')
        if len(number) < 4:
            number = '0' * (4 -len(number))+number
        numberList1 = list(number)
        numberList2 = list(number)
        numberList1.sort()
        LtoG = numberList1
        numberList2.sort(reverse = True)
        GtoL = numberList2
        GtoLstring = ''.join(GtoL)
        LtoGstring = ''.join(LtoG)
        GtoLint = int(GtoLstring)
        LtoGint = int(LtoGstring)
        number = GtoLint - LtoGint
        number = str(number)
        count += 1
print(''.join(finallist) + number)
if number == '0':
    print(num, "reaches 0 via Kaprekar's routine in 1 iterations")
else:
    print(num, "reaches 6174 via Kaprekar's routine in", count, "iterations")

        
