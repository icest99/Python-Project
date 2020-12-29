#we want to randomize words
import random

#import words list from words.py
from word import words

#utility ASCII 
import string

#since in our words list there is "-" sign or ' ' in some of our words which is not valid for our hangman games, so we have to pick untill we find the valid word using this function.
def get_valid_word(words):
  
  #random.choice will select a random item from a lsit 
  word = random.choice(words)
  
  #select a random words from list until it's valid
  while '-' in word or ' ' in word:
    word = random.choice(words)
  
  #return the result to get_valid_word(words)
  return word.upper()

def hangman():
  word = get_valid_word(words)

  #convert list into a set
  word_letter = set(word) #for keeping track of what the user had already guseed in the word
  alphabet = set(string.ascii_uppercase) #just imported upper case list of character in English dictionaries.
  used_letters = set() # what the user has guessed

  #getting user input
  while len(word_letter) > 0 :

    #' '.join(['a', 'b', 'cd']) --> 'a b cd'
    print('You have used these letters:', ' '.join(used_letters))

    #What current words is (ex, W - R D) ****** interesting way to declare list
    word_list = [letter if letter in used_letters else '-' for letter in word]

    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter!').upper()

    if user_letter in alphabet - used_letters: #if user input a chacracter that havent used yet, then we will add that to the used letter list.
      used_letters.add(user_letter)
      #and if user guessed correctly, decrease letter in the word
      if user_letter in word_letter:

        word_letter.remove(user_letter)

    elif user_letter in used_letters:
      print('You already gussed that letter')

    else:
      print("Invalid character, please type in a valid character")
    
    if len(word_letter) == 0:
      print(f'you guessed it right! it is {word}')

hangman()

#I will add lives later.