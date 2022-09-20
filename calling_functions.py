#By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Name:  Ryan Kethley

# Section:   565
# Assignment: 3.15 LAB: Unit Conversions
# Date:  9/8/22

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

#area equations
side = float(input("Please enter the side length:\n"))
h = (1/2)*(sqrt(3)*side)
TriangleArea = (1/2)*(side*h)
SquareArea = side*side
PentagonArea = side**2*(1/4)*(sqrt(5*(5+2*sqrt(5))))
DodecagonArea = (3)*(2+sqrt(3))*(side**2)
#Area results
printresult("triangle", side, TriangleArea)
printresult("square", side, SquareArea)
printresult("pentagon", side, PentagonArea)
printresult("dodecagon", side, DodecagonArea)