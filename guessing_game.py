# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Ryan Kethley
# Section:   565
# Assignment: 10.14 LAB: Guessing Game
# Date: 11/01/22

from sys import exit

#define variables
count = 1
user_guess = 1
value = 26

#first function
def high_or_low(guess):
    if int(guess) < value:
        print("Too low!")
    if int(guess) > value:
        print("Too high!")

#second function
def is_number(guess):
    if int(guess) == value:
        print(f"You guessed it! It took you {count} guesses.")
        exit()
        
#third function
def input_okay(guess):
    while True:
        try:
            guess = float(guess)
        except:
            print("Bad input! Try again:", end="")
            guess = input()
        if float(guess) == int(float(guess)):
            return int(guess)
        else:
            print("Bad input! Try again: ", end="")
            guess = input()

#print statements
print("Guess the secret number! Hint: it's an integer between 1 and 100...")
user_guess = input("What is your guess? ")
while user_guess != (value):
    user_guess = input_okay(user_guess)
    is_number(user_guess)
    high_or_low(user_guess)
    count += 1
    user_guess = input("What is your guess? ")
    

