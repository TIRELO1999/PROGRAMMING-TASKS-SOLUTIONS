"""
********************* PROBLEM STATEMENT ***********************************
Write a program that will take a string from the user and extract
VOWELS from that string. Then the program should be able to print
the STRING OF VOWELS and SORTED STRING OF THOSE VOWELS.

Example
String = " Tirelo "
Vowels = ieo
Sorted Vowels = eio
****************************************************************************

######################################################
This program takes a string from the user and extract vowels from that
string then sort them , then prints the results.
######################################################

NOTE : There are many ways this problem can be solved


========== CODING WITH CLIFFORD ==========
========== www.codingwithclifford.tk ==========

"""

vowels="aeiou" # String of all vowels
user_string=input("Enter your string here  :") #records the string from the user in user_string
string_vowels="" # empty string of vowels from the the user_string

user_string=user_string.lower()
#this for loop is used to extract the vowels from the user string
for val in  user_string:#loops through the user_string variable
    if val in vowels: # executes if the character in user_string is in vowels variable
        string_vowels+= val
sorted_vowels = "".join(sorted(string_vowels)) # records the sorted vowels extrated from the user_string
print("*****"*15)

#prints the results
print(" String        : {0} \n Vowels        : {1} \n Sorted Vowels : {2}".format(user_string,string_vowels,sorted_vowels))












#                                                          CODING WITH CLIFFORD