## This script follows the lesson from our third and final python meeting!

# We are going to practice writing a function, it needs to be at the start of the script so the rest of our code can utilize it

import pprint
from typing import Type


def stringify_lists(z):
    z_string = [] # Blank list
    for value in z:
        z_string.append(str(value)) # Append a adds values to the list
    return z_string

sample_list = stringify_lists([7, 8, 9, 10]) # Output should convert each item to a string
print(sample_list)

##############################

# Now we will write a function for converting Celsius to Farhenheit
# The chunk below basically details what the function is doing, in case you forget later and don't want to read the code lol

''' "doc_string"

Converts temperature from Celsius or Farhenheit to the other!

'''

def tempverter(temperature, convert_to):
    assert type(temperature) is int or type(temperature) is float, "I need a number to work with, Mary."
    assert convert_to in ["F", "C"], "Sorry I simply don't have the range, darling."
    if convert_to == "F":
        final = (temperature * (9/5)) + 32
    elif convert_to == "C":
        final = (temperature - 32) * (5/9)
    return final

test_temp = tempverter(212, "C")
print(test_temp, "1st Sample")

test_temp2 = tempverter(100, "F")
print(test_temp2, "2nd Sample")

# Alternatively we could use this:

def convert_fc(temperature, convert_to):
    try:
        if convert_to == "F":
            final = temperature * (9/5) + 32
        elif convert_to == "C":
            final = (temperature - 32) * (5/9)
        return final
    except UnboundLocalError:
        print("ERROR: Not using valid temperature system!.")
    except TypeError:
        print("ERROR: Are you sure that was a number?")
        
test_temp3 = convert_fc(100, "F")
print(test_temp3, "3rd Sample")

failed_temp = convert_fc(300, "Z")
print(failed_temp, "4th Sample, FAILURE")


##############################

x = [1.0, 2.0, 3.0, 4.0, 5.0] # Creating an list
print(str(x))
# Using str(x) will not work bc it will convert the entire list to one string, not individuals
# We can create a for-loop to make this function work for us:

x_string = [] # Blank list
for value in x:
    x_string.append(str(value)) # Append a adds values to the list
print(x_string)

# Can also be done in one line with LIST COMPREHENSION
x_string = [str(value) for value in x]
print(x_string)

#############################
# For this example to work you need to be in the correct file directory within the terminal below.
import pprint

input_file = "sample.txt" # A random text file I threw together for this.

# Modes:
# "r" - read
# "w" - write aka OVERWRITE
# "a" - append aka ADD TO

input_file_handler = open(input_file, "r")
print(input_file_handler)

lines = input_file_handler.readlines()
pprint.pprint(lines)

entire_file = input_file_handler.read()

pprint.pprint(lines)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(entire_file) # Prints blank bc the 'entire overview' is blank itself.

# You need to close files because the script will keep it open until the script is closed out
input_file_handler.close()

# Or you can complete all of the above without specifying close using this method:

with open(input_file, "r") as f:
    print(f)
    lines = f.readlines()
    pprint.pprint(lines)
    entire_file = f.read()
    pprint.pprint(lines)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(entire_file) # Prints blank bc the 'entire overview' is blank itself.

# File is now automatically closed!
# Now we will practice writing a text file w Python

new_file = "new_sample.txt"

with open(new_file, "w") as d:
    d.write("My dog Winnie is the best! \n\n")
    d.write("I am being deadass!")

with open(new_file, "a") as c:
    c.write("\n\n\n\n")
    c.write("I would like to add [append] that she smells like fresh laundry!")

# Printing out each letter as its own line using a for-loop
alpha = "abcdefghijklmnopqrstuvwxyz"
for letter in alpha:
    if letter == "a":
        continue
    print(letter)

# We could also try this instead
for letter in alpha:
    if letter != "a":
        print(letter)