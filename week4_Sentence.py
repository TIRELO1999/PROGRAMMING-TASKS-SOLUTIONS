"""
Write a program that accepts a sentence as input in which all of
the words are run together but the first character of each word is
uppercase. Convert the sentence to a string in which the words are
separated by spaces and only the first word starts with an uppercase letter.

************ Example ************
“TireloIsAProgrammer.” would be converted to “Tirelo is a programmer.”
********************************

######################################## HINT #################################################
Remember the idea here is to iterate over al characters in the user's sentence except the first,
then check if the character is uppercase , and if it is, then concatenate the fixed string we are
building with a space and a lowercase version of the letter, but if the character is lowercase,then
that letter is concatented as it is
####################################################################################################


===================== CODING WITH CLIFFORD ========================

"""

#Read the string from the user without spaces and with CAPS letter per word
sentence=input("Enter your Sentence (without spaces) with CAPS letter per word :")
#This creates a new string containing the first letter of the string from the user
fixed_sentence=sentence[0]

for character in sentence[1:]: #loops from the 2nd letter of the user' string
    if character.isupper():
        #adds the uppercase letter as lowercase to the fixed sentece
        fixed_sentence += " " + character.lower()
    else:
        fixed_sentence+= character # adds the letter to the fixed string as lowercase

#prints the fixed string
print(fixed_sentence)