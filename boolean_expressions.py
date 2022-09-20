# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ryan Kethley
#               Sam Kinnard
#               Caleb Lorimor
#               Evan Slyter
# Section:      513
# Assignment:   LAB: topic 2 (team) part 1
# Date:         DAY MONTH YEAR
#

############ Part A ############

z = True
x = False


value_a = input('Enter True or False for a: ')
value_b = input('Enter True or False for b: ')
value_c = input('Enter True or False for c: ')

if value_a == 'True' or value_a == 'T' or  value_a == 't':
   value_a = z
else:
    value_a = x

if value_b == 'True' or value_b == 'T' or value_b == 't':
    value_b = z   
else: 
    value_b = x   
    
if value_c == 'True' or value_c == 'T' or value_c == 't':
   value_c = z
else:
   value_c = x

############ Part B ############

print('a and b and c:', value_a and value_b and value_c)

print('a or b or c:', value_a or value_b or value_c)

############ Part C ############

print('XOR:', value_a and not value_b or not value_a and value_b)

print('Odd number:',  not (not value_a or value_b or value_c) and (value_a or not value_b or value_c) or (value_a or value_b or not value_c) )

