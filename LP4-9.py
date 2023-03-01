import random

botnum = random.randint(1,20)

guess=input("Guess the Number Generated (1-20):")

if str(botnum) == str(guess):
  print("Correct!")
else:
  print("Incorrect!")
  print(str(botnum) + " " + str("was the number."))
  print("You guessed!" + " " + str(guess))