# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ryan Kethley
# Section:      565
# Assignment:   Lab 6.15 Balancing Numbers
# Date:         4 October 2022

#input for n
n = int(input("Enter a value for n: "))

#variables
negn = n - 1
posn = n + 1
x = 0
y = 0
j = 0

#this code finds out the value of the summation of everything to the left of n
for i in range(0,negn):
    i += 1
    x += i

#this code adds the value of n + 1,2,3,4,5,....n+1 and then compares the value to x in order to find the answer
while y != x:
    j += 1
    y += n + j
    if y > x:
        print(n,'is not a balancing number')
        break
    elif x == y:
        print(n,'is a balancing number with r=',j)