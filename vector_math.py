# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ryan Kethley
# Section:      565
# Assignment:   7.27 LAB: Vector Math
# Date:         13 October 2022

#input the vectors
from math import *
vectorA = input("Enter the elements for vector A: ").split()
vectorB = input("Enter the elements for vector B: ").split()

#Find the magnitude 
A = [float(x) for x in vectorA]
magA = 0
for i in range(len(A)):
    magA += (A[i]**2)
print(f"The magnitude of vector A is {sqrt(magA):.5f} ")

B = [float(x) for x in vectorB]
magB = 0
for i in range(len(B)):
    magB += (B[i]**2)
print(f"The magnitude of vector B is {sqrt(magB):.5f} ")

#find a - b, a + b and dor product
AplusB = []
AminusB = []
dotproduct = 0

for i in range(len(A)):
    AplusB.append(A[i] + B[i])
print(f'A + B is {AplusB}')

for i in range(len(A)):
    AminusB.append(A[i] - B[i])
print(f'A - B is {AminusB}')

for i in range(len(A)):
    dotproduct += (A[i] * B[i])
print(f'The dot product is {dotproduct:.2f}')
