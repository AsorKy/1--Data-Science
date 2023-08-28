"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Calculate a random number
FILE TYPE   : Calculate a random number
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#///////////////   Python Program to generate random numbers     ///////////////
#///////////////   Python Program to generate random numbers     ///////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#EXERCISE:
# Write a function called randomization that takes as input a 
# positive integer n, and returns A, a random n x 1 Numpy array. 
#///////////////////////////////////////////


#///////////////////////////////////////////
#User Inputs
#///////////////////////////////////////////

try:
    score = input("Enter the number the score of a student:")
    s = float(score)
except:
    print("Dude, enter a number, no a string.")
    sys.exit()


if s >= 0.9 and s >= 0 and s <= 1.0:
    print("Your grade is A")
elif s >= 0.8 and s >= 0 and s < 0.9:
    print("Your grade is B")
elif s >= 0.7 and s >= 0 and s < 0.8:
    print("Your grade is C")
elif s >= 0.6 and s >= 0 and s < 0.7:
    print("Your grade is D")
elif s < 0.6 and s >= 0 and s < 1.0 :
    print("Your grade is F")
    
else:
    print("Your grade is out of range")