print("Hello World!")
x = 12 # Variables are defined with '=' in python
y = 87
z = 999

print((x + y)/z) # Print shows the contents, here we just create an EQ with the variables above

sequence = "AGCTAAGTCCCAAGTCAAGGGTCCACACTATATCATAGGAGAGAAAGATT" # Defining a random DNA seq
sequence_length = len(sequence)
print(sequence_length)

if sequence_length % 3 == 0:
    print("YAS! Codons have been found queen!")
else:
    print("Oopsie! No codons here baby!")
    if sequence_length % 3 == 1:
        print("Yikes, she isn't a codon Jim! Also, remainder is 1")
    elif sequence_length % 3 == 2:
        print("Oof, this is NOT a codon either AND your remainder is 2")
    else:
        print("Sir, this is an Wendy's.")
r = sequence_length % 3
if r == 0:
    print("Woohoo, codons found!")
else:
    print("Ugh, no codons found!!", "Remainder is:", r)

assert r == 0, "\n\n You dont have codons! Sucks to suck!"
print("Ready to translate!")