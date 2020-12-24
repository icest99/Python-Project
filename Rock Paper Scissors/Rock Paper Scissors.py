#There's so many way to improve these code, but for learning sake. This is good enough. I will revisit these code again in a month or two. to improve it by making it shorter, easier to read

import random

print("Hey! It's time to duel! Let's go!\n ROCK... \n PAPER... \n SCISSOR!!")

round = ''
your_score = 0
computer_score = 0
count = 0

while round != "end":
  
  your_hand = input ("What is your pick? Rock, Paper or Scissor: ").lower()
  
  computer_hand = random.choice(["rock","paper","scissor"])
  
  if computer_hand == your_hand:
    print("It's a tie. Pick again: ") 
  
  elif (computer_hand == "rock" and your_hand == "scissor") or (computer_hand == "paper" and your_hand == "rock") or (computer_hand == "scissor" and your_hand == "paper"):
    print("Haha, I win!. ")
    computer_score += 1
    count +=1

# R>S, S>P, P>R

  elif (computer_hand == "scissor" and your_hand == "rock") or (computer_hand == "scissor" and your_hand == "paper") or (computer_hand == "paper" and your_hand == "rock"):
    print("F%$#, you win this time.")
    your_score += 1
    count +=1

  else:
    print("That's a wrong input!")

  if count == 3:
    if computer_score > your_score:
      print("Yup, It's me the winner.")
    else:
      print("S%#t, i need to upgrade my cpu. you won, player.")
    
    break

#improvement idea: I should try to use def,return. more, break the game into two big part, user input and winning condition. add these to def and combine them together. it will make code shorter and more portable.
