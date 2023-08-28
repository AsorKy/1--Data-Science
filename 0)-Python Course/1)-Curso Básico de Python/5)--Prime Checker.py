"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Prime checker project
FILE TYPE   : Or and Loop concepts
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#//////////////////////////////  Prime Checker  ////////////////////////////////
#//////////////////////////////  Prime Checker  ////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#5)-Prime Checker
# Create an algotihm that checks if a numer is prime or not
#///////////////////////////////////////////

def prime_checker(Number):
    
    counter = 0
    
    for i in range(1, Number + 1):
        if i == 1 or i == Number:
            continue
        if Number % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False
            
        

def run():
    numer = int(input("Dude, enter a number:"))
    
    if prime_checker(numer):
        print("Dude, effectivelly you have a prime numer")
    else:
        print("Dude, you dont have a prime numer")


if __name__ == "__main__":
    run()