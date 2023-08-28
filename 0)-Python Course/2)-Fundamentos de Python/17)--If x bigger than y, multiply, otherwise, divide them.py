"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : If x<=y, multiply, otherwise, divide them
FILE TYPE   : If x<=y, multiply, otherwise, divide them
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#/////////   Python Program If x<=y, multiply, otherwise, divide them  /////////
#/////////   Python Program If x<=y, multiply, otherwise, divide them  /////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#EXERCISE:
# Let's start with writing a scalar function scalar_function, 
# which will apply the following operation with input x and y.
#///////////////////////////////////////////


#///////////////////////////////////////////
#User Inputs
#///////////////////////////////////////////

X = np.random.random()
Y = np.random.random()

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here
    if x <= y:
        s = x*y
    else:
        s = x/y
    return s

print(scalar_function(X, Y))