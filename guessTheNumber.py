import random

print("I am thinking of a number between 1 and 20")
print("Take a guess")

number = random.randint(1,20)

guess = int(input())

while(guess!=number):
    if (guess<number):
        print("Your guess is too low")
    elif (guess>number):
        print("Your guess is too high")

    guess = int(input())

print("Congrats you guessed the right number")
