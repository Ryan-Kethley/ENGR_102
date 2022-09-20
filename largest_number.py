#By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Name:  Ryan Kethley

# Section:   565
# Assignment: 3.15 LAB: Unit Conversions
# Date:  9/8/22

from math import *

#Largest Number Code
a = float(input("Enter number 1:\n"))
b = float(input("Enter number 2:\n"))
c = float(input("Enter number 3:\n"))

if a > b and a >= c:
    print(f' The largest number is {a:.1f}')
if b > a and b > c:
    print(f' The largest number is {b:.1f}')
if c > a and c > b:
    print(f' The largest number is {c:.1f}')
    
