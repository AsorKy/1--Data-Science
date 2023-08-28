"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Palindrome project
FILE TYPE   : Text inversion and lower method
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#////////////////////////////  Run through a text  /////////////////////////////
#////////////////////////////  Run through a text  /////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#3)-Run through a text
# Create an algotihm that runs through the characters of a text entered by console
# in such a way that it modifies them in capitalization or minimization  as indicated
# by the user. Also indicate a forbiden character un such a way that when it is detected 
# the program stops operating.
#///////////////////////////////////////////


def palindrome(words):
    words = words.replace(" ","")
    words = words.lower()
    inverted_words = words[::-1]
    if words == inverted_words:
        return True
    else:
        return False
    
def run():
    word = input("Dude, give me a word to check if it is a palindrome:")
    test = palindrome(word)
    if test == True:
        print("Dude, your word is a palindrome")
    else:
        print("Sorry dude, your word is not a palindrome")



if __name__ == '__main__':
    run()
