# Project 2 — Number Guessing Game
# Author: your name here

import random

secret = random.randint(1, 10)
guesses = 0

guess = int(input("Guess a number between 1 and 10: "))
guesses += 1

while guess != secret:
    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Try again: "))
    guesses += 1

print(f"🎉 Correct! You got it in {guesses} guess(es)!")
