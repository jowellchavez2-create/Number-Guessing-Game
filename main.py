import os
import time
import random

def cleanscreen():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    cleanscreen()
    print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 10.

Please select the difficulty level:

1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
""")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            easy()
        elif choice == 2:
            medium()
        elif choice == 3:
            hard()
        else:
            print("Error, insert a correct number.")
            time.sleep(1.5)
    except ValueError:
        print("Error, insert a correct number.")
        time.sleep(1.5)

def easy():
    cleanscreen()
    number = random.randint(1,10)
    attemps = 1
    print("""
Great! You have selected the Easy difficulty level.
Let's start the game!
""")
    while attemps < 12:
        guess = int(input("Enter your guess: "))
        if attemps == 10:
            print("Game over, try again.")
            time.sleep(2.5)
            break
        elif guess != number:
            attemps += 1
        elif guess == number:
            print(f"Congratulations! You guessed the correct number in {attemps} attempts.")
            time.sleep(2.5)
            break

def medium():
    cleanscreen()
    number = random.randint(1,10)
    attemps = 1
    print("""
Great! You have selected the Medium difficulty level.
Let's start the game!
""")
    while attemps < 7:
        guess = int(input("Enter your guess: "))
        if attemps == 5:
            print("Game over, try again.")
            time.sleep(2.5)
            break
        elif guess != number:
            attemps += 1
        elif guess == number:
            print(f"Congratulations! You guessed the correct number in {attemps} attempts.")
            time.sleep(2.5)
            break

def hard():
    cleanscreen()
    number = random.randint(1,10)
    attemps = 1
    print("""
Great! You have selected the Hard difficulty level.
Let's start the game!
""")
    while attemps < 5:
        guess = int(input("Enter your guess: "))
        if attemps == 3:
            print("Game over, try again.")
            time.sleep(2.5)
            break
        elif guess != number:
            attemps += 1
        elif guess == number:
            print(f"Congratulations! You guessed the correct number in {attemps} attempts.")
            time.sleep(2.5)
            break

while True:
    menu()
