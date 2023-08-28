"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Vectorise a function
FILE TYPE   : Vectorise a function
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#///////////////////   Python Program to Vectorise a function  /////////////////
#///////////////////   Python Program to Vectorise a function  /////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#EXERCISE:
# scalar_function can only handle scalar input, we could use the function 
# np.vectorize() turn it into a vectorized function. Note that the input 
# argument of np.vectorize() should be a scalar function, and the output of 
# np.vectorize() is a new function that can handle vector input.
# Please write a vector function vector_function, which will apply the 
# operation  defined above element-wisely with input vectors with same 
# dimension x and y.
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

def vector_function(x, y):
    vfunc = np.vectorize(scalar_function)
    return vfunc(x,y)

print(vector_function(X, Y))