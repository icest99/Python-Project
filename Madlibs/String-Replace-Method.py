## String Replace Method: it replace one string (specified by us) with another string (that we specified)
string = "this is a string"
string = string.replace("is", "was")
print("1: "+ string)

##using variable as an argument for string.replace() method
string = "this is a string"

string1 = str(input("Enter a string:"))
string = string.replace("is", string1)
print("2: "+ string)

##Creating a text file for MadLibs, put story with some "blank" inside the file. 'String-Replace-Method-Madlibs.txt'

import random
import os

# Get the current working directory (cwd)
cwd = os.getcwd()

# Get all the files in that directory
#files = os.listdir(cwd)
#print("Files in %r: %s" % (cwd, files))

# Change the current working directory to where the txt file is.
os.chdir('E:\Python Project\Madlibs')

#Open madlib text file. 'r' = open for reading (default)
mopen = open('madlibs.txt','r')

#Read the whole file and store each line in a list. 'readlines' method read and return every line from the file in a format of list. 'readline' method will only read and return a single line.
madlibtxt = mopen.readlines()

#Choose a random line from the list "random.choice(sequence)" sequence can be list, string, tuple. This function return a single items from the sequence.
madlib = random.choice(madlibtxt)
print(madlib)

#ask user to input a word
word = input("Enter a word: ")

#replace the blank with user's input
result = madlib.replace("blank", word)
print(result)