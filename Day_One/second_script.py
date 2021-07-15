#### Setting up Variables ####
sequence = "AGCTGCAAATTCGAGAGTCATAGGGCATCCTAAGATTGAGTCTGA"
sequence_length = len(sequence)
print(sequence_length)

nuc = "A"
purines = ["A", "G"]
pyrimidines = ["C", "T"]

#### Indexing in Python ####
pyrimidines.append("U") # Addings Uracil to the list of pyrimidines, this change is MUTABLE bc it is a list NOT a string

name_string = "YASicholas"
name_string.replace("N", "YAS") # Will not change string unless we REDFINE it bc lists are IMMUTABLE
print(name_string)

print(purines[0]) # Indexing starts at 0 in Python, so to list the first value we use 0
print(pyrimidines[2]) # Now includes 'U' because we ran a method on the list

# function(argument) Can accept multiple variety of inputs
# value/variable.method() Specifically tied to a type of input, cannot accept others
# If we wanted to examine every other variable in a list we would add a third number to the identifer
# Example of every other: list[1:10:2]

#### Creating a For-Loop ####
if nuc == "A":
    print("purine")
elif nuc == "G":
    print("purine")
elif nuc == "T":
    print("pyrimidine")
elif nuc == "C":
    print("pyrimidine")

# Using 'elif' allows us to keep the entire script from running, rather than collecting 'if's
# However, we are HARD CODING which is bad! We will adjust the script to reflect positive changes

if nuc in purines:
    print("purine")
elif nuc in pyrimidines:
    print("pyrimidine")

i = 1
for base in sequence:
    if base in purines:
        print("Nucleotide", i, "is a purine")
    elif base in pyrimidines:
        print("Nucleotide", i, "is a pyrimidine")
    i += 1

#HOMEWORK = for i in range(len(sequence)):
# For loop to COUNT (method) purines and pyrimidines without hard coding, involves nested for loops

total_purine = 0
total_pyrimide = 0
for base in sequence:
    if base in purines:
        total_purine += 1
    elif base in pyrimidines:
        total_pyrimide += 1
assert total_pyrimide + total_purine == sequence_length, "womp womp"

print("Total purines found:", total_purine)
print("Total pyrimidines found:", total_pyrimide)