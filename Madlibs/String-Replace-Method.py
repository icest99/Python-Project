## String Replace Method: it replace one string (specified by us) with another string (that we specified)
string = "this is a string"
string = string.replace("is", "was")
print("1: "+ string)

##using variable as an argument for string.replace() method
string = "this is a string"

string1 = str(input("Enter a string:"))
string = string.replace("is", string1)
print("2: "+ string)