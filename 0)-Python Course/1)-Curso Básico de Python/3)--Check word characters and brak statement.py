"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Run through a text
FILE TYPE   : Run through a text and break concept
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

def run():
    text = input("Hi dude, give me a text:")
    stopword = input("Dude, which word do you want to omit?:")
    upper    = input("""Dude, you want to print upper or lower letter?:
                     1--type lower
                     2--type upper
                     
                     choose an option
                     """).lower()
                     
    
    for character in text:
        if character.lower() == stopword.lower():
            break
        else:
            if upper == "lower".lower():
                print(character.lower())
            elif upper == "upper".lower():
                print(character.upper())
            else:
                print("Bro, type a valid option.")
                

if __name__ == "__main__":
    run()
        
        

        