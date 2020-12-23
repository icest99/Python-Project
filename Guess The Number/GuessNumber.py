import random
import math
#user might put the wrong number in. that might generate error so this function will help us bypass it. 
# also when input something that's lower or higher than the range, it just break and freakout
# i will fix that later! it works fine for now. (decem 23, 2020)

def guessNum():
  print("select two numbers for a range of number")
  a = int(input("Insert upper: " ))
  b = int(input("Insert lower: " ))
  print (type(b))

  minimumGuess = round(math.log(a - b + 1, 2))
  print("you have: " + str(minimumGuess) + " guesses.")
  ranNum = random.randint(b,a)

  #initialize the number of guesses.
  count = 0

  #making a loop to keep asking user until they guessed correctly, or too many time.
  while count != minimumGuess + 1:

    if count >= minimumGuess:
      print("You guessed too many time!")
      break

    guess = int(input("from " + str(a) + " to " + str(b) + ", Guess a number: "))

    if guess == ranNum:
      print("Correct!")
      print("You guessed "+ str(count) + " times!")
      if 
      break

    elif guess > ranNum:
      print("you guessed too much, try lower.")
      count += 1
    elif guess < ranNum:
      count += 1
      print("you guessed too low, try higher.")

guessNum()
