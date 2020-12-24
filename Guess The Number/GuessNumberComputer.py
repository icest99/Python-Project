import random

def computer_Guess():
  x, y = input("Enter lower bar and higher bar. For example, ""'20 50'\n").split()
  
  #This is my first time using f-string and it felt so good lmao. it's so easy to use and read.
  print(f"The lower bar is {x} , the upper bar is {y}")
  print("I will try to guess it now!")
  
  #count how many time the computer has guessed.
  count = 0
  ans = ""
  
  while ans != "c":

    #computer random the number to guess
    random_num = random.randint(int(x), int(y))

    print(f"I Guess {random_num}")

    ans = input(f"is {random_num} correct? [C], too high? [H], or too low? [L]: ").lower()
    
    if ans == "h":
      print("Ok, I will try guessing lower!")
      y = random_num - 1
    elif ans == "l":
      print("Ok, I will try guessing higher!")
      x = random_num + 1
    elif ans == "c":
      print("I'm correct!? Yes, I knew it. Now end this.")
    else:
      print("Hey, you're giving the wrong feedback. you need to enter C, H, or L for feedback!.\n now try again!")
    count += 1
  print(f"I guessed {count} time(s)!")
computer_Guess()